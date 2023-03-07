import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit

"""
Title Training of ML algorythm with californian housing data sets
"""

#Loading of data_sets######################################
dataset = pd.read_csv("datasets/housing/housing.csv")

#Analyse of the datasets#########################################

############################Panda###########################

"""
dataset.head()
dataset.info()
dataset.describe()
"""

""" 
MEMORY METHOD ANALYSE:
.info() permet d'obtenir une description des données en particuliers le nombre total de lignes, le type de chaque variables
et le nombre de valeurs non nuls.

.head() affiche les 5 premières lignes du data_sets

.describe présente un récapitulatif statistique du data_sets
"""
#############################Matplotlib#########################

"""
dataset.hist(bins = 50, figsize = (20,15))# Plus le bin est élevée plus le graphique est précis
plt.show()
"""

#CREATION OF A DATA_SET_TEST#########################################


#############################SciKit-Learn#########################

#échantillonage prise aléatoirement et non représentative

#train_set, test_set = train_test_split(dataset, test_size = 0.3, random_state = 42)

#échantillonnage représentative

split = StratifiedShuffleSplit(n_splits= 1, test_size= 0.2, random_state= 42)
for train_index, test_index in split.split(dataset, dataset["income_cat"]):
    strat_train_set = house.loc[train_index]
    strat_test_set = house.loc[test_index]

print(strat_test_set["income_cat"].value_counts()/len(strat_test_set))












