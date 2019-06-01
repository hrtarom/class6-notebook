# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 00:44:19 2019

@author: Hamid.t
"""
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import load_breast_cancer

import os
data = load_breast_cancer()

df  = pd.DataFrame(data.data)

df.columns= data.feature_names
df['target_label']=data.target

os.makedirs('./plots', exist_ok=True)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.scatter(df['mean fractal dimension'], df['mean radius'], 
          df['mean symmetry'],marker='o',alpha=0.3,s=100)




plt.style.use('ggplot')

plt.savefig(f'plots/3Dscatter.png', dpi=300)
plt.close()

count=df.groupby('target_label').size()
plt.pie(count,labels=['malignant', 'benign'],shadow=True, startangle=140)
plt.title("The number of instances from each group")


plt.savefig(f'plots/pie.png', dpi=300)