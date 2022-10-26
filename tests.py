#useful packages
import math
import matplotlib.pyplot as plt
import numpy as np
from copy import copy as copy
from numpy import dot as dot
from numpy import histogram as histogram
from numpy import zeros as zeros
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.special import comb
import numpy as np
from collections import Counter


def digitsfrequencytest(seq):
    count_0 = 0
    count_1 = 0
    for digit in seq:
        if digit == '0':
            count_0 += 1
        else:
            count_1 += 1
    rf_0 = count_0 / len(seq)
    rf_1 = count_1 / len(seq)
    return[rf_0,rf_1]

def digitsfrequencytestVisual(digitsfrequency):
    digits = ["0", "1"]
    plt.figure(2)
    plt.xlabel("digits")
    plt.ylabel("frequency")
    plt.title("relative frequency of digits")
    plt.bar(digits, digitsfrequency, color=['b','r'])
    for i in range(len(digits)):
        plt.text(i, digitsfrequency[i]/2,'{:,.3f}'.format(digitsfrequency[i]), ha = 'center')



    return plt.gcf()

def randomwalktest(seq):

    positions = [0]
    step = 0

    for i in range( len(seq) ):
        if seq[i] == '0':
            step = -1
        else:
            step = 1       
        
        positions.append(positions[i] + step)

    return (positions)

def randwalktestVisual(positions):
    plt.figure(1)
    plt.plot(positions)
    plt.xlabel('distance')
    plt.ylabel('walk')
    plt.title('random walk test')
    plt.axhline(y = 0, color = 'r', linestyle = 'dotted')
    return plt.gcf()

def matrixVisual(random_string):

    size = int(math.sqrt(len(random_string)))
    random_string = random_string[0:size*size]

    x = np.array(list(random_string.replace('0','b').replace('1','r')))
    shape = ( size, size )
    mat  = x.reshape( shape )
    X,Y = np.meshgrid(np.arange(mat.shape[1]), np.arange(mat.shape[0]))
    plt.figure(3)
    plt.scatter(X.flatten(), Y.flatten(), c=mat.flatten())
    plt.title("matrix visualisation")
    return plt.gcf()

def PokerTest(s,m):
    X2theoretical = [3.84,5.99,7.81,9.48,11.07,12.59,14.06]
    k = len(s)//m
    l = list(np.arange(0,k))
    s1 = s
    for i in range(0,k):
        while len(s1) > 0:
            l[i] = s1[:m]
            s1 = s1[m:]
            break
    n = l
    for j,i in enumerate(l):
        try:
            n[j] = Counter(i)['1']
        except:
            n[j] = Counter(i)['0']
        
    n.sort()
    niDict = dict(Counter(n))
    #we create a dummy dictionary with keys 
    k =[i for i in range(0,m+1)]
    dummydict = dict(zip(k,[0]*len(k)))
    def check_existance(i,collection: iter):
        return i in collection
    if dummydict.keys() == niDict.keys():
        print('ok')
    else:
        for i in dummydict.keys():
            if check_existance(i,niDict.keys()) == False:
                niDict[i] = 0
    b = []

    for i in niDict.keys():
    
        numerator = math.pow(niDict[i] - comb(m,i)*len(s)/((2**m)*m),2)
        denominator = comb(m,i)*len(s)/((2**m)*m)
        S = numerator / denominator
        b.append(S)
        
    X2 = sum(b)
    if X2 < X2theoretical[m-1]:
        print('The sequence is random')
    else:
        print('The sequence is not random')
    return X2

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def delete_figure_agg(figure_agg):
    figure_agg.get_tk_widget().forget()
    try:
        draw_figure.canvas_packed.pop(figure_agg.get_tk_widget())
    except Exception as e:
        print(f'Error removing {figure_agg} from list', e)
    plt.close('all')

