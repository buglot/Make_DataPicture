from MakeData.DataPic import DataPic as D
from sklearn.model_selection import train_test_split as ttr
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,accuracy_score,confusion_matrix
import os
import numpy as np
import matplotlib.pyplot as plt

class OneForAll:
    def __init__(self,path,imsize=(50,50),s2D=0,choice=0,Train_size=75,Test_size=25):
        self.__oneforall=D(path)
        self.__trainsize=float("0."+str(Train_size))
        self.__testsize=float("0."+str(Test_size))  
        self.__oneforall.Set_im_size(imsize[0],imsize[1])
        self.__oneforall.AnswerData(choice=choice)
        self.__oneforall.to_Answer()
        self.__oneforall.to_Data(s2D=s2D)
        self.__loadData = self.__oneforall.Data
        self.__loadAns = self.__oneforall.Ans
        self.Train,self.Test,self.TrainResult,self.TestResult = ttr(self.__loadData,self.__loadAns,
                train_size=self.__trainsize,test_size=self.__testsize)
        self.ModeloneForall=MLPClassifier()
        self.ModeloneForall.fit(self.Train,self.TrainResult)

class ReportTest:
    def __init__(self,Model,Test,TestResult):
        self.__Medel=Medel.predict(Test)
        self.__Test=Test
        self.__TestResult=TestResult
    
    def showAccuracy_score(self):
        return accuracy_score(self.__TestResult,self.__Medel)*100
    def showPredict(self,Rows=2,Columns=2,im_size=(50,50),size=(10,10)):
        x,y = plt.subplots(10,5,figsize=(10,10))
        for i,aix in enumerate(y.flat):
            aix.imshow(test[i].reshape(im_size),cmap='bone')
            aix.set(xticks=[],yticks=[])
            aix.set_ylabel(modellearn.predict([test[i]])[0],color='White' if modellearn.predict([test[i]])[0]==result[i] else 'red')
            aix.text(0.05,0.05,str(result[i]),transform=aix.transAxes,color='green')
        plt.show()

    def __str__(self):
        return classification_report(self.__TestResult,self.__Medel)