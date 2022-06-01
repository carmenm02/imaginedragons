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

