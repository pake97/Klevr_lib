import os
import subprocess
from time import time
bashCommandEL = "java -Xmx10g -Xms10g -jar deeplogic.jar ./src/main/resources/dataset/dataset/valid/el/{} ./src/main/resources/dataset/dataset/valid_materialized/el/"
bashCommandRL = "java -Xmx10g -Xms10g -jar deeplogic.jar ./src/main/resources/dataset/dataset/train/lr/{} ./src/main/resources/dataset/dataset/train_materialized/rlnew/"
bashCommandQL = "java -Xmx10g -Xms10g -jar deeplogic.jar ./src/main/resources/dataset/dataset/train/lq/{} ./src/main/resources/dataset/dataset/train_materialized/ql/"
i=0
t0 = time()
for file in os.listdir("src/main/resources/dataset/dataset/train/el/"):
    #print(bashCommandEL.format(file))
    process = subprocess.Popen(bashCommandEL.format(file).split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    i=i+1
    if(i==10):
        break
t1 = time()