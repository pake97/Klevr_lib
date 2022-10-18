import optuna
from optuna.trial import TrialState
import torch 
import torch.nn as nn
import numpy as np
import gc
from rdflib import Graph,Namespace

def get_device():
    if torch.cuda.is_available():
        device = 'cuda:0'
    else:
        device = 'cpu'
    return device