# -*- coding: utf-8 -*-
"""
Created on Fri May 31 17:49:31 2019

@author: Hamid.t
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer

import os
data = load_breast_cancer()

df  = pd.DataFrame(data.data)

df.columns= data.feature_names
df['target_label']=data.target

os.makedirs('./plots', exist_ok=True)


for col1_idx, column1 in enumerate(df.columns):
    for col2_idx, column2 in enumerate(df.columns):
        if col1_idx < col2_idx:
                sns.relplot(x=df.columns[col1_idx],y= df.columns[col2_idx],
                            data=df,kind='scatter',col='target_label',color='g')
                plt.tight_layout()
                plt.savefig(f'plots/{column1}_{column2}.png', dpi=300)
                
plt.close()







   

