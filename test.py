from MakeData.DataPic import DataPic as D
from MakeData.OneForAll import OneForAll
import numpy as np
import os
a=D('pic')
a.Set_im_size(11,11)
a.to_Answer()
a.SetlocalSaveData('1')
a.to_Data(s2D=0)
saved = np.load(os.path.join('1.npy'))

print(a.returnData(Data=a.Data,Show=5,im_size=(11,11)).show())
a.Show_data(a.Data,2,2,im_size=(11,11))

# Me =OneForAll("pic",(28,28))
