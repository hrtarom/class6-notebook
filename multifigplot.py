# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 00:41:37 2019

@author: Hamid.t
"""
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer

import os
data = load_breast_cancer()

df  = pd.DataFrame(data.data)

df.columns= data.feature_names
df['target_label']=data.target

os.makedirs('./plots', exist_ok=True)
fig, axes = plt.subplots(2, 2, figsize=(10,10))

axes[0][0].scatter(df.iloc[:,0], df.iloc[:,1],  color='brown', marker='*')
axes[0][0].set_title(f'{df.columns[0]} to {df.columns[1]}')
axes[0][0].set_xlabel(df.columns[0])
axes[0][0].set_ylabel(df.columns[1])

            
axes[0][1].scatter(df.iloc[:,0], df.iloc[:,2],  color='brown', marker='*')
axes[0][1].set_title(f'{df.columns[0]} to {df.columns[2]}')
axes[0][1].set_xlabel(df.columns[0])
axes[0][1].set_ylabel(df.columns[2])


axes[1][0].scatter(df.iloc[:,0], df.iloc[:,3],  color='brown', marker='*')
axes[1][0].set_title(f'{df.columns[0]} to {df.columns[3]}')
axes[1][0].set_xlabel(df.columns[0])
axes[1][0].set_ylabel(df.columns[3])


axes[1][1].scatter(df.iloc[:,0], df.iloc[:,4],  color='brown', marker='*')
axes[1][1].set_title(f'{df.columns[0]} to {df.columns[4]}')
axes[1][1].set_xlabel(df.columns[0])
axes[1][1].set_ylabel(df.columns[4])



plt.tight_layout()

plt.savefig(f'plots/multivoilinplot.png', dpi=300)
plt.close(fig)


plt.close()