from MakeData.DataPic import DataPic as D
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import os
a=D('pic')
a.SetSize_pic(11,11)
print(a.AnswerData())
a.SetlocalSaveData('1')
a.PackData(s2D=0)
saved = np.load(os.path.join('1.npy'))
a.Show_data(a.b,5,5,(4,4))
