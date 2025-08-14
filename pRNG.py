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
    
L_0=[] #list of x_i's (generated numbers)
L_1=[] #list of x_i+5's
for i in range(10000): # generating 10000 numbers
    x_i=c*x_i*(1-x_i)
    L_0.append(x_i)
                    
    if i%5==0:
        L_1.append(L_0[i]) # appending generated numbers with indices that are multiples of 5 

L_01=[]
L_11=[]
for i in range(1000): # making the length of the lists equal by picking the first 1000 numbers 
    L_01.append(L_0[i])
    L_11.append(L_1[i])

    
Plot(L_01, L_11, title='correlation plot for c=4', xlabel='x_i', ylabel='x_i+5', file_name='correlation_plot.png')










