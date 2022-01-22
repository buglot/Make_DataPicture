import os
import numpy as np 
import pandas as pd 
import cv2 
import matplotlib.pyplot as plot 

class Data_pic:
    
    def __init__(self,path=None,Scanfile=0):
        self.__path=path
        self.__Scanfile=Scanfile
        self.__pathANDfiles=[]
    
    def Scanfiles(self,Path=0):
        if Path ==0:
            Path = self.__path
        for root,dirs,files in os.walk(Path):
            self.__files=files
            self.__dirs=dirs
            self.__root=root

    def setpath(self,Path):self.__path=Path
    def getfile(self):return pd.DataFrame(self.__files,columns=['Files'])
    def getdirs(self):return pd.DataFrame(self.__dirs,columns=['Directory'])
    def getroot(self):return pd.DataFrame(self.__root,columns=['Root'])
    def returnData(self):pass
    def Size_pic(x=100,y=100):return x,y
    def chacklol(self):return self.__files == None
    def typedataloc(self):return type(self.__files)

    
    def FixLocFiles(self):
        for x in self.__files:
            self.__pathANDfiles.append(str(self.__path)+str(x))
        return self.__pathANDfiles
    def St(self):
        if self.__path.endswith('\\'):
            return self.__path
        else:
            self.__path+='\\'
            return self.__path
    
    def readPic(self,loc=None,s2D=None,Sizeimage=None):
        if loc==None:loc=self.__files
        if Sizeimage ==None:Sizeimage=self.Size_pic
        if typedataloc==type([]):
            for x in loc:
                self.__DataReadpic=cv2.imread(x,s2D)