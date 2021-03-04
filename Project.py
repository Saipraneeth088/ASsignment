import numpy as np
import pandas as pd
import warnings
import pickle
warnings.filterwarnings("ignore")

data = pd.read_csv("C:/Users/saipr/Documents/Assign/loan short.csv")
data.isnull().values.any()
data.dropna()
print(data)

data=pd.DataFrame(data)
data = np.array(data)




pickle.dump(data,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))
