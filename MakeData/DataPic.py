import os
import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plot
from MakeData.sup.redata import returnData as reData
from MakeData.sup.ViweData import View


class DataPic:
    def __init__(self, path=None, Scanfile=0):
        self.__path = path
        self.__Scanfile = Scanfile
        self.__ans = []
        self.__files = []
        if Scanfile == 0 and path != None:
            self.Scanfiles()
        self.__pathANDfiles = []
        self.__SIZEs = (50, 50)
        self.__localfileSave = 'Data1'
        self.__Ans = None
        self.__Data = None

    def Scanfiles(self, Path=0):
        if Path == 0:
            Path = self.__path
        for root, dirs, files in os.walk(Path, topdown=False):
            self.__files.append(files)
            self.__dirs = dirs
            self.__root = root

    def setpath(self, Path): self.__path = Path
    def getfile(self): return pd.DataFrame(self.__files, columns=['Files'])
    def getdirs(self): return pd.DataFrame(self.__dirs, columns=['Directory'])
    def getroot(self): return pd.DataFrame(
        [self.__root], columns=['Directory'])

    def typedataloc(self): return type(self.__files)
    def SetnameColums(self, *arg): self.__NameColums = arg
    def SetlocalSaveData(self, loc='Data1'): self.__localfileSave = loc
    def getAnswer(self): return self.__ans
    def getLOCans(self): return self.__LOCans
    def getLOCsaveData(self): return self.__localfileSave

    def dirANDfiles(self):
        self.__pathANDfiles = []
        for x in self.__files:
            self.__pathANDfiles.append(
                str(self.__path.split('\\')[-1])+'\\'+str(x))
        return self.__pathANDfiles

    def Set_im_size(self, x=50, y=50):
        self.__SIZEs = (x, y)

    def get_im_size(self):
        return self.__SIZEs

    def FixLocFiles(self):
        self.__pathANDfiles
        for x in self.__files:
            self.__pathANDfiles.append(str(self.__path)+str(x))
        return self.__pathANDfiles

    def AnswerData(self, choice=0, fixFile=False):
        if fixFile == False:
            fixFile = self.__files
        if choice == 0:
            for x in fixFile[0]:
                a = x.split('.')[0]
                self.__ans.append(a)
        if choice == 1:
            count = 0
            for x in self.__dirs:
                for i in fixFile[count]:
                    self.__ans.append(x)
                count += 1

    def to_Answer(self, LOC="Ans"):
        self.__LOCans = LOC
        self.__Ans = np.array(self.__ans)
        np.save(os.path.join(LOC), self.__Ans)

    def to_Data(self, loc=None, s2D=None, Sizeimage=None, show=False, choice=0):
        a = []
        if loc == None:
            loc = self.__files
        if Sizeimage == None:
            Sizeimage = self.__SIZEs
        if choice == 0:
            if self.typedataloc() == type([]):
                for x in loc[0]:
                    if show != False:
                        print('Load Data Picture: *'+x[-13:])
                    self.__DataReadpic = cv2.imread(
                        os.path.join(self.__path, x), s2D)
                    self.__DataReadpic = cv2.resize(
                        self.__DataReadpic, Sizeimage)
                    a.append(self.__DataReadpic.flatten())
        if choice == 1:
            count = 0
            for x in self.__dirs:
                for i in loc[count]:
                    o = os.path.join(self.__root, x, i)
                    if show != False:
                        print('Load Data Picture: *'+o[-13:])
                    self.__DataReadpic = cv2.imread(o, s2D)
                    self.__DataReadpic = cv2.resize(
                        self.__DataReadpic, Sizeimage)
                    a.append(self.__DataReadpic.flatten())
                count += 1
        self.__Data = np.array(a)
        np.save(os.path.join(self.__localfileSave), self.__Data)

    def Data(self): return self.__Data
    def Ans(self): return self.__Ans

    class returnData(reData):
        def __init__(self, Data=None, Show=5, im_size=(50, 50)):
            super().__init__(Data, Show, im_size)

    class Show_data(View):
        def __init__(self, Data, Columns=5, Rows=5, im_size=(50, 50), size=(5, 5)):
            super().__init__(Data, Columns, Rows, im_size, size)

class load:
    def __new__(self,path,allow_pickle=True):
        return np.load(os.path.join(path),allow_pickle=allow_pickle)
        