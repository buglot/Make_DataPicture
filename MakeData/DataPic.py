import os
import numpy as np 
import pandas as pd 
import cv2 
import matplotlib.pyplot as plot 
from MakeData.redata import returnData as reData
from MakeData.ViweData import View
class DataPic:
    
    def __init__(self,path=None,Scanfile=0):
        self.__path=path
        self.__Scanfile=Scanfile
        self.__ans=[]
        if Scanfile==0 and path!=None:self.Scanfiles()
        self.__pathANDfiles=[]
        self.__SIZEs=(2,2) 
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
    def checklol(self):return self.__files == None
    def typedataloc(self):return type(self.__files)
    def SetnameColums(self,*arg):self.__NameColums=arg
    def dirANDfiles(self):
        self.__pathANDfiles=[]
        for x in self.__files:
            self.__pathANDfiles.append(str(self.__path.split('\\')[-1])+'\\'+str(x))
        return self.__pathANDfiles
        
    def SetSize_pic(self,x=100,y=100):
        self.__SIZEs=(x,y)


    def FixLocFiles(self):
        self.__pathANDfiles
        for x in self.__files:
            self.__pathANDfiles.append(str(self.__path)+str(x))
        return self.__pathANDfiles
    def St(self):
        if self.__path.endswith('\\'):
            pass
        else:
            self.__path+='\\'

    def SetlocalSaveData(self,loc='Data1'):self.__localfileSave=loc

    def AnswerData(self,choice=0,fixFile=False):
        if fixFile == False:fixFile=self.__files
        if choice==0:
            for x in fixFile:
                a=x.split('.')[0]
                self.__ans.append(a)
            return self.__ans
            
    def PackData(self,loc=None,s2D=None,Sizeimage=None):
        a=[]
        if loc==None:loc=self.__files
        if Sizeimage ==None:Sizeimage=self.__SIZEs
        if self.typedataloc()==type([]):
            for x in loc:
                print('Load Data Picture: *'+x[-13:])
                self.__DataReadpic=cv2.imread(os.path.join(self.__path,x),s2D)
                self.__DataReadpic=cv2.resize(self.__DataReadpic, Sizeimage)
                a.append([self.__DataReadpic])
                self.b=np.array(a)
                np.save(os.path.join(self.__localfileSave),self.b)

    class returnData(reData):
        def __init__(self,Showall=False):
            super().__init__(self.__localfileSave,Showall)
    
    class Show_data(View):
        def __init__(self,data,columns=5,row=5,*size):
            super().__init__(data,columns,row,*size)
