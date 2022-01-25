import matplotlib.pyplot as plt 

class View:
    def __init__(self,data,columns=5,row=5,*size):
        x,y = plt.subplots(columns,row,figsize=size[0])
        for i,aix in enumerate(y.flat):
            aix.imshow(data[i].reshape(11,11),cmap='bone')     
            aix.set(xticks=[],yticks=[])
        plt.show()