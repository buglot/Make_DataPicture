import os
import numpy as np 
import pandas as pd 
import cv2 
import matplotlib.pyplot as plot 
from MakeData.sup.redata import returnData as reData
from MakeData.sup.ViweData import View
class DataPic:
    def __init__(self,path=None,Scanfile=0):
        self.__path=path
        self.__Scanfile=Scanfile
        self.__ans=[]
        self.Data=0
        if Scanfile==0 and path!=None:self.Scanfiles()
        self.__pathANDfiles=[]
        self.__SIZEs=(100,100) 
        self.__localfileSave='Data1'
    def Scanfiles(self,Path=0):
        if Path ==0:Path = self.__path
        for root,dirs,files in os.walk(Path):
            self.__files=files
            self.__dirs=dirs
            self.__root=root

    def setpath(self,Path):self.__path=Path
    def getfile(self):return pd.DataFrame(self.__files,columns=['Files'])
    def getdirs(self):return pd.DataFrame(self.__dirs,columns=['Directory'])
    def getroot(self):return pd.DataFrame(self.__root,columns=['Root'])
    def typedataloc(self):return type(self.__files)
    def SetnameColums(self,*arg):self.__NameColums=arg
    def SetlocalSaveData(self,loc='Data1'):self.__localfileSave=loc
    def getAnswer(self):return self.__ans
    def getLOCans(self):return self.__LOCans
    def getLOCsaveData(self):return self.__localfileSave
    def dirANDfiles(self):
        self.__pathANDfiles=[]
        for x in self.__files:
            self.__pathANDfiles.append(str(self.__path.split('\\')[-1])+'\\'+str(x))
        return self.__pathANDfiles
        
    def Set_im_size(self,x=50,y=50):
        self.__SIZEs=(x,y)
    def get_im_size(self):
        return self.__SIZEs
    def FixLocFiles(self):
        self.__pathANDfiles
        for x in self.__files:
            self.__pathANDfiles.append(str(self.__path)+str(x))
        return self.__pathANDfiles

    def AnswerData(self,choice=0,fixFile=False):
        if fixFile == False:fixFile=self.__files
        if choice==0:
            for x in fixFile:
                a=x.split('.')[0]
                self.__ans.append(a)
        if choice==1:
            for x in fixFile:
                self.__ans.append(self.__path)

    def to_Answer(self,LOC="Ans"):
        self.__LOCans=LOC
        self.Ans = np.array(self.__ans)
        np.save(os.path.join(LOC),self.Ans)

    def to_Data(self,loc=None,s2D=None,Sizeimage=None,show=False):
        a=[]
        if loc==None:loc=self.__files
        if Sizeimage ==None:Sizeimage=self.__SIZEs
        if self.typedataloc()==type([]):
            for x in loc:
                if show!=False:print('Load Data Picture: *'+x[-13:])
                self.__DataReadpic=cv2.imread(os.path.join(self.__path,x),s2D)
                self.__DataReadpic=cv2.resize(self.__DataReadpic, Sizeimage)
                a.append(self.__DataReadpic.flatten())
                b.append(self.__DataReadpic)
            self.Data=np.array(a)
            np.save(os.path.join(self.__localfileSave),self.Data)

    class returnData(reData):
        def __init__(self,Data=None,Show=5,im_size=(50,50)):
            super().__init__(Data,Show,im_size)
    
    class Show_data(View):
        def __init__(self,Data,Columns=5,Rows=5,im_size=(50,50),size=(5,5)):
            super().__init__(Data,Columns,Rows,im_size,size)
