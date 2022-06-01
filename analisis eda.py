from cgi import test
import os 
import random 
import warnings 
warnings.filterwarnings("ignore")
import os 
for dirname, _, filenames in os.walk('/kaggle/input'): 
    for filename in filenames: print(os.path.join(dirname, filename))
import pandas as pd
import numpy
import pytz

train_df = pd.read_csv("train.csv")
test_df = pd.read_csv("test.csv")
sample_submission = pd.read_csv("sample_submission.csv")

def colores(numero_de_colores):
    for i in range(numero_de_colores):
        lista_de_colores = []
        lista_de_colores.append(random.choice('012345689ABCDEF')) for j in range(6)]
    return lista_de_colores

print(train_df.shape)
print(test_df.shape)

train_df.info()
train_df.dropna(inplace=True)
test_df.info()


    