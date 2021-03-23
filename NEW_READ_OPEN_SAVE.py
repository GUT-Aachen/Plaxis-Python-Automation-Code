from plxscripting.easy import *
import math
import numpy



def Calculator (ADR):
    s_i, g_i = new_server('localhost', 10000, password='gkiePHMehran7075')
    # s_i.new()
    s_i.open(ADR)
    #s_o.open(ADR)
    s_o, g_o = new_server('localhost', 10001, password='gkiePHMehran7075')
    s_o.open(ADR)
    outpu_port = g_o.view(phase6)
    
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

    thresh = Wx + Wi / 2
    value = []
    Temp = 0
    Npoints = len(xloc)
    for k in range(0, Npoints):
        if (xloc[k] > thresh) and (xloc[k] < (thresh + 30)):
            vy = abs(float(g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (xloc[k], 0))))
            value.append(vy / Vy[k])
            Temp += vy / Vy[k]

    Efficiency = Temp / k
    #g_o.close()
    return Efficiency


Wx = [3, 6, 9, 12, 15]
De = [2, 3, 4, 5, 6, 7]
Wi = [0.3, 0.5, 0.7, 1, 1.5]

List =[]
Iter = 1
for i in (Wx):
    for j in (Wi):
        for k in (De):
          ADDR = str(r'D:/Benutzer/Naghizadehrokni/Chapter Three, Numerical Study/Parametric Study, Layer 1, 2m/Done/EPS 12, Vs 200/')
          ADDR = ADDR + str(Iter) + ".P2dx"
          print(ADDR)
          Iter = Iter + 1
          Out = Calculator(ADDR)
          Out = i * j * k
          List.append([i, k, j, Out])


a = numpy.asarray(List)
numpy.savetxt("Final_List_of_Efficiency.csv", a, delimiter=",")










