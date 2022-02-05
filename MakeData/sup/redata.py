import numpy as np
import random as rd
class returnData:
    def __init__(self,Data,Shows,im_size):
        self.__Show=Shows
        self.__D=Data
        self.__realData=[]
        for x in range(self.__D.shape[0]):
            self.__realData.append(self.__D[x].reshape(im_size))
        self.__realData = np.array(self.__realData)
    def RandomsData(self,count=5):
        a=np.random.choice(self.__D.shape[0], count, replace=False)
        return self.__realData[a,:,:]
    def show(self):
        return self.__realData[:self.__Show,:,:]