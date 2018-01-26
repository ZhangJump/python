import matplotlib.pyplot as plt
def draw():
    fig = plt.figure(1)
    fig.clf()
    ax = plt.subplot(111)
    decisionNode = dict(boxstyle="sawtooth",fc="0.8")
    arrow_args = dict(arrowstyle="<-")
    ax.annotate('a decision node',xy=(0.5,0.1),xycoords='axes fraction',xytext=(0.1,0.5),textcoords='axes fraction',va="center",ha="center",bbox=decisionNode,arrowprops=arrow_args)
    plt.show()
    
