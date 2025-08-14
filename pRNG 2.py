# Rudimentary pRNG

import matplotlib.pyplot as plt

def Plot(x, y , title='Sample Plot', xlabel='X-axis Label', ylabel='Y-axis Label',file_name='sample_plot.png'):
    plt.scatter(x, y, marker='o', color='b')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)  
    plt.savefig(file_name)
    plt.show()

c=4 #the only parameter
x_i=0.1 #x_0 (seed)
    
L_0=[] #list of 10,000 x_i's (generated numbers)
for i in range(10000): # generating 10000 numbers
    x_i=c*x_i*(1-x_i)
    L_0.append(x_i)
                    
X=L_0[:500] # list of first 500 x_i's
Y=L_0[:2500:5] #list of first 500 x_i+5's 

Plot(X, Y, title='correlation plot for c=4 (1)', xlabel='x_i', ylabel='x_i+5', file_name='correlation_plot.png')
    











