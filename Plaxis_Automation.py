import math
import numpy
import statistics
from plxscripting.easy import *
import TwoLayer_crossing
import TwoLayer

input_port_i = '10000'
input_port_o = '10001'
input_password = 'gkiePHMehran7075'# PUT YOUR PLAXIS 3D INPUT PASSWORD HERE
save_path = 'C:\Program Files (x86)\Plaxis\PLAXIS 3D' # r'C:\Plaxis\Data' # PUT THE FOLDER TO SAVE THE PLAXIS FILES HERE
s_i, g_i = new_server('localhost', 10000, password='gkiePHMehran7075')

f1 = open("points.txt", "r")
if f1.mode == "r":
    xloc = list(map(float, f1.read().split()))
else:
    print("can't read 'points.txt' file")
f1.close()

f2 = open("VelocityY.txt", "r")
if f2.mode == "r":
    Vy = list(map(float, f2.read().split()))
else:
    print("can't read 'Velocity.txt' file")
f2.close()


#VAR Name : X, Width, Depth, first layer depth (line_9), Gref (Line 21), Geofoam (Line 41)


def Calculator(Vector, s_i, g_i,xloc, Vy):
    #Vector=[x, d, l, w, gr, Ep]
    D = Vector[1]
    L = Vector[2]
    if D>L:
        Out = TwoLayer_crossing.Calculation(Vector, s_i, g_i, xloc, Vy)
    else:
        Out = TwoLayer.Calculation(Vector, s_i, g_i, xloc, Vy)
    return Out

X = [1.4, 4.2, 7.6, 10.5, 13.8]
D = [2.6, 3.5, 4.7, 5.3, 6.8, 7.5]
L = [1.5, 3.3, 5.2, 8.7]
W = [0.2]
Gref = [105756]
Eps = [12]
List =[]
Iter = 1
f=open('Efficiency_In_Process.csv', 'wb')
for x in (X):
    for d in (D):
        for l in (L):
            for w in (W):
                for gr in (Gref):
                   for Ep in range(0, len(Eps)):
                       Vector = [x, d, l, w, gr, Ep+1]
                       Out = Calculator(Vector, s_i, g_i, xloc, Vy)
                      # Out=x+d+l+w+gr+Ep
                       Vector1 = [[x, d, l, w, gr, Eps[Ep], Out]]
                       Vector = [x, d, l, w, gr, Eps[Ep], Out]
                       List.append(Vector)
                       a = numpy.asarray(Vector1)
                       print(a)
                       print(Vector1)
                       numpy.savetxt(f, a, fmt='%1.6e', delimiter=",")
                       Iter = Iter + 1
                       print(Iter)
                    
a = numpy.asarray(List)
print("best value obtained with X = {0:3.2f}, W = {1:3.2f}, D = {2:3.2f}, L = {3:3.2f}, Gref = {4:3.2f} and , Geofoam.".format(
        x, d, l, w, gr,
),  Eps[Ep])
numpy.savetxt("Efficiency2.csv", a, fmt='%1.6e', delimiter=",")
