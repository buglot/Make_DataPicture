from MakeData.DataPic import DataPic as D
from MakeData.DataPic import load as loads
from MakeData.OneForAll import OneForAll, ReportTest, Input_OneFile_Test
import numpy as np
import os
a=D('pic')
a.Set_im_size(11,11)
a.AnswerData(0)
a.to_Answer()
a.SetlocalSaveData('1')
print(a.Ans())
a.to_Data(s2D=0,choice=0)

# print(a.returnData(Data=a.Data(),Show=5,im_size=(11,11)).show())
# a.Show_data(a.Data(),2,2,im_size=(11,11))
# Me = OneForAll("waler", (28, 28), Test_size=60, Train_size=40, choice=1)
# report = ReportTest(Me.ModelOneForall, Me.Test, Me.TestResult)
# input_1 = Input_OneFile_Test("2.2.png", Me.ModelOneForall, im_size=(28, 28))
# print(input_1)

# a = loads("Data1.npy")
# print(a)
