
import json
import pandas as pd
from utils.yarrrml_api import Yarrrml_api
import unicodedata
from rdflib import Graph,Namespace
import rdflib
import warnings
from time import time
from utils.jar_wrapper import jarWrapper
from pykeen.models import TransE
from torch.optim import Adam
from pykeen.training import SLCWATrainingLoop
from pykeen.triples import TriplesFactory
import torch
import numpy as np
def open_file(filename):
    data={}
    with open(filename) as f:
        data = json.load(f)
    return data


def from_json_to_ttl(scene):
    api = Yarrrml_api(scene)
    ttl = api.annotate()
    return ttl

def write_temp_file(dict) -> None:
    with open('resources/source.json', 'w') as fp:
        json.dump(dict, fp)

def empty_txt(path)->None:
    file = open(path,"w")
    file.close()

def write_txt(path,line) -> None:
    with open(path, 'a') as f:
        f.write(line)


def write_temp_ttl(response) -> None:
     
    f = open("temp_files/scene.ttl", "w")
    f.write(response)
    f.close()
        
def adjust_scene(scene):
    idx=0
    for obj in scene['objects']:
        obj["id"]="o"+str(idx)+"scene"+str(scene["image_index"])
        obj["hasOnLeft"]=["o"+str(j) for j in scene["relationships"]["left"][idx]]
        obj["hasOnRight"] = ["o" + str(j) for j in scene["relationships"]["right"][idx]]
        obj["hasOnFront"] = ["o" + str(j) for j in scene["relationships"]["front"][idx]]
        obj["hasBehind"] = ["o" + str(j) for j in scene["relationships"]["behind"][idx]]
        obj["hasDirectlyOnLeft"] = ["o" + str(scene["relationships"]["left"][idx][0])] if len(scene["relationships"]["left"][idx])>0 else []
        obj["hasDirectlyOnRight"] = ["o" + str(scene["relationships"]["right"][idx][0])] if len(scene["relationships"]["right"][idx])>0 else []
        obj["hasDirectlyOnFront"] = ["o" + str(scene["relationships"]["front"][idx][0])] if len(scene["relationships"]["front"][idx])>0 else []
        obj["hasDirectlyBehind"] = ["o" + str(scene["relationships"]["behind"][idx][0])] if len(scene["relationships"]["behind"][idx])>0 else []
        obj["color"] = obj["color"].capitalize()
        obj["size"] = obj["size"].capitalize()
        obj["shape"] = obj["shape"].capitalize()
        if(obj["material"] == 'metal'):
            obj["material"] = 'metallic'
        obj["material"] = obj["material"].capitalize()
        idx = idx+1
    return scene


def get_ttl_scene(scene_path):
    scene_graph = Graph()
    scene_graph.parse(scene_path, format='ttl')
    return scene_graph


def main():
     
    data = open_file('./resources/dataset/CLEVR_train_scenes.json')['scenes']
    
    #questions = open_file('./resources/questions/CLEVR_train_questions.json')['questions']
    #question_this_scene = list(filter(lambda d: d['image_index'] in [data[0]['image_index']], questions))
    
    scene = data[3]
    scene = adjust_scene(scene)
    api = Yarrrml_api(scene)
    write_temp_ttl(api.annotate()) 

    #calls jar to merge ontology with the scene and materialize it.
    #java -jar deeplogic.jar ./src/main/resources/scene0.ttl ./
    args = ['hermit_reasoner.jar', './temp_files/scene.ttl', './resources/ontologies/el/KlevR_EL_ttl.ttl','temp_files/'] # Any number of args to be passed to the jar file
    result, done = jarWrapper(*args)

    materialized_scene = get_ttl_scene('temp_files/KlevR_materialized_scene.ttl')
    empty_txt('temp_files/train_file.txt')
    triples_list = []
    for s,p,o in materialized_scene.triples((None,None,None)):

        line=[]
        if '#' in s:
            line.append(s.split("/")[-1].split('#')[-1])

        else:
            line.append(s.split("/")[-1])
        line+="    "
        if '#' in p:
            line.append(p.split("/")[-1].split('#')[-1])

        else:
            line.append(p.split("/")[-1])
        line+="    "
        if '#' in o:
            line.append(o.split("/")[-1].split('#')[-1])

        else:
            line.append(o.split("/")[-1])
        #write_txt('temp_files/train_file.txt',line)
        #write_txt('temp_files/train_file.txt','\n')    
        triples_list.append(line)
    triples_list_np = np.asarray(triples_list,dtype=str)
    training_triples_factory = TriplesFactory.from_labeled_triples(triples=triples_list_np,create_inverse_triples=False)
     
    print(len(triples_list))
    model = torch.load('trained_model.pkl')
    #model = TransE(triples_factory=training_triples_factory)
    
    optimizer = Adam(params=model.get_grad_params())
    # Pick a training approach (sLCWA or LCWA)
    
    training_loop = SLCWATrainingLoop(
        model=model,
        triples_factory=training_triples_factory,
        optimizer=optimizer,
    )


    _ = training_loop.train(
        triples_factory=training_triples_factory,
        num_epochs=5,
        batch_size=256,
    )

    torch.save(model,'trained_model.pkl')
    #my_pykeen_model = torch.load('trained_model.pkl')



if __name__ == '__main__':
    warnings.filterwarnings("ignore")
    main()
    
    
    
