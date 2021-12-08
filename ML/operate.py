import math
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.feature_selection import f_regression
import matplotlib.pyplot as plt
import seaborn as sns


class file:
    def __init__(self, filename):
        self.DATA = pd.read_csv('{}'.format(filename))
        self.devIdx = []
        self.pearIdx = []

    def ReadFile(self):
        '''
        Read the csv file
        :return: pandas.DataFrame
        '''
        return self.DATA

    def stdev(self):
        '''
        This function is for standard deviation, and this function will drop the outlier data.
        :return: df
        '''
        arr = np.array(self.DATA.iloc[:, -1].values)  # get the last data
        dev = 3 * np.std(arr, ddof=1)  # sample deviation
        arr_ = list(arr)
        # print('last arr: ', arr, '\ndev: ', dev)
        for i in range(len(arr_)):
            if arr[i] > dev:  # get index of bigger than deviation
                self.devIdx.append(i)

        self.DATA = self.DATA.drop(self.DATA.index[self.devIdx])

        # print(len(self.devIdx))
        return self.DATA

    def Pca(self, df, n_comp):
        '''
        This function is for PCA, but I'm not sure is it correct.

        :param df: type is pandas.DataFrame
        :param n_comp: How many dimension want to reduce
        :return: After reduce dimension df
        '''
        pca = PCA(n_components=n_comp)
        pca.fit(df)
        X_pca = pca.transform(df)
        # print(pca.n_components_)
        # print('original shape', self.DATA.shape)
        # print('transformed shape', X_pca.shape)
        # print(pca.explained_variance_)
        # print(pca.transform(df))
        data = pd.DataFrame(X_pca)
        return data

    def pearson(self, threshold, y):
        '''
        This function is for pearson function, and it will return all the column index lager than threshold.
        If lager than threshold means it more important because pearson more close 0 means no relationship.
        
        :param threshold: The threshold for define which one is more important, and set the integer
        :param y: This is the label column, and set the integer
        :return: return the important column index
        '''
        Coor = self.DATA.corr()  # df.coor() is pearson coefficient
        target_arr = abs(Coor.iloc[y])  # It will become to all the column pearson coefficient
        # i+1 is for making i start from 1, and if larger then threshold will be choose
        self.pearIdx = [int(i + 1) for i in range(len(target_arr)) if target_arr[i] > threshold]
        print('features selects:\n', self.pearIdx, '\nselects length:', len(self.pearIdx))
        return self.pearIdx
