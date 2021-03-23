from plxscripting.easy import *
import math

s_i, g_i = new_server('localhost', 10000, password='gkiePHMehran7075')
s_i.new()

g_i.SoilContour.initializerectangular(0, 0, 70, 25)
borehole = g_i.borehole(0)
g_i.soillayer(25)
g_i.setproperties("ModelType", "Axisymmetry")


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
"cref", 0)

g_i.setmaterial(g_i.Soil_1, material1)

g_i.gotostructures()

g_i.plate((0, 0), (0.36, 0))
g_i.lineload((0, 0), (0.36, 0))
g_i.polygon((0, -15), (60, -15), (60, 0), (0, 0))

g_i.polygon((2, 0), (2.5, 0), (2.5, -4), (2, -4))

EA = 1800000
EI = 1350000
nu = 0.01
w = 1

d = math.sqrt(12 * EI / EA)
E = EA / d
G = E / (2 * (1 + nu))

g_i.platemat(('MaterialName', 'wall'), ('Gref', G), \
('d', d), ('nu', nu), ('EA', EA), ('EA2', EA),\
('EI', EI), ('w', w), ('PreventPunching', True))

g_i.Line_1.Plate.setmaterial(g_i.wall)

g_i.gotomesh()

g_i.BoreholePolygon_1_Polygon_1_Polygon_2_1.CoarsenessFactor = 0.1
g_i.BoreholePolygon_1_Polygon_1_1.CoarsenessFactor = 0.3
g_i.BoreholePolygon_1_1.CoarsenessFactor = 0.7
g_i.Line_1_Line_2_1.CoarsenessFactor = 0.075


g_i.mesh(0.1)

g_i.gotostages()
phase1 = g_i.phase(g_i.phases[0])
g_i.set(g_i.InitialPhase.DeformCalcType,"Gravity loading")
g_i.Line_1_Line_2_1.activate(g_i.phase_1)

phase2 = g_i.phase(g_i.phases[1])
g_i.BoreholePolygon_1_Polygon_1_Polygon_2_1.deactivate(g_i.phase_2)


phase3 = g_i.phase(g_i.phases[2])
g_i.Soil_1_Soil_2_Soil_3_1.Material[g_i.Phase_3] = material2

phase4 = g_i.phase(g_i.phases[3])
g_i.BoreholePolygon_1_Polygon_1_Polygon_2_1.activate(g_i.phase_4)

phase5 = g_i.phase(g_i.phases[4])
g_i.set(g_i.phase_5.DeformCalcType,"Dynamic")
g_i.set(g_i.Phase_5.Deform.TimeIntervalSeconds, 0.5)
g_i.set(g_i.Phase_5.Deform.ResetDisplacementsToZero, True)
g_i.DynLineLoad_1_1.activate(g_i.phase_5)
g_i.set(g_i.phase_5.DeformCalcType,"Dynamic")
g_i.DynLineLoad_1_1.qy_start[g_i.Phase_5] = -26
g_i.loadmultiplier()
g_i.set(g_i.LoadMultiplier_1.Signal, "Harmonic")
g_i.set(g_i.LoadMultiplier_1.Amplitude, 1)
g_i.set(g_i.LoadMultiplier_1.Frequency, 50)
g_i.DynLineLoad_1_1.Multipliery[g_i.Phase_5] = g_i.LoadMultiplier_1
g_i.Dynamics.BoundaryXMin[g_i.Phase_5] = "None"
g_i.Dynamics.BoundaryYMin[g_i.Phase_5] = "Viscous"


phase6 = g_i.phase(g_i.phases[5])
g_i.set(g_i.phase_6.DeformCalcType,"Dynamic")
g_i.set(g_i.Phase_6.Deform.TimeIntervalSeconds, 0.5)
g_i.DynLineLoad_1_1.activate(g_i.phase_6)
g_i.set(g_i.LoadMultiplier_1.Signal, "Harmonic")
g_i.set(g_i.LoadMultiplier_1.Amplitude, 1)
g_i.set(g_i.LoadMultiplier_1.Frequency, 50)
g_i.DynLineLoad_1_1.Multipliery[g_i.Phase_6] = g_i.LoadMultiplier_1
g_i.Dynamics.BoundaryXMin[g_i.Phase_5] = "None"
g_i.Dynamics.BoundaryYMin[g_i.Phase_5] = "Viscous"

g_i.calculate()

outpu_port = g_i.view(phase6)

s_o, g_o = new_server('localhost', 10001, password='gkiePHMehran7075')

H = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (12.5, 0))
print(H)
J = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (13, 0))
print(J)
K = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (13.5, 0))
print(K)
L = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (14, 0))
print(L)
M = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (14.5, 0))
print(M)
N = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (15, 0))
print(N)
O = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (15.5, 0))
print(O)
P = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (16, 0))
print(P)
Q = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (16.5, 0))
print(Q)
R = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (17, 0))
print(R)
S = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (17.5, 0))
print(S)
T = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (18, 0))
print(T)
U = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (18.5, 0))
print(U)
V = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (19, 0))
print(V)
W = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (19.5, 0))
print(W)
W1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (20, 0))
print(W1)
##X = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (20.5, 0))
##print(X)
Y = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (21, 0))
print(Y)
Z = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (21.5, 0))
print(Z)
Z1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (22, 0))
print(Z1)
##1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (22.5, 0))
##print(A1)
B1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (23, 0))
print(B1)
C1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (23.5, 0))
print(C1)
C11 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (24, 0))
print(C11)
D1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (24.5, 0))
print(D1)
E1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (25, 0))
print(E1)
F1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (25.5, 0))
print(F1)
G1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (26, 0))
print(G1)
H1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (26.5, 0))
print(H1)
I1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (27, 0))
print(I1)
J1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (27.5, 0))
print(J1)
K1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (28, 0))
print(K1)
L1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (28.5, 0))
print(L1)
M1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (29, 0))
print(M1)
N1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (29.5, 0))
print(N1)
O1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (30, 0))
print(O1)
O2 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (30.5, 0))
print(O2)
O3 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (31, 0))
print(O3)
O4 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (31.5, 0))
print(O4)
O5 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (32, 0))
print(O5)
O6 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (32.5, 0))
print(O6)
O7 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (33, 0))
print(O7)
O8 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (33.5, 0))
print(O8)
O9 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (34, 0))
print(O9)
O10 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (34.5, 0))
print(O10)
O11 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (35, 0))
print(O11)
O23 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (35.5, 0))
print(O23)
O24 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (36, 0))
print(O24)
O15 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (36.5, 0))
print(O15)
O17 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (37, 0))
print(O17)
O16 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (37.5, 0))
print(O16)
O15 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (38, 0))
print(O15)
O14 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (38.5, 0))
print(O14)
O13 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (39, 0))
print(O13)
O12 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (39.5, 0))
print(O12)
O32 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (40, 0))
print(O32)
X = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (40.5, 0))
print(X)
Y = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (41, 0))
print(Y)
Z = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (41.5, 0))
print(Z)
Z1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (42, 0))
print(Z1)
A1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (42.5, 0))
print(A1)
B1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (43, 0))
print(B1)
C1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (43.5, 0))
print(C1)
C11 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (44, 0))
print(C11)
D1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (44.5, 0))
print(D1)
E1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (45, 0))
print(E1)
F1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (45.5, 0))         
print(F1)
G1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (46, 0))
print(G1)
H1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (46.5, 0))
print(H1)
I1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (47, 0))
print(I1)
J1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (47.5, 0))
print(J1)
K1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (48, 0))
print(K1)
L1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (48.5, 0))
print(L1)
M1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (49, 0))
print(M1)
N1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (49.5, 0))
print(N1)
O1 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (50, 0))
print(O1)
O2 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (50.5, 0))
print(O2)
O3 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (51, 0))
print(O3)
O4 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (51.5, 0))
print(O4)
O5 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (52, 0))
print(O5)
O6 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (52.5, 0))
print(O6)
O7 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (53, 0))
print(O7)
O8= g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (53.5, 0))
print(O8)
O9 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (54, 0))
print(O9)
O10 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (54.5, 0))
print(O10)
O11 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (55, 0))
print(O11)
O23 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (55.5, 0))
print(O23)
O24 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (56, 0))
print(O24)
O15 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (56.5, 0))
print(O15)
O17 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (57, 0))
print(O17)
O16 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (57.5, 0))
print(O16)
O15 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (58, 0))
print(O15)
O14 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (58.5, 0))
print(O14)
O13 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (59, 0))
print(O13)
O12 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (59.5, 0))
print(O12)
O32 = g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (60, 0))
print(O32)











