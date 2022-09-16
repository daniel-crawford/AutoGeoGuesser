from A2GDataloader import *


# Initialize and Load in Data
dl = A2GDataLoader()
dl.load_data_path_label()
xtrain, ytrain, xtest, ytest = dl.get_train_test(0.8)

print(ytest)