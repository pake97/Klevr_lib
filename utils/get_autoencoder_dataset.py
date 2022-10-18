
import optuna
from optuna.trial import TrialState
import torch 
import torch.nn as nn
import numpy as np
import gc
import random
from rdflib import Graph,Namespace


def get_autoencoder_dataset(i,index,mapping_entities,mapping_properties, train_pre_path,train_materialized_path,ontology_materialized_path, batch_size,max_e,max_p):
    X_train=[]
    Y_train=[]
    
    #counter = 0
    for j in range(i*100+index*1000,(i+1)*100+index*1000):
    #for filename in os.listdir("/home/ubuntu/data/home/ubuntu/deeplogic/el_dataset/x"):
        n = Namespace("http://example.org/")
        g1 = Graph()
        g1.bind("ex",n)
        g1.parse(train_pre_path.format(j), format="turtle")
        spo_tensor= embed(mapping_entities,mapping_properties,g1,max_e,max_p)
        
        X_train.append(spo_tensor)
        g2 = Graph()
        g2.bind("ex",n)
        g2.parse(train_materialized_path.format(j),format="turtle")

        g3 = Graph()
        g3.parse(ontology_materialized_path, format="ttl")

        graph = g2 - g3
        graph.bind("ex",n)

        spo_tensor, mapping_entities,mapping_properties = embed(mapping_entities,mapping_properties,graph,max_e,max_p)
        Y_train.append(spo_tensor)
    train_x = torch.from_numpy(np.array(X_train)).float()
    train_y = torch.from_numpy(np.array(Y_train)).float()
    

    


    # Pytorch train and test sets
    train = torch.utils.data.TensorDataset(train_x,train_y)

    # data loader
    train_loader = torch.utils.data.DataLoader(train, batch_size = batch_size, shuffle = False)

    return train_loader,len(X_train), mapping_entities,mapping_properties

        
    