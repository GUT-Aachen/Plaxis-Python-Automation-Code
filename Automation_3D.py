import math
import numpy
import statistics
from plxscripting.easy import *

input_port_i = '10000'
input_port_o = '10001'
input_password = 'gkiePHMehran7075'# PUT YOUR PLAXIS 3D INPUT PASSWORD HERE
save_path = 'C:\Program Files (x86)\Plaxis\PLAXIS 3D' # r'C:\Plaxis\Data' # PUT THE FOLDER TO SAVE THE PLAXIS FILES HERE
s_i, g_i = new_server('localhost', 10000, password='gkiePHMehran7075')


def Calculator(wx, width, depth, length, Dist, s_i, g_i, type):
    s_i.new()
    material1 = g_i.soilmat()
    material1.setproperties(
        "MaterialName", "Soil",
        "Colour", 15262369,
        "SoilModel", 1,
        "gammaUnsat", 20,
        "gammaSat", 20,
        "Gref", 96150,
        "nu", 0.3,
        "cref", 0,
        "phi", 0,
        "RayleighBeta", 0.0003183)
    material2 = g_i.soilmat()
    material2.setproperties(
    "MaterialName", "Geofoam",
        "Colour", 9079434,
        "SoilModel", 1,
        "gammaUnsat", 0.61,
        "gammaSat", 0.61,
        "Gref", 6807,
        "nu", 0.01,
        "cref", 0,
        "phi", 0)
    g_i.Soilcontour.initializerectangular(0,0,40,20)
    borehole = g_i.borehole(0, 0)
    g_i.soillayer(20)
    g_i.setmaterial(g_i.Soil_1, material1)
    g_i.gotostructures()
    g_i.plate((0, 0, 0), (0.36, 0, 0), (0.36, 0.36, 0), (0, 0.36, 0))
    material3 = g_i.platemat()
    material3.setproperties(
        "MaterialName", "Plate",
        "Colour", 16711680,
        "IsIsotropic", True,
        "E1", 30000000,
        "E2", 30000000,
        "d", 0.1,
        "G12", 15000000,
        "G13", 15000000,
        "G23", 15000000)
    g_i.setmaterial(g_i.plate_1, material3)

    ''' g_i.surface(10, 0, 0, 10.5, 0, 0, 10.5, 10, 0, 10, 10, 0, 10, 0, 0)
        g_i.extrude((g_i.Polygon_2), 0, 0, -3)
        g_i.delete(g_i.Polygon_2)
        g_i.setmaterial(g_i.Soil_2, material2)'''


    if (type == 1): #(Function for single wall system)
        g_i.surface(wx-width/2, 0, 0, wx+width/2, 0, 0, wx+width/2, length, 0, wx-width/2, length, 0, wx-width/2, 0, 0)
        g_i.extrude((g_i.Polygon_2), 0, 0, 0-depth)
        g_i.delete(g_i.Polygon_2)
        g_i.setmaterial(g_i.Soil_2, material2)
    elif (type == 2): # (Function for Double Wall system)
        g_i.surface(wx-Dist-width/2, 0, 0, wx-Dist+width/2, 0, 0, wx-Dist+width/2, length, 0, wx-Dist-width/2, length, 0, wx-Dist-width/2, 0, 0)
        g_i.extrude((g_i.Polygon_2), 0, 0, 0-depth)
        g_i.delete(g_i.Polygon_2)
        g_i.setmaterial(g_i.Soil_2, material2)

        g_i.surface(wx+Dist-width/2, 0, 0, wx+Dist+width/2, 0, 0, wx+Dist+width/2, length, 0, wx+Dist-width/2, length, 0, wx+Dist-width/2, 0, 0)
        g_i.extrude((g_i.Polygon_2), 0, 0, 0-depth)
        g_i.delete(g_i.Polygon_2)
        g_i.setmaterial(g_i.Soil_3, material2)
    elif (type == 3):# (Function for Triangle wall System)
        g_i.surface(wx-width, 0, 0, wx+width, 0, 0, wx, 0, 0-depth)
        g_i.delete(g_i.Polygon_2)
        g_i.setmaterial(g_i.Soil_2, material2)

    g_i.surfload(0, 0, 0, 0.36, 0, 0, 0.36, 0.36, 0, 0, 0.36, 0)
    g_i.surface(0, 0, 0, 35, 0, 0, 35, 20, 0, 0, 20, 0, 0, 0, 0)
    g_i.surface(0, 0, 0, 35, 0, 0, 35, 0, -15, 0, 0, -15, 0, 0, 0)
    
    g_i.gotomesh()

    g_i.Polygon_1_Polygon_2_Polygon_3_1.CoarsenessFactor = 0.1
    g_i.Polygon_3_1.CoarsenessFactor = 0.15
    g_i.Polygon_3_2.CoarsenessFactor = 0.2
    g_i.Polygon_4_1.CoarsenessFactor = 0.15
    g_i.Polygon_4_2.CoarsenessFactor = 0.3
    g_i.BoreholeVolume_1_1.CoarsenessFactor = 0.7

    g_i.mesh(3.15, 256)
    g_i.gotostages()

    phase1 = g_i.phase(g_i.phases[0])
    g_i.Polygon_1_Polygon_2_Polygon_3_1.activate(g_i.phase_1)

    phase2 = g_i.phase(g_i.phases[1])
    g_i.BoreholeVolume_1_Volume_1_1.deactivate(g_i.phase_2)

    phase3 = g_i.phase(g_i.phases[2])
    g_i.Soil_1_Soil_2_1.Material[g_i.Phase_3] = material2

    phase4 = g_i.phase(g_i.phases[3])
    g_i.Volume_1.activate(g_i.phase_4)

    phase5 = g_i.phase(g_i.phases[4])
    g_i.set(g_i.phase_5.DeformCalcType,"Dynamic")
    g_i.set(g_i.Phase_5.Deform.TimeIntervalSeconds, 0.0005)
    g_i.set(g_i.Phase_5.Deform.ResetDisplacementsToZero, True)
    g_i.DynSurfaceLoad_1_1.activate(g_i.phase_5)
    g_i.set(g_i.phase_5.DeformCalcType,"Dynamic")
    g_i.DynSurfaceLoad_1_1.sigz[g_i.Phase_5] = -26
    g_i.loadmultiplier()
    g_i.set(g_i.LoadMultiplier_1.Signal, "Harmonic")
    g_i.set(g_i.LoadMultiplier_1.Amplitude, 1)
    g_i.set(g_i.LoadMultiplier_1.Frequency, 50)
    g_i.DynSurfaceLoad_1_1.Multiplierz[g_i.Phase_5] = g_i.LoadMultiplier_1
    g_i.Dynamics.BoundaryXMin[g_i.Phase_5] = "None"
    g_i.Dynamics.BoundaryYMin[g_i.Phase_5] = "None"
    g_i.Dynamics.BoundaryZMin[g_i.Phase_5] = "Viscous"

    phase6 = g_i.phase(g_i.phases[5])
    g_i.set(g_i.phase_6.DeformCalcType,"Dynamic")
    g_i.set(g_i.Phase_6.Deform.TimeIntervalSeconds, 0.005)
    g_i.DynSurfaceLoad_1_1.activate(g_i.phase_6)
    g_i.set(g_i.LoadMultiplier_1.Signal, "Harmonic")
    g_i.set(g_i.LoadMultiplier_1.Amplitude, 1)
    g_i.set(g_i.LoadMultiplier_1.Frequency, 50)
    g_i.DynSurfaceLoad_1_1.Multiplierz[g_i.Phase_6] = g_i.LoadMultiplier_1
    g_i.Dynamics.BoundaryXMin[g_i.Phase_6] = "None"
    g_i.Dynamics.BoundaryYMin[g_i.Phase_6] = "None"
    g_i.Dynamics.BoundaryZMin[g_i.Phase_6] = "Viscous"

    g_i.calculate()

    outpu_port = g_i.view(phase6)
    s_o, g_o = new_server('localhost', 10001, password='gkiePHMehran7075')

    f1 = open("points.txt", "r")
    if f1.mode == "r":
        xloc = list(map(float, f1.read().split()))
    else:
        print("can't read 'points.txt' file")
    f1.close()

    f2 = open("VelocityZ.txt", "r")
    if f2.mode == "r":
        Vz = list(map(float, f2.read().split()))
    else:
        print("can't read 'Velocity.txt' file")
    f2.close()

    thresh = wx + width / 2
    value = []
    Temp = 0
    Npoints = len(xloc)
    for k in range(0, Npoints):
        if (xloc[k] > thresh) and (xloc[k] < (thresh + 30)):
            vz = abs(float(g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (xloc[k], 0, 0))))
            value.append(vz / Vz[k])
            #if (vy / Vy[k]<8):
            Temp += vz / Vz[k]

    Efficiency = statistics.mean(value)
    g_o.close()
    return Efficiency



#Calculator(wx, width, length, depth, Dist, s_i, g_i, type):

Wx = [3, 6] #Location of the trench
De = [2, 3] #Depth of the trench
Le = [5, 20] #Length of the trench
Wi = [0.3, 0.5] #Width of the trench
Dist= [2, 2.5] #Distance between the wall

List =[]
Iter = 1
type = 1
for i in (Wx):
    for j in (Wi):
        for k in (De):
            for l in (Le):
                if type == 1 :
                    Out = Calculator(i, j, k, l, 1, s_i, g_i, type)
                    List.append([i, j, k, l, Out])
                    continue
                for m in (Dist):
                    Out = Calculator(i, j, k, l, m, s_i, g_i, type)
                    List.append([i, j, k, l, m, Out])


a = numpy.asarray(List)
if type == 1:
    numpy.savetxt("Single_Efficiency.csv", a, delimiter=",")
elif type == 2:
    numpy.savetxt("Two_Wall_Efficiency.csv", a, delimiter=",")
elif type == 3:
    numpy.savetxt("Triangle_Wall_Efficiency.csv", a, delimiter=",")










