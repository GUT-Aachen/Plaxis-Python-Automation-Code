import math


from plxscripting.easy import *

input_port_i = '10000'
input_port_o = '10001'
input_password = 'gkiePHMehran7075'# PUT YOUR PLAXIS 3D INPUT PASSWORD HERE
save_path = 'C:\Program Files (x86)\Plaxis\PLAXIS 3D' # r'C:\Plaxis\Data' # PUT THE FOLDER TO SAVE THE PLAXIS FILES HERE
s_i, g_i = new_server('localhost', 10001, password='gkiePHMehran7075')
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
borehole = g_i.borehole(0,0)
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

g_i.surface(10, 0, 0, 10.5, 0, 0, 10.5, 10, 0, 10, 10, 0, 10, 0, 0)
g_i.extrude((g_i.Polygon_2), 0, 0, -3)
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

g_i.mesh(0.15, 256)
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
g_i.set(g_i.Phase_5.Deform.TimeIntervalSeconds, 0.5)
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
g_i.set(g_i.Phase_6.Deform.TimeIntervalSeconds, 0.5)
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
	
A= g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (8.5, 0, 0))
print(A)
B = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (9, 0, 0))
print(B)
C = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (9.5, 0, 0))
print(C)
D = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (10, 0, 0))
print(D)
E = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (10.5, 0, 0))
print(E)
F = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (11, 0, 0))
print(F)
G = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (11.5, 0, 0))
print(G)
H11 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (12, 0, 0))
print(H11)
##H = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (12.5, 0, 0))
##print(H)
J = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (13, 0, 0))
print(J)
K = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (13.5, 0, 0))
print(K)
L = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (14, 0, 0))
print(L)
M = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (14.5, 0, 0))
print(M)
N = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (15, 0, 0))
print(N)
O = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (15.5, 0, 0))
print(O)
P = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (16, 0, 0))
print(P)
Q = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (16.5, 0, 0))
print(Q)
R = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (17, 0, 0))
print(R)
S = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (17.5, 0, 0))
print(S)
T = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (18, 0, 0))
print(T)
U = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (18.5, 0, 0))
print(U)
V = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (19, 0, 0))
print(V)
W = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (19.5, 0, 0))
print(W)
W1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (20, 0, 0))
print(W1)
X = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (20.5, 0, 0))
print(X)
Y = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (21, 0, 0))
print(Y)
Z = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (21.5, 0, 0))
print(Z)
Z1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (22, 0, 0))
print(Z1)
A1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (22.5, 0, 0))
print(A1)
B1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (23, 0, 0))
print(B1)
C1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (23.5, 0, 0))
print(C1)
C11 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vz, (24, 0, 0))
print(C11)

   