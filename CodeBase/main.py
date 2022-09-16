import pandas as pd
import matplotlib.pyplot as plt

from A2GDataloader import *


# Initialize and Load in Data
dl = A2GDataLoader()
dl.load_data_path_label()
xtrain, ytrain, xtest, ytest = dl.get_train_test(0.8)











'''
#Some Analysis
inputs_freq = pd.Series(ytrain).value_counts()/len(ytrain)
plt.bar(inputs_freq.index.to_list(),inputs_freq.to_list())


outputs_freq = pd.Series(ytest).value_counts()/len(ytest)
plt.bar(outputs_freq.index.to_list(),outputs_freq.to_list())
'''