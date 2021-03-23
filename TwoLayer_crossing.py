from plxscripting.easy import *
import math
import statistics

def Calculation(gene, s_i, g_i, xloc, Vy):
    # Read Gene Data
    #gene=[x, d, l, w, gr, Ep]
    X = gene[0] #Location of the trench
    D = gene[1] #Depth of the trench
    L = gene[2] #Thickness of the first layer
    W = gene[3] #Width of the trench
    Gref = gene[4] #Shear modulud of the first layer
    GeoFoam =math.ceil(gene[5])    #Type of geofoam

    # Config the Plaxis
    s_i, g_i = new_server('localhost', 10000, password='gkiePHMehran7075')
    s_i.new()

    g_i.SoilContour.initializerectangular(0, 0, 70, 25)
    borehole = g_i.borehole(0)
    g_i.soillayer(L)
    g_i.soillayer(25)
    g_i.setproperties("ModelType", "Axisymmetry")

    material1 = g_i.soilmat()
    material1.setproperties(
        "MaterialName", "Soil1",
        "Colour", 1887942,
        "SoilModel", 1,
        "gammaUnsat", 20,
        "gammaSat", 20,
        "Gref", Gref,
        "nu", 0.3,
        "cref", 0,
        "phi", 0,
        "RayleighBeta", 0.0003183)

    material2 = g_i.soilmat()
    material2.setproperties(
        "MaterialName", "Soil2",
        "Colour", 15262369,
        "SoilModel", 1,
        "gammaUnsat", 20,
        "gammaSat", 20,
        "Gref", 326198,
        "nu", 0.3,
        "cref", 0,
        "phi", 0,
        "RayleighBeta", 0.0003183)

    if GeoFoam == 1: #
        A = 0.112
        B = 669.6
    elif GeoFoam == 2:
        A = 0.114
        B = 1116
    elif GeoFoam == 3:
        A = 0.184
        B = 1785
    elif GeoFoam == 4:
        A = 0.216
        B = 2232
    elif GeoFoam == 5:
        A = 0.288
        B = 3348
    elif GeoFoam == 6:
        A = 0.384
        B = 4595


    material3 = g_i.soilmat()
    material3.setproperties(
        "MaterialName", "Geofoam",
        "Colour", 9079434,
        "SoilModel", 1,
        "gammaUnsat", A,
        "gammaSat", A,
        "Gref", B,
        "nu", 0.1,
        "cref", 0)

    g_i.setmaterial(g_i.Soil_1, material1)
    g_i.setmaterial(g_i.Soil_2, material2)


    g_i.gotostructures()

    g_i.plate((0, 0), (0.36, 0))
    g_i.lineload((0, 0), (0.36, 0))
    g_i.polygon((0, -15), (60, -15), (60, 0), (0, 0))

    g_i.polygon((X-W/2, 0), (X+W/2, 0), (X+W/2, 0-D), (X-W/2, 0-D))

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

    g_i.BoreholePolygon_1_Polygon_1_Polygon_2_1.CoarsenessFactor.CoarsenessFactor = 0.1
    g_i.BoreholePolygon_2_Polygon_1_Polygon_2_1.CoarsenessFactor = 0.1
    g_i.BoreholePolygon_1_Polygon_1_1.CoarsenessFactor = 0.3
    g_i.BoreholePolygon_2_Polygon_1_1.CoarsenessFactor = 0.3
    g_i.BoreholePolygon_2_1.CoarsenessFactor = 0.7
    g_i.BoreholePolygon_1.CoarsenessFactor = 0.7
    g_i.BoreholePolygon_1_1.CoarsenessFactor = 0.7
    g_i.Line_1_Line_2_1.CoarsenessFactor = 0.075


    g_i.mesh(0.05)

    g_i.gotostages()
    phase1 = g_i.phase(g_i.phases[0])
    g_i.set(g_i.InitialPhase.DeformCalcType,"Gravity loading")
    g_i.Line_1_Line_2_1.activate(g_i.phase_1)

    phase2 = g_i.phase(g_i.phases[1])
    g_i.BoreholePolygon_1_Polygon_1_Polygon_2_1.deactivate(g_i.phase_2)
    g_i.BoreholePolygon_2_Polygon_1_Polygon_2_1.deactivate(g_i.phase_2)

    phase3 = g_i.phase(g_i.phases[2])
    g_i.Soil_1_Soil_3_Soil_4_1.Material[g_i.Phase_3] = material3
    g_i.Soil_2_Soil_3_Soil_4_1.Material[g_i.Phase_3] = material3

    phase4 = g_i.phase(g_i.phases[3])
    g_i.BoreholePolygon_1_Polygon_1_Polygon_2_1.activate(g_i.phase_4)
    g_i.BoreholePolygon_2_Polygon_1_Polygon_2_1.activate(g_i.phase_4)

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
    Npoints = len(xloc)
    thresh = X + W / 2
    value = []
    for k in range(0, Npoints):
        if (xloc[k]>thresh) and (xloc[k]<(thresh+30)):
            vy = abs(float(g_o.getsingleresult(g_o.Phase_6, g_o.ResultTypes.Soil.Vy, (xloc[k], 0))))
            value.append(vy/Vy[k])

    g_o.close()
    Ar = statistics.mean(value)
    return Ar
    





