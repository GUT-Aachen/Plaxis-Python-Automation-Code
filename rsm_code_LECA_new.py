#!/usr/bin/env python
# coding: utf-8

# In[8]:


import os
from plxscripting.easy import *
#for python server setup
s_i, g_i = new_server('localhost', 10000, password='KnaT?M=cLV7~S83=')
s_o, g_o = new_server('localhost', 10001, password='KnaT?M=cLV7~S83=')
def runProcess(n,i,j,k,l,m,o):
    int(n)
    float(i)
    float(j)
    float(k)
    float(l)
    float(m)
    float(o)
    s_i.new()
    g_i.gotosoil()
    #setting model conditions
    g_i.SoilContour.initializerectangular(0, 0, 70, 50)
    g_i.setproperties("Title","Automation_Test")
    #for soil layer construction
    borehole_1 = g_i.borehole(0, 0)
    g_i.soillayer(1)
    g_i.soillayer(2)
    g_i.soillayer(3)
    g_i.setsoillayerlevel(borehole_1,1, -1)
    g_i.setsoillayerlevel(borehole_1,2, -i)
    g_i.setsoillayerlevel(borehole_1,3, -30)
    #for soil conditions
    g_i.borehole_1.setproperties("Head ",-30)
    material = g_i.soilmat()
    material.setproperties("MaterialName","1.Layer","Colour",10676870,"SoilModel",1,"gammaUnsat",19.5,"gammaSat",19.5,
    "Gref",j,"nu",0.2,"RayleighAlpha",0.1197,"RayleighBeta",6.973E-3,"Rinter",0.67)
    g_i.Soils[0].Material = material
    material = g_i.soilmat()
    material.setproperties("MaterialName","1.Layer","Colour",10676870,"SoilModel",1,"gammaUnsat",19.5,"gammaSat",19.5,
    "Gref",j,"nu",0.2,"RayleighAlpha",0.1197,"RayleighBeta",6.973E-3,"Rinter",0.67)
    g_i.Soils[1].Material = material
    material = g_i.soilmat()
    material.setproperties("MaterialName","2.Layer","Colour",6606905,"SoilModel",1,"gammaUnsat",20.5,"gammaSat",20.5,
    "Gref",188100,"nu",0.2,"RayleighAlpha",0.1102,"RayleighBeta",6.657E-3,"Rinter",0.67)
    g_i.Soils[2].Material = material
    g_i.soilmat("MaterialName","Pile","Colour",8422021,"SoilModel",1,"DrainageType",4,"gammaUnsat",25,"gammaSat",25,
    "Gref",16000000,"nu",0.25,"Rinter",0.67)
    g_i.soilmat("MaterialName","LECA","Colour",16055291,"SoilModel",1,"gammaUnsat",3,"gammaSat",3,"Gref",969.2,
    "nu",0.3,"Rinter",0.67)
    #setting construction materials
    g_i.platemat("MaterialName","Floors","Colour",16711680,"d",0.1,"w",25,"E1",28000000,"E2",28000000,"Nu12",0.25,"G12",11200000,
    "G13",11200000,"G23",11200000)
    g_i.platemat("MaterialName","Foundation","Colour",15890743,"d",0.3,"w",25,"E1",28000000,"E2",28000000,"Nu12",0.25,"G12",
    11200000,"G13",11200000,"G23",11200000)
    g_i.platemat("MaterialName","Wall","Colour",16668197,"d",0.2,"w",25,"E1",30000000,"E2",30000000,"Nu12",0.25,"G12",12000000,
    "G13",12000000,"G23",12000000)
    g_i.beammat("MaterialName","Beams","Colour",16711935,"BeamType",0,"PredefinedBeamType",3,"Height",0.5,"Width",0.25,"w",25,
    "E",28000000)
    g_i.beammat("MaterialName","FoundationBeams","Colour",15666410,"BeamType",0,"PredefinedBeamType",3,"Height",0.8,"Width",0.65,
    "w",25,"E",28000000)
    g_i.anchormat("MaterialName","Floor_1","Colour",0,"EA",7500000)
    g_i.anchormat("MaterialName","Floor","Colour",0,"EA",9080000)
    #starting with structures
    g_i.gotostructures()
    #ground plate
    g_i.surface(35,17,-3.5,48.5,17,-3.5,48.5,33,-3.5,35,33,-3.5,35,17,-3.5)
    g_i.decomposesrf(g_i.Polygon_1)
    g_i.decomposeoutl(g_i.Polygon_1)
    #walls
    g_i.extrude(g_i.Line_Polygon_1_1,g_i.Line_Polygon_1_2,g_i.Line_Polygon_1_3,g_i.Line_Polygon_1_4,0,0,3.5)
    g_i.plate(g_i.Polygon_1,g_i.Polygon_2,g_i.Polygon_3,g_i.Polygon_4,g_i.Polygon_5)
    #set materials for geometries
    g_i.setmaterial(g_i.Polygon_1.Plate,g_i.Foundation)
    g_i.setmaterial(g_i.Polygon_2.Plate,g_i.Polygon_3.Plate,g_i.Polygon_4.Plate,g_i.Polygon_5.Plate,g_i.Wall)
    g_i.beam(g_i.Line_Polygon_1_1,g_i.Line_Polygon_1_2,g_i.Line_Polygon_1_3,g_i.Line_Polygon_1_4)
    g_i.setmaterial(g_i.Line_Polygon_1_1.Beam,g_i.Line_Polygon_1_2.Beam,g_i.Line_Polygon_1_3.Beam,g_i.Line_Polygon_1_4.Beam,
    g_i.FoundationBeams)
    #construct reinforments
    g_i.arrayr(g_i.Line_Polygon_1_4,5,2.7,0,0)
    g_i.arrayr(g_i.Line_Polygon_1_3,5,0,-3.2,0)
    g_i.n2nanchor(35,17,-3.5,35,17,0)
    g_i.setmaterial(g_i.Line_9.NodeToNodeAnchor,g_i.Floor)
    g_i.arrayr(g_i.Line_9,6,2.7,0,0)
    g_i.arrayr(g_i.Line_9,g_i.Line_10,g_i.Line_11,g_i.Line_12,g_i.Line_13,g_i.Line_14,6,0,3.2,0)
    #building levels
    g_i.arrayr(g_i.Line_Polygon_1_1,g_i.Line_Polygon_1_2,g_i.Line_Polygon_1_3,g_i.Line_1,g_i.Line_2,g_i.Line_Polygon_1_4,g_i.Line_3,g_i.Line_4,
    g_i.Line_5,g_i.Line_6,g_i.Line_7,g_i.Line_8,2,0,0,3.5)
    g_i.setmaterial(g_i.Line_45.Beam,g_i.Line_46.Beam,g_i.Line_47.Beam,g_i.Line_48.Beam,g_i.Line_49.Beam,g_i.Line_50.Beam,
    g_i.Line_51.Beam,g_i.Line_52.Beam,g_i.Line_53.Beam,g_i.Line_54.Beam,g_i.Line_55.Beam,g_i.Line_56.Beam,g_i.Beams_1)
    g_i.arrayr(g_i.Polygon_1,2,0,0,3.5)
    g_i.setmaterial(g_i.Polygon_6.Plate,g_i.Floors)
    g_i.n2nanchor(35,17,0,35,17,3)
    g_i.setmaterial(g_i.Line_57.NodeToNodeAnchor,g_i.Floor_1)
    g_i.arrayr(g_i.Line_57,6,2.7,0,0)
    g_i.arrayr(g_i.Line_57,g_i.Line_58,g_i.Line_59,g_i.Line_60,g_i.Line_61,g_i.Line_62,6,0,3.2,0)
    g_i.arrayr(g_i.Line_45,g_i.Line_46,g_i.Line_47,g_i.Line_48,g_i.Line_49,g_i.Line_50,g_i.Line_51,g_i.Line_52,g_i.Line_53,
    g_i.Line_54,g_i.Line_55,g_i.Line_56,2,0,0,3)
    g_i.arrayr(g_i.Polygon_6,2,0,0,3)
    #array the floor level to build levels
    g_i.arrayr(g_i.Line_57,g_i.Line_58,g_i.Line_59,g_i.Line_60,g_i.Line_61,g_i.Line_62,g_i.Line_63,g_i.Line_64,g_i.Line_65,
    g_i.Line_66,g_i.Line_67,g_i.Line_68,g_i.Line_69,g_i.Line_70,g_i.Line_71,g_i.Line_72,g_i.Line_73,g_i.Line_57,g_i.Line_74,
    g_i.Line_75,g_i.Line_76,g_i.Line_77,g_i.Line_78,g_i.Line_79,g_i.Line_75,g_i.Line_76,g_i.Line_77,g_i.Line_78,g_i.Line_79,
    g_i.Line_80,g_i.Line_81,g_i.Line_82,g_i.Line_83,g_i.Line_84,g_i.Line_85,g_i.Line_86,g_i.Line_87,g_i.Line_88,g_i.Line_89,
    g_i.Line_90,g_i.Line_91,g_i.Line_92,g_i.Line_93,g_i.Line_94,g_i.Line_95,g_i.Line_96,g_i.Line_97,g_i.Line_98,g_i.Line_99,
    g_i.Line_100,g_i.Line_101,g_i.Line_102,g_i.Line_103,g_i.Line_104,g_i.Polygon_7,5,0,0,3)
    #structuring foundation objects
    g_i.group(g_i.NodeToNodeAnchor_1,g_i.NodeToNodeAnchor_2,g_i.NodeToNodeAnchor_3,g_i.NodeToNodeAnchor_4,g_i.NodeToNodeAnchor_5,
    g_i.NodeToNodeAnchor_6,g_i.NodeToNodeAnchor_7,g_i.NodeToNodeAnchor_8,g_i.NodeToNodeAnchor_9,g_i.NodeToNodeAnchor_10,
    g_i.NodeToNodeAnchor_11,g_i.NodeToNodeAnchor_12,g_i.NodeToNodeAnchor_13,g_i.NodeToNodeAnchor_14,g_i.NodeToNodeAnchor_15,
    g_i.NodeToNodeAnchor_16,g_i.NodeToNodeAnchor_17,g_i.NodeToNodeAnchor_18,g_i.NodeToNodeAnchor_19,g_i.NodeToNodeAnchor_20,
    g_i.NodeToNodeAnchor_21,g_i.NodeToNodeAnchor_22,g_i.NodeToNodeAnchor_23,g_i.NodeToNodeAnchor_24,g_i.NodeToNodeAnchor_25,
    g_i.NodeToNodeAnchor_26,g_i.NodeToNodeAnchor_27,g_i.NodeToNodeAnchor_28,g_i.NodeToNodeAnchor_29,g_i.NodeToNodeAnchor_30,
    g_i.NodeToNodeAnchor_31,g_i.NodeToNodeAnchor_32,g_i.NodeToNodeAnchor_33,g_i.NodeToNodeAnchor_34,g_i.NodeToNodeAnchor_35,
    g_i.NodeToNodeAnchor_36)
    g_i.group_1.rename("Foundation_Columns")
    g_i.group(g_i.Plate_2,g_i.Plate_3,g_i.Plate_4,g_i.Plate_5)
    g_i.group_1.rename("Foundation_Walls")
    g_i.group(g_i.Beam_1,g_i.Beam_2,g_i.Beam_3,g_i.Beam_4,g_i.Beam_5,g_i.Beam_6,g_i.Beam_7,g_i.Beam_8,g_i.Beam_9,g_i.Beam_10,
    g_i.Beam_11,g_i.Beam_12)
    g_i.group_1.rename("Foundation_Beams")
    #constructing the pile
    g_i.surface(15.15,24.85,0,15.15,25.15,0,14.85,25.15,0,14.85,24.85,0)
    g_i.extrude(g_i.polygon_12,0,0,-6)
    g_i.decomposesrf(g_i.volume_1)
    g_i.posinterface(g_i.Polygon_Volume_1_2,g_i.Polygon_Volume_1_3,g_i.Polygon_Volume_1_4,g_i.Polygon_Volume_1_5,
    g_i.Polygon_Volume_1_6)
    #constructing the trench
    g_i.surface(15.15+k,25-o,0,15.15+k+l,25-o,0,15.15+k+l,25+o,0,15.15+k,25+o,0,15.15+k,25-o,0)
    g_i.extrude(g_i.polygon_13,0,0,-m)
    g_i.delete(g_i.Polygon_13)
    g_i.decomposesrf(g_i.volume_2)
    g_i.posinterface(g_i.Polygon_Volume_2_2,g_i.Polygon_Volume_2_3,g_i.Polygon_Volume_2_4,g_i.Polygon_Volume_2_5)
    #designing the driving load
    g_i.loadmultiplier()
    g_i.LoadMultiplier_1.setproperties("Amplitude",7459,"Frequency",10)
    g_i.surfload(g_i.Polygon_Volume_1_1)
    g_i.DynSurfaceLoad_1.setproperties("sigz",-1,"Multiplierz",g_i.LoadMultiplier_1)
    #for better mesh quality around the interacting constructions
    g_i.surface(5,5,0,60,5,0,60,45,0,5,45,0,5,5,0)
    g_i.extrude(g_i.Polygon_13,0,0,-m-5)
    g_i.delete(g_i.Polygon_13)
    #meshing
    g_i.gotomesh()
    #refining the pile
    g_i.BoreholeVolume_1_Volume_1_Volume_3_1.setproperties("CoarsenessFactor",0.1)
    g_i.BoreholeVolume_2_Volume_1_Volume_3_1.setproperties("CoarsenessFactor",0.1)
    if (i<=5):
        g_i.BoreholeVolume_3_Volume_1_Volume_3_1.setproperties("CoarsenessFactor",0.1)
    #refining the trench    
    g_i.BoreholeVolume_1_Volume_2_Volume_3_1.setproperties("CoarsenessFactor",0.1)
    g_i.BoreholeVolume_2_Volume_2_Volume_3_1.setproperties("CoarsenessFactor",0.1)
    #refining the soil
    g_i.BoreholeVolume_1_Volume_3_1.setproperties("CoarsenessFactor",0.25)
    g_i.BoreholeVolume_2_Volume_3_2.setproperties("CoarsenessFactor",0.25)
    if (m+5>i):
        g_i.BoreholeVolume_3_Volume_3_1.setproperties("CoarsenessFactor",0.25)
    #condtional refinements depending on soil and trench depths
    if (m>i):
        g_i.BoreholeVolume_3_Volume_2_Volume_3_1.setproperties("CoarsenessFactor",0.1)
        g_i.refine(g_i.Polygon_Volume_2_2_3,g_i.Polygon_Volume_2_3_3,g_i.Polygon_Volume_2_4_3,g_i.Polygon_Volume_2_5_3)
    #refining the structure
    g_i.refine(g_i.Polygon_1_Polygon_Polygon_1_1_1,g_i.Polygon_2_1,g_i.Polygon_2_2,g_i.Polygon_3_1,g_i.Polygon_3_2,g_i.Polygon_4_1,g_i.Polygon_4_2,g_i.Polygon_5_1,g_i.Polygon_5_2,g_i.Polygon_4_1,g_i.Polygon_5_1,g_i.Polygon_6_1,
    g_i.Polygon_7_1,g_i.Polygon_8_1,g_i.Polygon_9_1,g_i.Polygon_10_1,g_i.Polygon_11_1)
    g_i.refine(g_i.Polygon_1_Polygon_Polygon_1_1_1,g_i.Polygon_2_1,g_i.Polygon_2_2,g_i.Polygon_3_1,g_i.Polygon_3_2,g_i.Polygon_4_1,g_i.Polygon_4_2,g_i.Polygon_5_1,g_i.Polygon_5_2,g_i.Polygon_4_1,g_i.Polygon_5_1,g_i.Polygon_6_1,
    g_i.Polygon_7_1,g_i.Polygon_8_1,g_i.Polygon_9_1,g_i.Polygon_10_1,g_i.Polygon_11_1)
    g_i.mesh(0.05)
    #designing stages
    g_i.gotostages()
    #1.Phase: Foundation Excavation
    g_i.phase(g_i.InitialPhase)
    g_i.Phase_1.setproperties("Identification","Foundation_Excavation")
    g_i.deactivate(g_i.BoreholeVolume_1_Volume_3_2,g_i.Phase_1)
    if (i<=3):
        g_i.deactivate(g_i.BoreholeVolume_3_Volume_3_1,g_i.Phase_1)
    if (i>3):
        g_i.deactivate(g_i.BoreholeVolume_2_Volume_3_1,g_i.Phase_1)
    #2.Phase: Foundation construction
    g_i.phase(g_i.Phase_1)
    g_i.Phase_2.setproperties("Identification","Foundation_Construction")
    g_i.Phase_2.setproperties("ResetDisplacementsToZero",True)
    g_i.activate(g_i.Plate_1,g_i.Foundation_Walls,g_i.Foundation_Beams,g_i.Foundation_Columns,g_i.Plate_6,g_i.Phase_2)
    #3.Phase: Building the floors
    g_i.phase(g_i.Phase_2)
    g_i.Phase_3.setproperties("Identification","Floor_Construction")
    g_i.Phase_3.setproperties("ResetDisplacementsToZero",True)
    g_i.activate(g_i.NodeToNodeAnchors,g_i.Beams,g_i.Points,g_i.Plates,g_i.Phase_3)
    #4.Phase: Trench Excavation
    g_i.phase(g_i.Phase_3)
    g_i.Phase_4.setproperties("Identification","Trench_Excavation")
    g_i.Phase_4.setproperties("ResetDisplacementsToZero",True)
    if (m>i):
        g_i.deactivate(g_i.BoreholeVolume_3_Volume_2_Volume_3_1,g_i.Phase_4)
    g_i.deactivate(g_i.BoreholeVolume_1_Volume_2_Volume_3_1,g_i.BoreholeVolume_2_Volume_2_Volume_3_1,g_i.Phase_4)
    #5.Phase: Geofoam installation
    g_i.phase(g_i.Phase_4)
    g_i.Phase_5.setproperties("Identification","LECA Installation")
    g_i.Phase_5.setproperties("ResetDisplacementsToZero",True)
    g_i.Soil_1_Soil_5_Soil_6_1.setmaterial(g_i.Phase_5,g_i.LECA)
    g_i.Soil_2_Soil_5_Soil_6_1.setmaterial(g_i.Phase_5,g_i.LECA)
    if (m>i):
        g_i.Soil_3_Soil_5_Soil_6_1.setmaterial(g_i.Phase_5,g_i.LECA)
        g_i.activate(g_i.BoreholeVolume_3_Volume_2_Volume_3_1,g_i.Phase_5)
    g_i.activate(g_i.BoreholeVolume_1_Volume_2_Volume_3_1,g_i.BoreholeVolume_2_Volume_2_Volume_3_1,g_i.Phase_5)
    #6.Phase: Presetting the pile
    g_i.phase(g_i.Phase_5)
    g_i.Phase_6.setproperties("Identification","Presetting the pile")
    g_i.Phase_6.setproperties("ResetDisplacementsToZero",True)
    g_i.Soil_1_Soil_4_Soil_6_1.setmaterial(g_i.Phase_6,g_i.Pile)
    g_i.Soil_2_Soil_4_Soil_6_1.setmaterial(g_i.Phase_6,g_i.Pile)
    if (i<=5):
        g_i.Soil_3_Soil_4_Soil_6_1.setmaterial(g_i.Phase_6,g_i.Pile)
    g_i.activate(g_i.Interfaces,g_i.Phase_6)
    #7.Phase: Pile driving
    g_i.phase(g_i.Phase_6)
    g_i.Phase_7.setproperties("Identification","Pile driving","DeformCalcType","dynamic")
    g_i.Phase_7.setproperties("TimeIntervalSeconds",0.5)
    g_i.Phase_7.setproperties("ResetDisplacementsToZero",False)
    g_i.Phase_7.setproperties("UseDefaultIterationParams",False)
    g_i.Phase_7.setproperties("TimeStepDetermType","manual")
    g_i.Phase_7.setproperties("MaxSteps",100)
    g_i.activate(g_i.SurfaceLoads,g_i.Phase_7)
    g_i.activate(g_i.DynSurfaceLoad_1_1,g_i.Phase_7)
    g_i.Dynamics.setproperties("BoundaryXmin",g_i.Phase_7,"viscous","BoundaryYmin",g_i.Phase_7,"viscous",
    "BoundaryZmin",g_i.Phase_7,"viscous","BoundaryXmax",g_i.Phase_7,"viscous","BoundaryYmax",g_i.Phase_7,"viscous",
    "BoundaryZmax",g_i.Phase_7,"none")
    #Select mesh points prior to caculation
    g_i.selectmeshpoints()
    g_o.addcurvepoint("node",35,25,-0.5)
    g_o.addcurvepoint("node",35,23.4,3)
    g_o.addcurvepoint("node",36.35,26.6,3)
    g_o.update()
    #Start of calculation
    g_i.calculate()
    #Saving the calculation
    n=str(n)
    name=r'\\MASTER01\d\Benutzer\Martin\example'+n
    g_i.save(name)
    #automating the output data generation
    s_o.open(name)
    def gettable_data(filename=None, phaseorder=None):
        # init data for lists
        stepids = []
        vzAs = []
        uxBs = []
        uzCs = []
        times = []
        phasenames = []
        #look into all phases, all steps:
        for phase in phaseorder:
            for step in phase.Steps.value:
                phasenames.append(phase.Name.value)
                stepids.append(int(step.Name.value.replace("Step_", "")))
                vzAs.append(g_o.getcurveresults(g_o.Nodes[0],step,g_o.ResultTypes.Soil.Vz))
                uxBs.append(g_o.getcurveresults(g_o.Nodes[1],step,g_o.ResultTypes.Soil.Ux))
                uzCs.append(g_o.getcurveresults(g_o.Nodes[2],step,g_o.ResultTypes.Soil.Uz))
                # make sure step info on time is available, then add it:
                timevalue = "-"
                if hasattr(step, 'Reached'):
                    if hasattr(step.Reached, 'Time'):
                        timevalue = step.Reached.Time.value
                times.append(timevalue)
        if filename:
            with open(filename, "w") as file:
                file.writelines(["{}\t{}\t{}\t{}\t{}\t{}\n".format(ph, nr, t, vzA, uxB, uzC)
                                 for ph, nr, t, vzA, uxB, uzC in zip(phasenames,stepids,times,vzAs,uxBs,uzCs)])
    gettable_data(filename= name, phaseorder=[g_o.Phase_7]) 
    s_o.close()
import numpy 
def main():
    i=5
    j=44720
    n=0
    for k in numpy.arange(3,3.1,1.7):
        for l in numpy.arange(0.3,0.31,0.24):
            for m in numpy.arange(2,2.1,1):
                for o in numpy.arange(9,9.1,4.5):
                    n=n+1
                    runProcess(n,i,j,k,l,m,o)
main()


# In[ ]:





# In[ ]:




