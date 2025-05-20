import numpy as np
import pandas as pd
import altair as alt
from lib import *


def species_generator(mu1, sigma1, mu2, sigma2, n_samples, target, seed):
    # mu1 is the mean weight
    # mu2 is the  mean wingspan
    rand = np.random.RandomState(seed)
    f1 = rand.normal(mu1, sigma1, n_samples)
    f2 = rand.normal(mu2, sigma2, n_samples)
    X = np.array([f1, f2])
    X = X.transpose()
    y = np.full((n_samples), target)
    return X, y



albatross_weight_mean = 9000 # in grams
albatross_weight_variance =  800 # in grams
albatross_wingspan_mean = 300 # in cm
albatross_wingspan_variance = 20 # in cm 
n_samples = 100
target = 1
seed = 100

# aX: feature matrix (weight, wingspan)
# ay: target value (1)
aX, ay = species_generator(albatross_weight_mean, albatross_weight_variance,
                           albatross_wingspan_mean, albatross_wingspan_variance,
                           n_samples,target,seed )


albatross_dic = {'weight-(gm)': aX[:,0],
                 'wingspan-(cm)': aX[:,1], 
                 'species': ay,
                 'url': "https://raw.githubusercontent.com/pabloinsente/nn-mod-cog/master/notebooks/images/albatross.png"}


# put values in a relational table (pandas dataframe)
albatross_df = pd.DataFrame(albatross_dic)

owl_weight_mean = 1000 # in grams
owl_weight_variance =  200 # in grams
owl_wingspan_mean = 100 # in cm
owl_wingspan_variance = 15 # in cm
n_samples = 100
target = -1
seed = 100

# oX: feature matrix (weight, wingspan)
# oy: target value (1)
oX, oy = species_generator(owl_weight_mean, owl_weight_variance,
                           owl_wingspan_mean, owl_wingspan_variance,
                           n_samples,target,seed )

owl_dic = {'weight-(gm)': oX[:,0],
             'wingspan-(cm)': oX[:,1], 
             'species': oy,
             'url': "https://raw.githubusercontent.com/pabloinsente/nn-mod-cog/master/notebooks/images/owl.png"}

# put values in a relational table (pandas dataframe)
owl_df = pd.DataFrame(owl_dic)


# df = albatross_df.append(owl_df, ignore_index=True)
df = pd.concat([albatross_df, owl_df], ignore_index=True)
