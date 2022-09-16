import sys
import os
import random


class A2GDataLoader:
    def __init__(self, dir = './DataBase/'):
        self.dir = dir
        self.path_label = []

    def load_data_path_label(self, paths = None):
        '''
        Return pathnames (up to self.dir) and labels as list of tuples
        '''
        data_path_label=[]
        for country in os.listdir(self.dir):
            for f in os.listdir(os.path.join(self.dir, country)):
                data_path_label.append((os.path.abspath(f),country))
        
        self.path_label = data_path_label

    def get_train_test(self, p):
        random.shuffle(self.path_label)
        n = len(self.path_label)
        train = self.path_label[0:int(0.8*n)]
        xtrain = [p for p,l in train]
        ytrain = [l for p,l in train]

        test = self.path_label[int(0.8*n):]
        xtest = [p for p,l in test]
        ytest = [l for p,l in test]

        return xtrain, ytrain, xtest, ytest





