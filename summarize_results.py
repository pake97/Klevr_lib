import os
import json

def read_json(file):
    data={}
    with open(file) as f:
        data = json.load(f)
    return data

def write_json(file,data):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main(directory):
    results={}
    for filename in os.scandir(directory):
        results[filename.name.split('_')[-1]]={}
        f = os.path.join(directory+"/"+filename.name, 'results.json')
        results[filename.name.split('_')[-1]]=read_json(f)
    write_json('ui/embedding_result.json',results)


if __name__ == '__main__':
    main('embedding_models')
