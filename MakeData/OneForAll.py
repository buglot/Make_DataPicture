from MakeData.DataPic import DataPic as D
from sklearn.model_selection import train_test_split as ttr
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,accuracy_score,confusion_matrix
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import cv2

class OneForAll:
    def __init__(self,path,imsize=(50,50),s2D=0,choice=0,Train_size=75,Test_size=25):
        self.__oneforall=D(path)
        self.__trainsize=float("0."+str(Train_size))
        self.__testsize=float("0."+str(Test_size))  
        self.__oneforall.Set_im_size(imsize[0],imsize[1])
        self.__oneforall.AnswerData(choice=choice)
        self.__oneforall.to_Answer()
        self.__oneforall.to_Data(s2D=s2D,choice=choice)
        self.__loadData = self.__oneforall.Data()
        self.__loadAns = self.__oneforall.Ans()
        self.Train,self.Test,self.TrainResult,self.TestResult = ttr(self.__loadData,self.__loadAns,
                train_size=self.__trainsize,test_size=self.__testsize)
        self.ModelOneForall=MLPClassifier()
        self.ModelOneForall.fit(self.Train,self.TrainResult)

class ReportTest:
    def __init__(self,Model,Test,TestResult):
        self.__Model=Model.predict(Test)
        self.__Models=Model
        self.__Test=Test
        self.__TestResult=TestResult
    
    def showAccuracy_score(self):
        return accuracy_score(self.__TestResult,self.__Model)*100

    def showPredict(self,Rows=2,Columns=2,im_size=(50,50),size=(10,10)):
        x,y = plt.subplots(Rows,Columns,figsize=size)
        for i,aix in enumerate(y.flat):
            aix.imshow(self.__Test[i].reshape(im_size),cmap='bone')
            aix.set(xticks=[],yticks=[])
            aix.text(0.05,0.87,"Predict : "+str(self.__Models.predict([self.__Test[i]])[0]),transform=aix.transAxes,color='White' if self.__Models.predict([self.__Test[i]])[0]==self.__TestResult[i] else 'red')
            aix.text(0.05,0.05,str(self.__TestResult[i]),transform=aix.transAxes,color='green')
        plt.show()

    def showBlockPredict(self):
        mat=confusion_matrix(self.__TestResult,self.__Model)
        d=[]
        for x in self.__TestResult:
            if x not in d:
                d.append(x)
        d.sort()
        sb.heatmap(mat.T,square=True,annot=True,fmt='d',cbar=False
        ,xticklabels=d
        ,yticklabels=d)
        plt.ylabel('Predict')
        plt.xlabel('Real Data')
        plt.show()

    def __str__(self):
        return classification_report(self.__TestResult,self.__Model)

class Input_OneFile_Test:
    def __init__(self,File,Model,im_size=(50,50),s2D=0):
        self.__file = os.path.join(File)
        self.__Models=Model
        self.__cv=cv2.imread(self.__file,s2D)
        self.__cv=cv2.resize(self.__cv,im_size,interpolation=cv2.INTER_CUBIC)
    def show(self):
        print("Predict: "+str(self.__Models.predict([self.__cv.flatten()])))

    def __str__(self):
        return "Predict: "+str(self.__Models.predict([self.__cv.flatten()]))