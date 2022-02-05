import matplotlib.pyplot as plt 

class View:
    def __init__(self,data,columns=5,row=5,im_size=(10,10),size=(5,5)):
        x,y = plt.subplots(columns,row,figsize=size)
        for i,aix in enumerate(y.flat):
            aix.imshow(data[i].reshape(im_size),cmap='bone')     
            aix.set(xticks=[],yticks=[])
        plt.show()