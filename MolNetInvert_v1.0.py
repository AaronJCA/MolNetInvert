from tkinter import *
import tkinter as tk
from tkinter import ttk  
from tkinter import filedialog
from tkinter import messagebox
import math
import time
import numpy as np
import copy
import re
from colour import Color
import csv

###################################################################################################################################################

iconData = '''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'''

class summaryOfAttribute:
    def __init__(self, ID, name, sampleCols):
        self.ID = ID
        self.name = name
        self.sampleCols = sampleCols

class usedAttribute:
    def __init__(self, name, totalNodes, currentCount, keyAttribute, attID):
        self.name = name
        self.totalNodes = totalNodes
        self.currentCount = currentCount
        self.keyAttribute = keyAttribute
        self.attID = attID

class summaryOfDataFile:
    def __init__(self, ID, name, attributeClassification, sampleCol):
        self.ID = ID
        self.name = name
        self.attributeClassification = attributeClassification 
        self.sampleCol = sampleCol

class newNode:
    def __init__(self, ID, associatedAttributes, nodesInCluster, nodeColour, clusterID, mzVal, rtVal, peakAreas, areaAttributes, featureName, attributeAreas, OGNodeID, molecularFeatureID, assignedAdduct, sharedName):
        self.ID = ID
        self.associatedAttributes = associatedAttributes
        self.nodesInCluster = nodesInCluster
        self.nodeColour = nodeColour
        self.clusterID = clusterID
        self.mzVal = mzVal
        self.rtVal = rtVal
        self.peakAreas = peakAreas
        self.areaAttributes = areaAttributes
        self.featureName = featureName
        self.attributeAreas = attributeAreas
        self.OGNodeID = OGNodeID
        self.molecularFeatureID = molecularFeatureID
        self.assignedAdduct = assignedAdduct
        self.sharedName = sharedName

class newEdge:
    def __init__(self, ID, targetNode, attributeTarget, sumOfPeakAreas, averageOfPeakAreas):
        self.ID = ID
        self.targetNode = targetNode
        self.attributeTarget = attributeTarget
        self.sumOfPeakAreas = sumOfPeakAreas
        self.averageOfPeakAreas = averageOfPeakAreas

class ionIdentityCluster:
    def __init__(self, ionIdentityID, associatedCluster, nodeCount):
        self.ionIdentityID = ionIdentityID
        self.associatedCluster = associatedCluster
        self.nodeCount = nodeCount

class CreateToolTip(object):

    def __init__(self, widget, text='widget info'):
        self.waittime = 500     #miliseconds
        self.wraplength = 180   #pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.widget.config(bg = "white")
        self.schedule()

    def leave(self, event=None):
        self.widget.config(bg = "SystemButtonFace")
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = tk.Toplevel(self.widget)
        self.tw.configure(bg='#ffffff')
        self.tw.wm_attributes("-transparentcolor", '#ffffff')
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))

        core_Txt = self.text
        boardLine = 1
        msgBG = "#FFFFFE"
        
        label = tk.Label(self.tw, text=core_Txt, justify='left',
                       background=msgBG, relief='solid', borderwidth=boardLine,
                       wraplength = self.wraplength)
        label.grid(row=0, column=1, rowspan=1, columnspan=1, padx = 0, pady = 0, sticky="NW")#.pack(ipady=1)
        
    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()
#
def DefineCoordinates(nodeNumber, totalNodesInAssociation, currentAssociation, possibleAssociations, keyAtt, centerNode):

    spiral = 1
    
    if keyAtt == 1:
        radiusOffSet = 4
    else:
        radiusOffSet = 0
        if spiral != 1:
            nodeNumber = nodeNumber - 1

    xOffSet = 0
    yOffSet = 0

    offSetPossition = currentAssociation
    offsetFraction = 2*3.1415926535897/(possibleAssociations)*currentAssociation

    xOffSet = (possibleAssociations*5)*math.cos(offsetFraction)
    yOffSet = (possibleAssociations*5)*math.sin(offsetFraction)

    if spiral == 0:
        if nodeNumber != 0:
            level = round(math.sqrt(nodeNumber)/2)
            if level < 1:
                level = 1

            i = 1
            levelCount = 0
            nodePos = 0
            while round(math.sqrt(i)/2) <= round(math.sqrt(nodeNumber)/2)+1:
                roundLevel = round(math.sqrt(i)/2)
                if roundLevel < 1:
                    roundLevel = 1

                if roundLevel == level:
                    levelCount = levelCount + 1
                if i == nodeNumber:
                    nodePos = i
                i = i + 1
                
            position = nodePos
            circularFraction = 2*3.1415926535897/(levelCount)*nodePos
    else:
        #orbs = 2
        spaceFactor = 4 #Increase to tighten gaps between nodes (4 looks good)
        circularFraction = (((math.sqrt(nodeNumber)*2)/spaceFactor)-int((math.sqrt(nodeNumber)*2)/spaceFactor)) * 6.283
        radiusFactor = 1.8 #Increase to decrease radius increment per node (1.5-1.8 looks good)
        level = math.sqrt(nodeNumber)/radiusFactor+0.2

    if centerNode == 1 or nodeNumber == 0:
        x = xOffSet
        y = yOffSet
    else:
        x = (radiusOffSet + level) * math.cos(circularFraction) + xOffSet
        y = (radiusOffSet + level) * math.sin(circularFraction) + yOffSet
    
    return x,y

class MainApp(tk.Frame):

    newFileName = ""
    file_path = ""
    file_pathMetaData = ""
    
    dataFiles_Dic = {}
    allAttributes_Dic = {}
    allNodes_Dic = {}
    allEdges_Dic = {}
    allIonIdentities_Dic = {}
    clusterAdjustedEdges = {}
    adductAdjustedEdges = {}
    allAttributesList = []
    nodesToWrite = {}
    edgesToWrite = {}
    possibleAttAss =[]
    attributesToDelete = []
    uniqueAttributes = []
    maxNode = 2
    minEdge = 0
    maxEdge = 0
    uploadType = "GNPS"
    IIMN = 0
    classical = 0

    def dataFromGraphFile(self):

        MainApp.allEdges_Dic = {}
        MainApp.allNodes_Dic = {}
        MainApp.allIonIdentities_Dic = {}
        MainApp.allAttributes_Dic = {}
        MainApp.uniqueAttributes = []
        MainApp.allAttributesList = []
        preferedAttributes = []
        MainApp.IIMN = 0
        MainApp.classical = 0

        if self.networkTypeVal.get() == 3:
            if MainApp.file_pathMetaData == "":
                tk.messagebox.showinfo("No Metadata File Found", "There was no metadata file selected." + "\n" + "\n" + "Processing will continue without a prefered metadata list.")
                preferedAttributes = []
            else:
                with open(MainApp.file_pathMetaData, 'r') as f:
                    metaData_file = f.readlines()

                for i in range(1, len(metaData_file)):
                    if "GNPSGROUP:" in metaData_file[i]:
                        preferedAttributes.append(metaData_file[i].replace('\n',"").replace("_", ""))
                    else:
                        preferedAttributes.append("GNPSGROUP:" + metaData_file[i].replace('\n',"").replace("_", ""))

                if preferedAttributes == []:
                    tk.messagebox.showinfo("No Metadata Info Found", "There was no metadata in the selected file." + "\n" + "\n" + "Processing will continue without a prefered metadata list.")
                    
        if MainApp.file_path == "":
            tk.messagebox.showinfo("No File Found", "There was no file selected." + "\n" + "\n" + "Processing will be stopped.")
            return
        else:
            if MainApp.file_path [-8:] == ".graphml":
                MainApp.newFileName = MainApp.file_path.replace(".graphml", "_Invert.xgmml")
                MainApp.newFileName = MainApp.newFileName[::-1].split("/")[0][::-1]
            
            with open(MainApp.file_path, 'r') as f:
                graph = f.readlines()

            root.title(MainApp.versionName + " - Importing Graph File")
            progress = 0
            
            if self.networkTypeVal.get() == 2:
                attributeNotation = '.+attr.name="G.*[1-7]"'
                MainApp.classical = 1
            else:
                attributeNotation = '.+attr.name="GNPSGROUP:'
                MainApp.classical = 0
                

            nodeCount = 0
            iICount = 0
            attCount = 0
            onEdge = 1
            AttDic = {'CompoundName': "VOID", 'parent mass': "VOID", 'RTMean': "VOID", 'componentindex': "VOID", "Annotated Adduct Features ID": "VOID", "Best Ion": "VOID", "shared name": "VOID"}
                
            for i in range(1, len(graph)):

                attMatch = re.match(attributeNotation, graph[i])
                if attMatch:
                    if preferedAttributes == []:
                        attCount = attCount + 1
                        MainApp.allAttributes_Dic[attCount] = summaryOfAttribute(ID = attCount, name = graph[i].split('<key attr.name="')[1].split('"')[0].replace("_", ""), sampleCols = [])
                        AttDic[graph[i].split('id="')[1].split('"')[0].replace("_", "")] = graph[i].split('<key attr.name="')[1].split('"')[0].replace("_", "")
                    elif graph[i].split('<key attr.name="')[1].split('"')[0].replace("_", "") in preferedAttributes:
                        attCount = attCount + 1
                        MainApp.allAttributes_Dic[attCount] = summaryOfAttribute(ID = attCount, name = graph[i].split('<key attr.name="')[1].split('"')[0].replace("_", ""), sampleCols = [])
                        AttDic[graph[i].split('id="')[1].split('"')[0].replace("_", "")] = graph[i].split('<key attr.name="')[1].split('"')[0].replace("_", "")
                        
                if '<key attr.name="Compound_Name"' in graph[i]:
                    AttDic[graph[i].split('<key attr.name="')[1].split('"')[0].replace("_", "")] = graph[i].split('id="')[1].split('"')[0].replace("_", "")
                if '<key attr.name="RTMean"' in graph[i]:
                    AttDic[graph[i].split('<key attr.name="')[1].split('"')[0]] = graph[i].split('id="')[1].split('"')[0].replace("_", "")
                if '<key attr.name="parent mass"' in graph[i]:
                    AttDic[graph[i].split('<key attr.name="')[1].split('"')[0]] = graph[i].split('id="')[1].split('"')[0].replace("_", "")
                if '<key attr.name="componentindex"' in graph[i]:
                    AttDic[graph[i].split('<key attr.name="')[1].split('"')[0]] = graph[i].split('id="')[1].split('"')[0].replace("_", "")
                if '<key attr.name="Annotated Adduct Features ID"' in graph[i]:
                    AttDic[graph[i].split('<key attr.name="')[1].split('"')[0]] = graph[i].split('id="')[1].split('"')[0].replace("_", "")
                if '<key attr.name="shared name"' in graph[i]:
                    AttDic[graph[i].split('<key attr.name="')[1].split('"')[0]] = graph[i].split('id="')[1].split('"')[0].replace("_", "")
                if '<key attr.name="Best Ion"' in graph[i]:
                    AttDic[graph[i].split('<key attr.name="')[1].split('"')[0]] = graph[i].split('id="')[1].split('"')[0].replace("_", "")
                    MainApp.IIMN = 1
                if "<node id=" in graph[i]:
                    nodeCount = nodeCount + 1
                    MainApp.allNodes_Dic[nodeCount] = newNode(ID = nodeCount, associatedAttributes = [], nodesInCluster = 1, nodeColour = "#FFFFFF", clusterID = 0, \
                                                              mzVal = "", rtVal = "", peakAreas = [], areaAttributes = [], featureName = "-", attributeAreas = [], \
                                                              OGNodeID = graph[i].split('node id="')[1].split('"')[0], molecularFeatureID = "", assignedAdduct = "", \
                                                              sharedName = "")
                    onEdge = 0
                elif "<edge source=" in graph[i] or "<edge id=" in graph[i]:
                    onEdge = 1

                if onEdge == 0:
                    if "<data key=" in graph[i]:
                        if AttDic["parent mass"] == graph[i].split('<data key="')[1].split('"')[0]:
                            if "</data>" in graph[i]:
                                MainApp.allNodes_Dic[nodeCount].mzVal = graph[i].split('<data key="'+ AttDic["parent mass"] + '">')[1].split('</data>')[0]
                        elif AttDic["RTMean"] == graph[i].split('<data key="')[1].split('"')[0]:
                            if "</data>" in graph[i]:
                                MainApp.allNodes_Dic[nodeCount].rtVal = str(round(float(graph[i].split('<data key="'+ AttDic["RTMean"] + '">')[1].split('</data>')[0]),4))
                        elif AttDic["shared name"] == graph[i].split('<data key="')[1].split('"')[0]:
                            if "</data>" in graph[i]:
                                MainApp.allNodes_Dic[nodeCount].sharedName = str(graph[i].split('<data key="'+ AttDic["shared name"] + '">')[1].split('</data>')[0])
                        elif AttDic["componentindex"] == graph[i].split('<data key="')[1].split('"')[0]:
                            if "</data>" in graph[i]:
                                MainApp.allNodes_Dic[nodeCount].clusterID = str(float(graph[i].split('<data key="'+ AttDic["componentindex"] + '">')[1].split('</data>')[0]))
                        elif AttDic["CompoundName"] == graph[i].split('<data key="')[1].split('"')[0].replace("_", ""):
                            if "</data>" in graph[i]:
                                MainApp.allNodes_Dic[nodeCount].featureName = graph[i].replace("_", "").split('<data key="'+ AttDic["CompoundName"] + '">')[1].split('</data>')[0]
                                MainApp.allNodes_Dic[nodeCount].featureName = MainApp.allNodes_Dic[nodeCount].featureName.replace(";", "").replace("!", "").replace('"', "").replace("&", "")
                        elif AttDic["Annotated Adduct Features ID"] == graph[i].split('<data key="')[1].split('"')[0]:
                            if "</data>" in graph[i]:
                                MainApp.allNodes_Dic[nodeCount].molecularFeatureID = graph[i].split('<data key="'+ AttDic["Annotated Adduct Features ID"] + '">')[1].split('</data>')[0].replace(" ", "")
                                if MainApp.allNodes_Dic[nodeCount].molecularFeatureID != "":
                                    if MainApp.allNodes_Dic[nodeCount].molecularFeatureID not in MainApp.allIonIdentities_Dic:
                                        MainApp.allIonIdentities_Dic[MainApp.allNodes_Dic[nodeCount].molecularFeatureID] = ionIdentityCluster(ionIdentityID = MainApp.allNodes_Dic[nodeCount].molecularFeatureID, \
                                                                                                                                              associatedCluster = 0, nodeCount = 1)
                                    else:
                                        MainApp.allIonIdentities_Dic[MainApp.allNodes_Dic[nodeCount].molecularFeatureID].nodeCount = MainApp.allIonIdentities_Dic[MainApp.allNodes_Dic[nodeCount].molecularFeatureID].nodeCount + 1
                                
                        elif AttDic["Best Ion"] == graph[i].split('<data key="')[1].split('"')[0]:
                            if "</data>" in graph[i]:
                                MainApp.allNodes_Dic[nodeCount].assignedAdduct = graph[i].split('<data key="'+ AttDic["Best Ion"] + '">')[1].split('</data>')[0]
                        else:
                            key = graph[i].split('<data key="')[1].split('"')[0]
                            if key in AttDic:
                                MainApp.allNodes_Dic[nodeCount].areaAttributes.append(AttDic[key])
                                MainApp.allNodes_Dic[nodeCount].peakAreas.append(graph[i].split('<data key="' + key + '">')[1].split('</data>')[0])
                                if float(graph[i].split('<data key="' + key + '">')[1].split('</data>')[0]) > 0:
                                    MainApp.allNodes_Dic[nodeCount].associatedAttributes.append(AttDic[key])
                                    MainApp.allNodes_Dic[nodeCount].associatedAttributes.sort()
                                    MainApp.allNodes_Dic[nodeCount].attributeAreas.append("0")
                                        
                                    if AttDic[key] not in MainApp.uniqueAttributes:
                                        MainApp.uniqueAttributes.append(AttDic[key])
                                        MainApp.uniqueAttributes.sort()

                progress = progress + 1
                if i/5000 == int(i/5000):  
                    MainApp.progBar['value'] = ((progress+1)/len(graph))*100
                    MainApp.update_idletasks(self)
                if (progress+1)/len(graph)*100 == 100:
                    MainApp.progBar['value'] = 0

            if len(MainApp.allAttributes_Dic) == 0:
                tk.messagebox.showinfo("No Metadata Found", "There was no metadata found in your selected graph file." + "\n" + \
                                       "Please make sure you have included a metadata table in your GNPS workflow." + "\n" + "\n" + "Processing has be stopped.")
                root.title(MainApp.versionName)
                return

            for nodeID in MainApp.allNodes_Dic:
                j = 0
                for area in MainApp.allNodes_Dic[nodeID].peakAreas:
                    if float(area) > 0:
                        k = 0
                        for att in MainApp.allNodes_Dic[nodeID].associatedAttributes:
                            if att == MainApp.allNodes_Dic[nodeID].areaAttributes[j]:
                                MainApp.allNodes_Dic[nodeID].attributeAreas[k] = area
                            k = k + 1
                    j = j + 1
                if MainApp.allNodes_Dic[nodeID].molecularFeatureID in MainApp.allIonIdentities_Dic:
                    if MainApp.allIonIdentities_Dic[MainApp.allNodes_Dic[nodeID].molecularFeatureID].associatedCluster == 0:
                        MainApp.allIonIdentities_Dic[MainApp.allNodes_Dic[nodeID].molecularFeatureID].associatedCluster = MainApp.allNodes_Dic[nodeID].clusterID
                    elif float(MainApp.allNodes_Dic[nodeID].clusterID) != -1:
                        MainApp.allIonIdentities_Dic[MainApp.allNodes_Dic[nodeID].molecularFeatureID].associatedCluster = MainApp.allNodes_Dic[nodeID].clusterID
            
            i = 1
            for nodeID in MainApp.allNodes_Dic:
                j = 0
                for nodeAss in MainApp.allNodes_Dic[nodeID].associatedAttributes:
                    peakArea = 0
                    avPeakArea = 0
                    for attID in MainApp.allAttributes_Dic:
                        if MainApp.allAttributes_Dic[attID].name == nodeAss:
                            peakArea = MainApp.allNodes_Dic[nodeID].attributeAreas[j]

                    j = j + 1
                    if MainApp.allNodes_Dic[nodeID].areaAttributes.count(nodeAss) != 0:
                        avPeakArea = peakArea #GNPS file only contains averaged intensities/areas
                    else:
                        avPeakArea = 0
                    MainApp.allEdges_Dic[i] = newEdge(ID = i, targetNode = MainApp.allNodes_Dic[nodeID].ID, attributeTarget = nodeAss, sumOfPeakAreas = 0, averageOfPeakAreas = avPeakArea)
                    i = i + 1

            for attID in MainApp.allAttributes_Dic:
                MainApp.allAttributesList.append(MainApp.allAttributes_Dic[attID].name)

            root.title(MainApp.versionName)
    
    def getFeatureTableFile(self):

        MainApp.allEdges_Dic = {}
        MainApp.allNodes_Dic = {}
        MainApp.uniqueAttributes = []
        MainApp.allAttributesList = []
        preferedAttributes = []
        MainApp.IIMN = 0
        MainApp.classical = 1

        massValOffset = 0
        rtValOffset = 0

        if MainApp.file_path == "":
            tk.messagebox.showinfo("No File Selected", "There was feature list file selected." + "\n" + "\n" + "Processing is stopped.")
            return
        elif MainApp.file_pathMetaData == "":
            tk.messagebox.showinfo("No Metadata File Selected", "There was no metadata file selected." + "\n" + "\n" + "Processing is stopped.")
            return
        else:
            if MainApp.file_path [-4:] == ".csv":
                MainApp.newFileName = MainApp.file_path.replace(".csv", "_Invert.xgmml")
                MainApp.newFileName = MainApp.newFileName[::-1].split("/")[0][::-1]
                
            with open(MainApp.file_pathMetaData, 'r') as f:
                metaData_file = f.readlines()

            for i in range(1, len(metaData_file)):
                if len(metaData_file[i].split('\t')) < 2:
                    tk.messagebox.showinfo("Metadata File Error", "Missing metadata for sample." + "\n" + "\n" + "One of more lines in the file is missing a second column for the metadata." + "\n" + "\n" + \
                                           "The file should be a tab separated text file with the first column consisting of the samples names, and the second column consisting of their metadata grouping.")
                    return
                MainApp.dataFiles_Dic[i-1] = summaryOfDataFile(ID = i-1, name = metaData_file[i].split('\t')[0], attributeClassification = metaData_file[i].split('\t')[1], sampleCol = 0)
                attFound = 0
                
                for att in MainApp.allAttributes_Dic:
                    if MainApp.allAttributes_Dic[att].name == metaData_file[i].split('\t')[1]:
                        attFound = 1
                if attFound == 0:
                    MainApp.allAttributes_Dic[len(MainApp.allAttributes_Dic)+1] = summaryOfAttribute(ID = i-1, name = metaData_file[i].split('\t')[1], sampleCols = [])

            with open(MainApp.file_path, newline='') as csvfile:
                featureTable_file = csv.reader(csvfile)

                i = 0
                for row in featureTable_file:
                    if i == 0:
                        j = 0
                        for heading in row:
                            if heading == "row m/z":
                                massValOffset = j
                            if heading == "row retention time":
                                rtValOffset = j
                            for fileID in MainApp.dataFiles_Dic:
                                if " Peak area" in heading:
                                    if MainApp.dataFiles_Dic[fileID].name == heading.split(" Peak area")[0]:
                                        MainApp.dataFiles_Dic[fileID].sampleCol = j
                            j = j + 1                
                            
                    else:
                        MainApp.allNodes_Dic[i] = newNode(ID = i, associatedAttributes = [], nodesInCluster = 1, nodeColour = "#FFFFFF", clusterID = 0, \
                                                          mzVal = round(float(row[massValOffset]),6), rtVal = round(float(row[rtValOffset]),4), peakAreas = [], \
                                                          areaAttributes = [], featureName = row[0], attributeAreas = [], OGNodeID = "", molecularFeatureID = "", assignedAdduct = "", \
                                                          sharedName = row[0])

                        #asigning attribute associations to nodes
                        for fileID in MainApp.dataFiles_Dic:
                            MainApp.allNodes_Dic[i].peakAreas.append(row[MainApp.dataFiles_Dic[fileID].sampleCol])
                            
                            if float(row[MainApp.dataFiles_Dic[fileID].sampleCol]) != 0:
                                MainApp.allNodes_Dic[i].associatedAttributes.append(MainApp.dataFiles_Dic[fileID].attributeClassification)

                            for att in MainApp.allAttributes_Dic:
                                if MainApp.allAttributes_Dic[att].name == MainApp.dataFiles_Dic[fileID].attributeClassification:
                                    MainApp.allNodes_Dic[i].areaAttributes.append(MainApp.allAttributes_Dic[att].name)
                                    
                        MainApp.allNodes_Dic[i].associatedAttributes = sorted(list(set(MainApp.allNodes_Dic[i].associatedAttributes)))
                        
                    i = i + 1

            for nodeID in MainApp.allNodes_Dic:
                for attID in MainApp.allAttributes_Dic:
                    totalPeak = 0
                    i = 0
                    for eachAtt in MainApp.allNodes_Dic[nodeID].areaAttributes:
                        if eachAtt == MainApp.allAttributes_Dic[attID].name:
                            totalPeak = totalPeak + float(MainApp.allNodes_Dic[nodeID].peakAreas[i])

                        i = i + 1

                    MainApp.allNodes_Dic[nodeID].attributeAreas.append(totalPeak)

            i = 1
            for nodeID in MainApp.allNodes_Dic:
                for nodeAss in MainApp.allNodes_Dic[nodeID].associatedAttributes:
                    peakArea = 0
                    avPeakArea = 0
                    j = 0
                    for attID in MainApp.allAttributes_Dic:
                        if MainApp.allAttributes_Dic[attID].name == nodeAss:
                            peakArea = MainApp.allNodes_Dic[nodeID].attributeAreas[j]
                        j = j + 1
                    if MainApp.allNodes_Dic[nodeID].areaAttributes.count(nodeAss) != 0:
                        avPeakArea = peakArea / MainApp.allNodes_Dic[nodeID].areaAttributes.count(nodeAss)
                    else:
                        avPeakArea = 0
                    MainApp.allEdges_Dic[i] = newEdge(ID = i, targetNode = MainApp.allNodes_Dic[nodeID].ID, attributeTarget = nodeAss, sumOfPeakAreas = peakArea, averageOfPeakAreas = avPeakArea)
                    i = i + 1

        for attID in MainApp.allAttributes_Dic:
            MainApp.allAttributesList.append(MainApp.allAttributes_Dic[attID].name)

    def preferenceFilter(self):
        MainApp.nodesToWrite = {}
        MainApp.edgesToWrite = {}
        allNodesDicCopy = {}
        collapsedClusterDic = {}
        collapsedAdductDic = {}
        MainApp.clusterAdjustedEdges = {}
        MainApp.adductAdjustedEdges = {}
        allNodesDicCopy = copy.deepcopy(MainApp.allNodes_Dic)
        maxClusterIDVal = 0

        progress = 0
        root.title(MainApp.versionName + " - Removing Nodes with Unslected Attributes")
        #Remove unused attributes, retain attributes to be deleted, and give peak areas for selected attributes
        for nodeID in allNodesDicCopy:
            newAttList = []
            newAttPeakList = []
            i = 0
            for att in allNodesDicCopy[nodeID].associatedAttributes:
                if att in MainApp.uniqueAttributes or att in MainApp.attributesToDelete:
                    newAttList.append(att)
                    newAttPeakList.append(allNodesDicCopy[nodeID].attributeAreas[i])

            if float(allNodesDicCopy[nodeID].clusterID) > maxClusterIDVal:
                maxClusterIDVal = float(allNodesDicCopy[nodeID].clusterID)

                i = i + 1

            allNodesDicCopy[nodeID].associatedAttributes = newAttList
            allNodesDicCopy[nodeID].attributeAreas = newAttPeakList

            progress = progress + 1
            if progress/100 == int(progress/100):
                MainApp.progBar['value'] = ((progress+1)/len(allNodesDicCopy))*100
                MainApp.update_idletasks(self)
            if (progress+1)/len(allNodesDicCopy)*100 == 100:
                MainApp.progBar['value'] = 0

        root.title(MainApp.versionName)
        
        #Collapse Clusters into Nodes
        if self.q1.get() == 1:

            allClusterIDs = []

            i = 1
            for nodeID in allNodesDicCopy:
                ##Incorporate Ion Identity Nodes into Associated Clusters
                if MainApp.IIMN == 1:
                    if allNodesDicCopy[nodeID].molecularFeatureID in MainApp.allIonIdentities_Dic:
                        if float(MainApp.allIonIdentities_Dic[allNodesDicCopy[nodeID].molecularFeatureID].associatedCluster) != -1:
                            allNodesDicCopy[nodeID].clusterID = MainApp.allIonIdentities_Dic[allNodesDicCopy[nodeID].molecularFeatureID].associatedCluster
                        #Create New Clusters for indepenant Ion Identity Clusters
                        else:
                            maxClusterIDVal = maxClusterIDVal + 1
                            allNodesDicCopy[nodeID].clusterID = maxClusterIDVal
                            MainApp.allIonIdentities_Dic[allNodesDicCopy[nodeID].molecularFeatureID].associatedCluster = maxClusterIDVal


                        
                if float(allNodesDicCopy[nodeID].clusterID) <= 0:
                    collapsedClusterDic[i] = newNode(ID = allNodesDicCopy[nodeID].ID, associatedAttributes = allNodesDicCopy[nodeID].associatedAttributes, \
                                                     nodesInCluster = allNodesDicCopy[nodeID].nodesInCluster, nodeColour = "#FFFFFF", clusterID = allNodesDicCopy[nodeID].clusterID, \
                                                     mzVal = allNodesDicCopy[nodeID].mzVal, rtVal = allNodesDicCopy[nodeID].rtVal, \
                                                     peakAreas = allNodesDicCopy[nodeID].peakAreas, areaAttributes = allNodesDicCopy[nodeID].areaAttributes, \
                                                     featureName = allNodesDicCopy[nodeID].featureName, attributeAreas = allNodesDicCopy[nodeID].attributeAreas, OGNodeID = str(allNodesDicCopy[nodeID].OGNodeID), \
                                                     molecularFeatureID = "", assignedAdduct = "", sharedName = str(allNodesDicCopy[nodeID].sharedName))
                    i = i + 1
                else:
                    if allNodesDicCopy[nodeID].clusterID not in allClusterIDs:
                        allClusterIDs.append(allNodesDicCopy[nodeID].clusterID)
                        
                        collapsedClusterDic[i] = newNode(ID = allNodesDicCopy[nodeID].ID, associatedAttributes = allNodesDicCopy[nodeID].associatedAttributes, \
                                                         nodesInCluster = allNodesDicCopy[nodeID].nodesInCluster, nodeColour = "#FFFFFF", clusterID = allNodesDicCopy[nodeID].clusterID, \
                                                         mzVal = allNodesDicCopy[nodeID].mzVal, rtVal = allNodesDicCopy[nodeID].rtVal, \
                                                         peakAreas = allNodesDicCopy[nodeID].peakAreas, areaAttributes = allNodesDicCopy[nodeID].areaAttributes, \
                                                         featureName = allNodesDicCopy[nodeID].featureName, attributeAreas = allNodesDicCopy[nodeID].attributeAreas, OGNodeID = str(allNodesDicCopy[nodeID].OGNodeID), \
                                                         molecularFeatureID = "", assignedAdduct = "", sharedName = str(allNodesDicCopy[nodeID].sharedName))
                        i = i + 1
                    else:
                        for node in collapsedClusterDic:
                            if collapsedClusterDic[node].clusterID == allNodesDicCopy[nodeID].clusterID:
                                collapsedClusterDic[node].nodesInCluster = int(collapsedClusterDic[node].nodesInCluster) + 1
                                collapsedClusterDic[node].OGNodeID = str(collapsedClusterDic[node].OGNodeID) + ";" + str(allNodesDicCopy[nodeID].OGNodeID)
                                collapsedClusterDic[node].sharedName = str(collapsedClusterDic[node].sharedName) + ";" + str(allNodesDicCopy[nodeID].sharedName)
                                collapsedClusterDic[node].mzVal = collapsedClusterDic[node].mzVal + ";" + allNodesDicCopy[nodeID].mzVal
                                collapsedClusterDic[node].rtVal = collapsedClusterDic[node].rtVal + ";" + allNodesDicCopy[nodeID].rtVal
                                if allNodesDicCopy[nodeID].featureName != "-":
                                    if collapsedClusterDic[node].featureName == "-":
                                        collapsedClusterDic[node].featureName = ""
                                    collapsedClusterDic[node].featureName = collapsedClusterDic[node].featureName + ";" + allNodesDicCopy[nodeID].featureName

                                if allNodesDicCopy[nodeID].areaAttributes == collapsedClusterDic[node].areaAttributes:
                                    tempList = []
                                    tempList = [float(x) + float(y) for x, y in zip(allNodesDicCopy[nodeID].peakAreas, collapsedClusterDic[node].peakAreas)]
                                    collapsedClusterDic[node].peakAreas = tempList

                                else:
                                    j = 0
                                    for att in allNodesDicCopy[nodeID].areaAttributes:
                                        k = 0
                                        for collapsedAtt in collapsedClusterDic[node].areaAttributes:
                                            if att == collapsedAtt:
                                                collapsedClusterDic[node].peakAreas[k] = float(collapsedClusterDic[node].peakAreas[k]) + float(allNodesDicCopy[nodeID].peakAreas[j])
                                            k = k + 1
                                        j = j + 1
                                    
            for nodeID in collapsedClusterDic:
                if collapsedClusterDic[nodeID].nodesInCluster > 1:
                    assAtt = []
                    j = 0
                    for allPeaks in collapsedClusterDic[nodeID].peakAreas:
                        if float(allPeaks) > 0:
                            if collapsedClusterDic[nodeID].areaAttributes[j] in MainApp.uniqueAttributes or collapsedClusterDic[nodeID].areaAttributes[j] in MainApp.attributesToDelete:
                                assAtt.append(collapsedClusterDic[nodeID].areaAttributes[j])
                        j = j + 1
                    
                    collapsedClusterDic[nodeID].associatedAttributes = assAtt
                    collapsedClusterDic[nodeID].associatedAttributes.sort()
                    collapsedClusterDic[nodeID].attributeAreas = [0] * len(assAtt)
                        
                    j = 0
                    for att in collapsedClusterDic[nodeID].associatedAttributes:
                        collapsedClusterDic[nodeID].attributeAreas[j] = 0
                        k = 0
                        for allAtt in collapsedClusterDic[nodeID].areaAttributes:
                            if allAtt == att:
                                collapsedClusterDic[nodeID].attributeAreas[j] = float(collapsedClusterDic[nodeID].attributeAreas[j]) + float(collapsedClusterDic[nodeID].peakAreas[k])
                            k = k + 1
                        j = j + 1
  
            allNodesDicCopy = copy.deepcopy(collapsedClusterDic)

            edgeID = 1

            for nodeID in allNodesDicCopy:
                j = 0
                
                for association in allNodesDicCopy[nodeID].associatedAttributes:
                    MainApp.clusterAdjustedEdges[edgeID] = newEdge(ID = edgeID, targetNode = allNodesDicCopy[nodeID].ID, attributeTarget = association, \
                                                                   sumOfPeakAreas = allNodesDicCopy[nodeID].attributeAreas[j], averageOfPeakAreas = allNodesDicCopy[nodeID].attributeAreas[j])
                    edgeID = edgeID + 1
                    j = j + 1
            MainApp.adductAdjustedEdges = {}

            
        i = 1
        progress = 0
        root.title(MainApp.versionName + " - Creating Needed Nodes")
        for nodeID in allNodesDicCopy:
            keepNode = 0
            totalAttAss = 0

            #Exclude Universal Nodes
            if self.q3.get() == 1:
                #Removes nodes that are universal
                for selectedAtt in MainApp.uniqueAttributes:
                    if selectedAtt not in allNodesDicCopy[nodeID].associatedAttributes:
                        keepNode = 1
                    else:
                        totalAttAss = totalAttAss + 1
            else:
                keepNode = 1
                totalAttAss = totalAttAss + 1

            #Removes nodes that are selected for deletion
            for selectedAtt in MainApp.attributesToDelete:
                if selectedAtt in allNodesDicCopy[nodeID].associatedAttributes:
                    keepNode = 0

            #Removes nodes that are only associated with unselected attributes
            singletonNode = 1
            for selectedAtt in allNodesDicCopy[nodeID].associatedAttributes:
                if selectedAtt in MainApp.uniqueAttributes:
                    singletonNode = 0
            if singletonNode == 1:
                keepNode = 0
            

            if keepNode == 1:
                if self.q3B.get() == 1:
                        
                    if totalAttAss <= int(self.QuestionNo03B_Spin.get()):
                        MainApp.nodesToWrite[i] = newNode(ID = allNodesDicCopy[nodeID].ID, associatedAttributes = allNodesDicCopy[nodeID].associatedAttributes, \
                                                          nodesInCluster = allNodesDicCopy[nodeID].nodesInCluster, nodeColour = "#FFFFFF", clusterID = allNodesDicCopy[nodeID].clusterID, \
                                                          mzVal = allNodesDicCopy[nodeID].mzVal, rtVal = allNodesDicCopy[nodeID].rtVal, \
                                                          peakAreas = allNodesDicCopy[nodeID].peakAreas, areaAttributes = allNodesDicCopy[nodeID].areaAttributes, \
                                                          featureName = allNodesDicCopy[nodeID].featureName, attributeAreas = allNodesDicCopy[nodeID].attributeAreas, \
                                                          OGNodeID = allNodesDicCopy[nodeID].OGNodeID, molecularFeatureID = allNodesDicCopy[nodeID].molecularFeatureID, \
                                                          assignedAdduct = allNodesDicCopy[nodeID].assignedAdduct, sharedName = allNodesDicCopy[nodeID].sharedName)
                        i = i + 1

                else:
                    MainApp.nodesToWrite[i] = newNode(ID = allNodesDicCopy[nodeID].ID, associatedAttributes = allNodesDicCopy[nodeID].associatedAttributes, \
                                                      nodesInCluster = allNodesDicCopy[nodeID].nodesInCluster, nodeColour = "#FFFFFF", clusterID = allNodesDicCopy[nodeID].clusterID, \
                                                      mzVal = allNodesDicCopy[nodeID].mzVal, rtVal = allNodesDicCopy[nodeID].rtVal, \
                                                      peakAreas = allNodesDicCopy[nodeID].peakAreas, areaAttributes = allNodesDicCopy[nodeID].areaAttributes, \
                                                      featureName = allNodesDicCopy[nodeID].featureName, attributeAreas = allNodesDicCopy[nodeID].attributeAreas, \
                                                      OGNodeID = allNodesDicCopy[nodeID].OGNodeID, molecularFeatureID = allNodesDicCopy[nodeID].molecularFeatureID, \
                                                      assignedAdduct = allNodesDicCopy[nodeID].assignedAdduct, sharedName = allNodesDicCopy[nodeID].sharedName)
                    i = i + 1

            progress = progress + 1
            if progress/100 == int(progress/100):
                MainApp.progBar['value'] = ((progress+1)/len(allNodesDicCopy))*100
                MainApp.update_idletasks(self)
            if (progress+1)/len(allNodesDicCopy)*100 == 100:
                MainApp.progBar['value'] = 0


    def edgeWriter(self):

        edgesToSearch = {}
        MainApp.AttSummary = {}
        MainApp.maxEdge = 0
        MainApp.minEdge = 123456789
        MainApp.maxNode = 5
        if MainApp.adductAdjustedEdges != {}:
            edgesToSearch = copy.deepcopy(MainApp.adductAdjustedEdges)
        if MainApp.clusterAdjustedEdges != {}:
            edgesToSearch = copy.deepcopy(MainApp.clusterAdjustedEdges)
        else:
            edgesToSearch = copy.deepcopy(MainApp.allEdges_Dic)
            
        MainApp.edgesToWrite = {}
        i = 1
        progress = 0
        root.title(MainApp.versionName + " - Creating Needed Edges")
        
        for nodeID in MainApp.nodesToWrite:
            for edgeID in edgesToSearch:
                if MainApp.nodesToWrite[nodeID].ID == edgesToSearch[edgeID].targetNode and edgesToSearch[edgeID].attributeTarget in MainApp.uniqueAttributes:
                    MainApp.edgesToWrite[i] = newEdge(ID = edgesToSearch[edgeID].ID, targetNode = edgesToSearch[edgeID].targetNode, \
                                              attributeTarget = edgesToSearch[edgeID].attributeTarget, \
                                              sumOfPeakAreas = edgesToSearch[edgeID].sumOfPeakAreas, averageOfPeakAreas = edgesToSearch[edgeID].averageOfPeakAreas)
                    if MainApp.maxEdge < float(MainApp.edgesToWrite[i].averageOfPeakAreas):
                        MainApp.maxEdge = float(MainApp.edgesToWrite[i].averageOfPeakAreas)
                    if MainApp.minEdge == 123456789:
                        MainApp.minEdge = float(MainApp.edgesToWrite[i].averageOfPeakAreas)
                    elif MainApp.minEdge > float(MainApp.edgesToWrite[i].averageOfPeakAreas):
                        MainApp.minEdge = float(MainApp.edgesToWrite[i].averageOfPeakAreas)
                        
                    i = i + 1

            progress = progress + 1
            if progress/200 == int(progress/200):
                MainApp.progBar['value'] = ((progress+1)/len(MainApp.nodesToWrite))*100
                MainApp.update_idletasks(self)
            if (progress+1)/len(MainApp.nodesToWrite)*100 == 100:
                MainApp.progBar['value'] = 0

        attCount = 0               
        for nodeID in MainApp.nodesToWrite:
            attAssSum = ""
            for att in MainApp.nodesToWrite[nodeID].associatedAttributes:
                attAssSum = attAssSum + att + ":"
            if attAssSum not in MainApp.possibleAttAss:
                MainApp.possibleAttAss.append(attAssSum)

            if attAssSum not in MainApp.AttSummary:
                attCount = attCount + 1
                MainApp.AttSummary[attAssSum] = usedAttribute(name = attAssSum, totalNodes = 1, currentCount = 0, keyAttribute = 0, attID = attCount)
            else:
                MainApp.AttSummary[attAssSum].totalNodes = MainApp.AttSummary[attAssSum].totalNodes + 1

            if int(MainApp.nodesToWrite[nodeID].nodesInCluster) > int(MainApp.maxNode):
                MainApp.maxNode = MainApp.nodesToWrite[nodeID].nodesInCluster
                    
        for att in MainApp.allAttributes_Dic:
            if MainApp.allAttributes_Dic[att].name in MainApp.uniqueAttributes:
                MainApp.nodesToWrite[len(MainApp.nodesToWrite)+1] = newNode(ID = MainApp.allAttributes_Dic[att].name, associatedAttributes = [MainApp.allAttributes_Dic[att].name], \
                                                                            nodesInCluster = 1, nodeColour = "#FFFFFF", clusterID = 0, mzVal = 0, rtVal = 0, \
                                                                            peakAreas = [], areaAttributes = [], featureName = MainApp.allAttributes_Dic[att].name, attributeAreas = [], OGNodeID = "", \
                                                                            molecularFeatureID = "", assignedAdduct = "", sharedName = "")

                if MainApp.allAttributes_Dic[att].name + ":" in MainApp.AttSummary:
                    MainApp.AttSummary[MainApp.allAttributes_Dic[att].name + ":"].keyAttribute = 1
                    MainApp.AttSummary[MainApp.allAttributes_Dic[att].name + ":"].totalNodes = MainApp.AttSummary[MainApp.allAttributes_Dic[att].name + ":"].totalNodes + 1
                else:
                    attCount = attCount + 1
                    MainApp.AttSummary[MainApp.allAttributes_Dic[att].name + ":"] = usedAttribute(name = attAssSum, totalNodes = 1, currentCount = 0, keyAttribute = 1, attID = attCount)
                    

    def writeNewFile(self):
                
        startCol = Color("#FF1234")
        colourProfiles1 = []
        colourProfiles1 = list(startCol.range_to(Color("#12FF34"),int(len(MainApp.possibleAttAss)/2)+1))
        colourProfiles2 = []
        colourProfiles2 = list(Color("#12FF56").range_to(Color("#1234FF"),int(len(MainApp.possibleAttAss)/2)+1))
        colourProfiles = []
        colourProfiles = colourProfiles1 + colourProfiles2

        fileSaveName = self.folderOutput

        if str(fileSaveName) != "None":
            nodes = []
            edges = []
            nodes.append('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>')
            nodes.append('<graph id="124" label="Sheet1" directed="1" cy:documentVersion="3.0" xmlns:dc="http://purl.org/dc/elements/1.1/" ' + \
                    'xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:cy="http://www.cytoscape.org" xmlns="http://www.cs.rpi.edu/XGMML">')
            nodes.append('  <att name="networkMetadata">')
            nodes.append('    <rdf:RDF>')
            nodes.append('      <rdf:Description rdf:about="http://www.cytoscape.org/">')
            nodes.append('        <dc:type>Protein-Protein Interaction</dc:type>')
            nodes.append('        <dc:description>N/A</dc:description>')
            nodes.append('        <dc:identifier>N/A</dc:identifier>')
            nodes.append('        <dc:date>2022-11-09 19:07:57</dc:date>')
            nodes.append('        <dc:title>Sheet1</dc:title>')
            nodes.append('        <dc:source>http://www.cytoscape.org/</dc:source>')
            nodes.append('        <dc:format>Cytoscape-XGMML</dc:format>')
            nodes.append('      </rdf:Description>')
            nodes.append('    </rdf:RDF>')
            nodes.append('  </att>')
            nodes.append('  <att name="shared name" value="Sheet1" type="string" cy:type="String"/>')
            nodes.append('  <att name="name" value="Sheet1" type="string" cy:type="String"/>')
            nodes.append('  <att name="selected" value="1" type="boolean" cy:type="Boolean"/>')
            nodes.append('  <att name="networkMetadata" type="string" cy:type="String"/>')
            nodes.append('  <att name="__Annotations" type="list" cy:type="List" cy:elementType="String">')
            nodes.append('  </att>')
            nodes.append('  <att name="layoutAlgorithm" value="Prefuse Force Directed Layout" type="string" cy:type="String" cy:hidden="1"/>')

            size = 0
            i = 0
            x = 0
            y = 0
            progress = 0
            root.title(MainApp.versionName + " - Writing new nodes to graph file")
            for nodeID in MainApp.nodesToWrite:

                size = int(MainApp.nodesToWrite[nodeID].nodesInCluster)
                if size == 0:
                    size = 1

                currentNdCol = "#AFE8FF"
                currentAtts = ""
                for atAs in range(len(MainApp.possibleAttAss)):
                    attToCompare = ""
                    for att in MainApp.nodesToWrite[nodeID].associatedAttributes:
                        attToCompare = attToCompare + att + ":"
                        
                    if MainApp.possibleAttAss[atAs] == attToCompare:
                        currentNdCol = str(colourProfiles[atAs])
             
                currentNode = MainApp.nodesToWrite[nodeID].featureName
                nodes.append('  <node id="' + str(MainApp.nodesToWrite[nodeID].ID) + '" label="' + str(currentNode) + '">')
                nodes.append('    <att name="Node ID" value="' + str(MainApp.nodesToWrite[nodeID].ID) + '" type="string" cy:type="String"/>')
                if MainApp.classical == 1:
                    nodes.append('    <att name="shared name" value="' + str(MainApp.nodesToWrite[nodeID].sharedName) + '" type="string" cy:type="String"/>')
                elif MainApp.uploadType != "GNPS":
                    nodes.append('    <att name="shared name" value="' + str(currentNode) + '" type="string" cy:type="String"/>')
                else:
                    nodes.append('    <att name="shared name" value="' + str(MainApp.nodesToWrite[nodeID].OGNodeID) + '" type="string" cy:type="String"/>')
                if MainApp.uploadType == "GNPS":
                    nodes.append('    <att name="Compound names" value="' + str(currentNode) + '" type="string" cy:type="String"/>')
                    nodes.append('    <att name="GNPS Node ID" value="' + str(MainApp.nodesToWrite[nodeID].OGNodeID) + '" type="string" cy:type="String"/>')
                    nodes.append('    <att name="GNPS Cluster ID" value="' + str(MainApp.nodesToWrite[nodeID].clusterID) + '" type="string" cy:type="String"/>')
                else:
                    nodes.append('    <att name="Feature name" value="' + str(currentNode) + '" type="string" cy:type="String"/>')
                    nodes.append('    <att name="Feature Table ID" value="' + str(MainApp.nodesToWrite[nodeID].OGNodeID) + '" type="string" cy:type="String"/>')
                if MainApp.IIMN == 1:
                    nodes.append('    <att name="Adducts" value="' + str(MainApp.nodesToWrite[nodeID].assignedAdduct) + '" type="string" cy:type="String"/>')
                    nodes.append('    <att name="Molecular ID" value="' + str(MainApp.nodesToWrite[nodeID].molecularFeatureID) + '" type="string" cy:type="String"/>')
                nodes.append('    <att name="Feature Parent Masses" value="' + str(MainApp.nodesToWrite[nodeID].mzVal) + '" type="string" cy:type="String"/>')
                nodes.append('    <att name="Feature Retention Times" value="' + str(MainApp.nodesToWrite[nodeID].rtVal) + '" type="string" cy:type="String"/>')
                nodes.append('    <att name="selected" value="0" type="boolean" cy:type="Boolean"/>')
                
                if currentNode in MainApp.uniqueAttributes:
                    colour = "#E0E0E0"
                    outLineColour = "#9E9E9E"
                    size = 80
                    nodeWidth = 3
                else:
                    colour = currentNdCol
                    outLineColour = "#CCCCCC"
                    nodeWidth = 0

                assAtts = ""
                for att in MainApp.nodesToWrite[nodeID].associatedAttributes:
                    assAtts = assAtts + att + ":"

                if currentNode + ":" == assAtts:
                    centerNode = 1
                else:
                    centerNode = 0

                numOfAttAss = len(MainApp.AttSummary)

                MainApp.AttSummary[assAtts].currentCount = MainApp.AttSummary[assAtts].currentCount + 1
                x, y = DefineCoordinates(MainApp.AttSummary[assAtts].currentCount, MainApp.AttSummary[assAtts].totalNodes, MainApp.AttSummary[assAtts].attID, \
                                         numOfAttAss, MainApp.AttSummary[assAtts].keyAttribute, centerNode)

                nodes.append('    <att name="Nodes in cluster" value="' + str(size) + '" type="real" cy:type="Double"/>')
                nodes.append('    <att name="Associated Attributes" value="' + str(assAtts) + '" type="string" cy:type="String"/>')
                nodes.append('    <att name="Node colour" value="' + str(colour) + '" type="string" cy:type="String"/>')
                nodes.append('    <graphics type="ELLIPSE"  width="' + str(nodeWidth) + '" outline="' + str(outLineColour) + '" fill="' + colour + '" h="' + str(math.sqrt(size)*3) + '" w="' + str(math.sqrt(size)*3) + '" y="' + str(y*10) + '" x="' + str(x*10) + '" >')
                nodes.append('      <att name="COMPOUND_NODE_PADDING" value="10.0" type="string" cy:type="String"/>')
                nodes.append('      <att name="NODE_VISIBLE" value="true" type="string" cy:type="String"/>')
                nodes.append('      <att name="NODE_LABEL_FONT_SIZE" value="1" type="string" cy:type="String"/>')
                nodes.append('    </graphics>')
                nodes.append('  </node>')

                progress = progress + 1
                if progress/50 == int(progress/50):
                    MainApp.progBar['value'] = ((progress+1)/len(MainApp.nodesToWrite))*100
                    MainApp.update_idletasks(self)
                if (progress+1)/len(MainApp.nodesToWrite)*100 == 100:
                    MainApp.progBar['value'] = 0

                i = i + 1

            progress = 0
            root.title(MainApp.versionName + " - Writing new edges to graph file")
            for edgeID in MainApp.edgesToWrite:

                normalisedEdgeWeight = float(MainApp.edgesToWrite[edgeID].averageOfPeakAreas) / MainApp.maxEdge * 3
                                
                edges.append('  <edge id="' + str(MainApp.edgesToWrite[edgeID].ID) + '" label="' + str(MainApp.edgesToWrite[edgeID].targetNode) + ' (pp) ' + str(MainApp.edgesToWrite[edgeID].attributeTarget) + '" source="' + \
                             str(MainApp.edgesToWrite[edgeID].targetNode) + '" target="' + str(MainApp.edgesToWrite[edgeID].attributeTarget) + '" cy:directed="1">')
                edges.append('    <att name="shared name" value="' + str(MainApp.edgesToWrite[edgeID].targetNode) + ' (pp) ' + str(MainApp.edgesToWrite[edgeID].attributeTarget) + '" type="string" cy:type="String"/>')
                edges.append('    <att name="shared interaction" value="pp" type="string" cy:type="String"/>')
                edges.append('    <att name="name" value="' + str(MainApp.edgesToWrite[edgeID].targetNode) + ' (pp) ' + str(MainApp.edgesToWrite[edgeID].attributeTarget) + '" type="string" cy:type="String"/>')
                edges.append('    <att name="selected" value="0" type="boolean" cy:type="Boolean"/>')
                edges.append('    <att name="interaction" value="pp" type="string" cy:type="String"/>')
                if MainApp.uploadType == "Table":
                    edges.append('    <att name="Sum peak area of feature" value="' + str(MainApp.edgesToWrite[edgeID].sumOfPeakAreas) + '" type="real" cy:type="Double"/>')
                    edges.append('    <att name="Average peak area of feature" value="' + str(MainApp.edgesToWrite[edgeID].averageOfPeakAreas) + '" type="real" cy:type="Double"/>')
                else:
                    edges.append('    <att name="Average peak area of cluster nodes" value="' + str(MainApp.edgesToWrite[edgeID].averageOfPeakAreas) + '" type="real" cy:type="Double"/>')
                edges.append('    <att name="SqurRoot Normalised Area" value="' + str(normalisedEdgeWeight) + '" type="real" cy:type="Double"/>')
                edges.append('    <graphics fill="#AFAFAF"  width="' + str(normalisedEdgeWeight) + '">')
                edges.append('          <att name="EDGE_TRANSPARENCY" value="150" type="string" cy:type="String"/>')
                edges.append('    </graphics>')
                edges.append('  </edge>')

                progress = progress + 1
                if progress/50 == int(progress/50):
                    MainApp.progBar['value'] = ((progress+1)/len(MainApp.edgesToWrite))*100
                    MainApp.update_idletasks(self)
                if (progress+1)/len(MainApp.edgesToWrite)*100 == 100:
                    MainApp.progBar['value'] = 0

            completeNetwork = []
            for node in nodes:
                completeNetwork.append(node)
            for edge in edges:
                completeNetwork.append(edge)

            completeNetwork.append('</graph>')
            
            with open(fileSaveName.name,'w') as j:
                for nodesAndEdges in completeNetwork:
                    line = nodesAndEdges
                    j.write(f"{line}\n")

        root.title(MainApp.versionName)
        MainApp.progBar['value'] = 0

    def __init__(self, parent, *args, **kwargs):

        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.initialiseGUI()
        
    def initialiseGUI(self):
        MainApp.versionName = 'MolNetInvert v1.0'
        root.title(MainApp.versionName)
        root.geometry('536x475') #x,y
        root.configure(background='white')
        root.resizable(False, False)

        root.configure(background='white')
        self.databaseCoreColour = "#EEEEEE"

        self.checkSheetCover = Frame(root, bg='white')
        self.checkSheetCover.grid(row=1, column=1, columnspan=100, rowspan=100, sticky="neswn", padx=(0,0), pady=(0,0))
        self.checkSheet_Frame = Frame(self.checkSheetCover, bd=1, bg='white')
        self.checkSheet_Frame.grid(row=2, column=2, columnspan=98, rowspan=96, sticky="neswn", padx=(0,0), pady=(0,10))
        self.checkSheet_Canvas = Canvas(self.checkSheet_Frame, bg=self.databaseCoreColour)
        self.checkSheet_Canvas.grid(row=3, column=3, columnspan=96, rowspan=94, sticky="neswn", padx=(10,10), pady=(10,10))

        MainApp.progBar = ttk.Progressbar(self.checkSheet_Canvas, orient=HORIZONTAL)
        MainApp.progBar.grid(row=21, column=1, columnspan=10, pady=(0,0), sticky=EW)

        MainApp.Title_Label = Label(self.checkSheet_Canvas, bg=self.databaseCoreColour, text="")
        MainApp.Title_Label.grid(row=4, column=1, columnspan=10, rowspan=1, sticky="W", padx=(0,570), pady=(0,190))

        self.MakeBoxes()
        
        def on_close():
            root.destroy()

        root.protocol("WM_DELETE_WINDOW",  on_close)

    def MakeBoxes(self):

        MainApp.Title_Label.grid_remove()

        self.AllAtts = MainApp.uniqueAttributes
        self.AttToAdd = []
        self.AttToDel = []

        self.networkTypeVal = IntVar()
        self.featureBased_Radio = Radiobutton(self.checkSheet_Canvas, text="GNPS: Feature Based", variable=self.networkTypeVal, value=1, command=self.RadioSelect)
        self.featureBased_Radio.grid(row=2, column=1, columnspan=3, rowspan=1, sticky="N", padx=(2,2), pady=(2,0))
        
        self.classical_Radio = Radiobutton(self.checkSheet_Canvas, text="GNPS: Classical", variable=self.networkTypeVal, value=2, command=self.RadioSelect)
        self.classical_Radio.grid(row=3, column=1, columnspan=3, rowspan=1, sticky="N", padx=(2,2), pady=0)

        self.featureBasedPlus_Radio = Radiobutton(self.checkSheet_Canvas, text="GNPS: Feature Based + Metadata Preference List", variable=self.networkTypeVal, value=3, command=self.RadioSelect)
        self.featureBasedPlus_Radio.grid(row=4, column=1, columnspan=3, rowspan=1, sticky="N", padx=(2,2), pady=0)
        
        self.QuantTable_Radio = Radiobutton(self.checkSheet_Canvas, text="Feature List (Quant Table) + Metadata Table", variable=self.networkTypeVal, value=4, command=self.RadioSelect)
        self.QuantTable_Radio.grid(row=5, column=1, columnspan=3, rowspan=1, sticky="N", padx=(2,2), pady=(0,10))

        self.RadioNo01_ttp = CreateToolTip(self.featureBased_Radio, "For directly uploading .graphML files created by GNPS FBMN and IIMN workflows.")
        self.RadioNo02_ttp = CreateToolTip(self.classical_Radio, "For directly uploading .graphML files created by GNPS via classical molecular networking workflow.")
        self.RadioNo03_ttp = CreateToolTip(self.featureBasedPlus_Radio, "For directly uploading .graphML files created by the GNPS FBMN workflow, with an accompanying list of metadata attributes in a .txt file.")
        self.RadioNo04_ttp = CreateToolTip(self.QuantTable_Radio, "For uploading data in the form of a .csv feature list, and tab separated metadata .txt files")

        self.In_Btn = Button(self.checkSheet_Canvas, width=20, text="Select File to Process", command=self.OpenFile, state=DISABLED)
        self.In_Btn.grid(row=6, column=1, columnspan=3, rowspan=1, sticky="N", padx=(2,2), pady=(0,10))

        self.AddAttribute_Label = Label(self.checkSheet_Canvas, bg=self.databaseCoreColour, text="All Attributes:")
        self.AddAttribute_Label.grid(row=7, column=1, columnspan=1, rowspan=1, sticky="E", padx=(10,2), pady=(0,0))
        self.AddAttribute_Options = sorted(self.AllAtts) #self.AttributesToAdd
        self.AddAttribute_CBox = ttk.Combobox(self.checkSheet_Canvas, values=self.AddAttribute_Options,state=DISABLED)
        if self.AllAtts != []:
            self.AddAttribute_CBox.insert(0, self.AddAttribute_Options[0])
        self.AddAttribute_CBox.config(state=DISABLED)
        self.AddAttribute_CBox.grid(row=7, column=2, columnspan=2, rowspan=1, sticky="WE", padx=(2,50), pady=0)

        self.RemoveAttribute_Label = Label(self.checkSheet_Canvas, bg=self.databaseCoreColour, text="Included attribute nodes:")
        self.RemoveAttribute_Label.grid(row=9, column=1, columnspan=1, rowspan=1, sticky="E", padx=(10,2), pady=(0,0))
        self.RemoveAttribute_Options = self.AttToAdd #self.AttributesToRemove
        self.RemoveAttribute_CBox = ttk.Combobox(self.checkSheet_Canvas, width = 45, values=self.RemoveAttribute_Options,state=DISABLED)
        self.RemoveAttribute_CBox.insert(0, "")
        self.RemoveAttribute_CBox.config(state=DISABLED)
        self.RemoveAttribute_CBox.grid(row=9, column=2, columnspan=2, rowspan=1, sticky="WE", padx=(2,50), pady=0)

        self.AttributesToDelete_Label = Label(self.checkSheet_Canvas, bg=self.databaseCoreColour, text="Delete nodes with attributes:")
        self.AttributesToDelete_Label.grid(row=10, column=1, columnspan=1, rowspan=1, sticky="E", padx=(10,2), pady=(5,0))
        self.AttributesToDelete_Options = self.AttToDel #self.AttributesToDelete
        self.AttributesToDelete_CBox = ttk.Combobox(self.checkSheet_Canvas, values=self.AttributesToDelete_Options,state=NORMAL)
        self.AttributesToDelete_CBox.insert(0, "")
        self.AttributesToDelete_CBox.config(state=DISABLED)
        self.AttributesToDelete_CBox.grid(row=10, column=2, columnspan=2, rowspan=1, sticky="WE", padx=(2,50), pady=(5,0))

        self.SpaceHolder_Label = Label(self.checkSheet_Canvas, bg=self.databaseCoreColour, text=" ")
        self.SpaceHolder_Label.grid(row=12, column=1, columnspan=1, rowspan=1, sticky="E", padx=(10,2), pady=(5,0))

        self.q1 = tk.IntVar()
        self.q3 = tk.IntVar()
        self.q3B = tk.IntVar()

        self.q3B_SpinVal = [1,2,3,4,5,6,7,8,9]

        self.QuestionNo01_Check = Checkbutton(self.checkSheet_Canvas, text='Collapse Clusters Into Single Nodes', variable = self.q1, onvalue=1, offvalue=0,state=DISABLED)
        self.QuestionNo03_Check = Checkbutton(self.checkSheet_Canvas, text='Exclude Universal Nodes', variable = self.q3, onvalue=1, offvalue=0, command=self.ExcludeUniCluster, state=DISABLED)
        self.QuestionNo03B_Check = Checkbutton(self.checkSheet_Canvas, text='Max. Node-Attrubute Edges:', variable = self.q3B, onvalue=1, offvalue=0, command=self.ExcludeSpecificNum, state=DISABLED)

        self.QuestionNo03B_Spin = Spinbox(self.checkSheet_Canvas, values = self.q3B_SpinVal, width=2,state=DISABLED)

        self.QuestionNo01_ttp = CreateToolTip(self.QuestionNo01_Check, "Nodes within the same cluster in the original network will be represented as a single node in the new processed network")
        self.QuestionNo03_ttp = CreateToolTip(self.QuestionNo03_Check, "Exclude singletons (or collapsed clusters) from the original network that are present in all selected attributes")
        self.QuestionNo03B_ttp = CreateToolTip(self.QuestionNo03B_Check, 'Only include singletons (or collapsed clusters) from the original network that are present "n" or less selected attributes')

        self.QuestionNo01_Check.grid(row=12, column=2, columnspan=2, rowspan=1, sticky="W", padx=(10,2), pady=(0,0))
        self.QuestionNo03_Check.grid(row=13, column=2, columnspan=1, rowspan=1, sticky="W", padx=(10,2), pady=(0,0))
        self.QuestionNo03B_Check.grid(row=14, column=2, columnspan=1, rowspan=1, sticky="W", padx=(40,2), pady=(0,0))

        self.QuestionNo03B_Spin.grid(row=14, column=3, columnspan=1, rowspan=1, sticky="W", padx=(0,2), pady=(0,0))

        self.Out_Btn = Button(self.checkSheet_Canvas, width=20, text="Process Network", command=self.SelectOutPut,state=DISABLED)
        self.Out_Btn.grid(row=18, column=1, columnspan=3, rowspan=1, sticky="N", padx=(2,2), pady=(10,10))

        self.Add_Btn = Button(self.checkSheet_Canvas, width=16, text="Add Attribute", command=self.AttributeAdd,state=DISABLED)
        self.DeleteNodes_Btn = Button(self.checkSheet_Canvas, width=16, text="Delete Attribute", command=self.DeleteAttribute,state=DISABLED)
        
        self.Remove_Btn = Button(self.checkSheet_Canvas, width=18, text="Clear Selections", command=self.ClearAttSelection,state=DISABLED)

        self.Add_Btn.grid(row=8, column=2, columnspan=1, rowspan=1, sticky="W", padx=(2,0), pady=10)
        self.DeleteNodes_Btn.grid(row=8, column=2, columnspan=1, rowspan=1, sticky="E", padx=(0,2), pady=10)
        self.Remove_Btn.grid(row=11, column=2, columnspan=1, rowspan=1, sticky="N", padx=(2,2), pady=10)

    def RadioSelect(self):
        self.In_Btn.config(state=NORMAL)

        if self.networkTypeVal.get() == 4:
            self.QuestionNo01_Check.grid_remove()
            self.QuestionNo03_Check.config(text="Exclude Universal Features")
            self.QuestionNo03B_Check.config(text="Max. Feature-Attrubute Edges:")
            self.AttributesToDelete_Label.config(text="Delete features with attributes:")

            self.QuestionNo03_ttp = CreateToolTip(self.QuestionNo03_Check, "Exclude features that are present in all selected attributes")
            self.QuestionNo03B_ttp = CreateToolTip(self.QuestionNo03B_Check, 'Only include features that are present in "n" or less selected attributes')
            root.geometry('545x452')

        else:
            self.QuestionNo01_Check.grid(row=12, column=2, columnspan=2, rowspan=1, sticky="W", padx=(10,2), pady=(0,0))
            self.QuestionNo03_Check.grid(row=13, column=2, columnspan=1, rowspan=1, sticky="W", padx=(10,2), pady=(0,0))
            self.QuestionNo03B_Check.grid(row=14, column=2, columnspan=1, rowspan=1, sticky="W", padx=(40,2), pady=(0,0))

            self.QuestionNo03_Check.config(text="Exclude Universal Nodes")
            self.QuestionNo03B_Check.config(text="Max. Node-Attrubute Edges:")
            self.AttributesToDelete_Label.config(text="Delete nodes with attributes:")

            self.QuestionNo03_ttp = CreateToolTip(self.QuestionNo03_Check, "Exclude clusters from the original network that are present in all selected attributes")
            self.QuestionNo03B_ttp = CreateToolTip(self.QuestionNo03B_Check, 'Only include clusters from the original network that are present in "n" or less selected attributes')
            root.geometry('536x475')
                
    def ExcludeSpecificNum(self):
        if self.q3B.get() == 1:
            self.QuestionNo03B_Spin.config(state=NORMAL)
        else:
            self.QuestionNo03B_Spin.config(state=DISABLED)

    def ExcludeUniCluster(self):
        if self.q3.get() == 1:
            self.QuestionNo03B_Check.config(state=NORMAL)
        else:
            self.q3B = tk.IntVar(value=0)
            self.QuestionNo03B_Check.config(state=DISABLED, variable = self.q3B)
            self.QuestionNo03B_Spin.config(state=DISABLED)

    def OpenFile(self):
        self.AddAttribute_Options = []
        self.AddAttribute_CBox.config(values=self.AddAttribute_Options, state='normal')
        self.AddAttribute_CBox.delete(0, "")
        self.AddAttribute_CBox.config(state='readonly')
        self.RemoveAttribute_Options = []
        self.RemoveAttribute_CBox.config(values=self.RemoveAttribute_Options, state='normal')
        self.RemoveAttribute_CBox.delete(0, "")
        self.RemoveAttribute_CBox.config(state='readonly')
        self.AttributesToDelete_CBox.config(values=self.RemoveAttribute_Options, state='normal')
        self.AttributesToDelete_CBox.delete(0, "")
        self.AttributesToDelete_CBox.config(state='readonly')

        if self.networkTypeVal.get() < 3:
            MainApp.uploadType = "GNPS"
            MainApp.file_path = filedialog.askopenfilename(filetypes=[('Network File (graphml)', ['*.graphml'])])
            self.dataFromGraphFile()
        elif self.networkTypeVal.get() == 3:
            MainApp.uploadType = "GNPS"
            MainApp.file_path = filedialog.askopenfilename(filetypes=[('Network File (graphml)', ['*.graphml'])])
            MainApp.file_pathMetaData = filedialog.askopenfilename(filetypes=[('Metadata List (.txt)', ['*.txt'])])
            self.dataFromGraphFile()
        else:
            MainApp.uploadType = "Table"
            MainApp.file_path = filedialog.askopenfilename(filetypes=[('Feature Table (.csv)', ['*.csv'])])
            MainApp.file_pathMetaData = filedialog.askopenfilename(filetypes=[('Metadata (tab delimited .txt)', ['*.txt'])])
            self.getFeatureTableFile()

        self.AllAtts = MainApp.allAttributesList
        self.AttToAdd = []
        
        if self.AllAtts != []:
            self.QuestionNo01_Check.config(state="normal")
            self.Add_Btn.config(state="normal")
            self.In_Btn.config(state="disabled")
            self.Remove_Btn.config(state="normal")
            self.DeleteNodes_Btn.config(state="normal")
            self.AddAttribute_Options = sorted(self.AllAtts)
            self.AddAttribute_CBox.config(values=self.AddAttribute_Options,state="normal") 
            self.AddAttribute_CBox.insert(0, self.AddAttribute_Options[0])
            self.AddAttribute_CBox.config(state="readonly")

            self.featureBased_Radio.config(state="disabled")
            self.classical_Radio.config(state="disabled")
            self.featureBasedPlus_Radio.config(state="disabled")
            self.QuantTable_Radio.config(state="disabled")

            self.QuestionNo03_Check.config(state="normal")
            
    def SelectOutPut(self):
        if self.q3B.get() == 0:
            outPutFileName = MainApp.newFileName.split(".xgmml")[0] + "_" + str(self.q1.get())+str(self.q3.get())+ "0" + ".xgmml"
        else:
            outPutFileName = MainApp.newFileName.split(".xgmml")[0] + "_" + str(self.q1.get())+str(self.q3.get())+str(self.QuestionNo03B_Spin.get()) + ".xgmml"
        
        self.folderOutput = filedialog.asksaveasfile(mode='wb', initialfile = outPutFileName, defaultextension=".xgmml", filetypes=[('xgmml (graph file)', '*.xgmml')])

        if self.folderOutput != "" and self.AttToAdd != []:
            self.QuestionNo01_Check.config(state=DISABLED)
            self.QuestionNo03_Check.config(state=DISABLED)
            self.Add_Btn.config(state=DISABLED)
            self.Remove_Btn.config(state=DISABLED)
            self.In_Btn.config(state=DISABLED)
            self.Out_Btn.config(state=DISABLED)
            self.RemoveAttribute_CBox.config(state=DISABLED)
            self.AddAttribute_CBox.config(state=DISABLED)

            MainApp.attributesToDelete = self.AttributesToDelete_Options
            
            self.preferenceFilter()
            self.edgeWriter()
            self.writeNewFile()

            self.QuestionNo01_Check.config(state=NORMAL)
            self.QuestionNo03_Check.config(state=NORMAL)
            self.Add_Btn.config(state=NORMAL)
            self.Remove_Btn.config(state=NORMAL)
            self.In_Btn.config(state=DISABLED)
            self.Out_Btn.config(state=NORMAL)
            self.RemoveAttribute_CBox.config(state='readonly')
            self.AddAttribute_CBox.config(state='readonly')
        
    def AttributeAdd(self):
        i = 0
        for each in self.AllAtts:
            if self.AllAtts[i] == self.AddAttribute_CBox.get():
                self.AttToAdd.append(self.AddAttribute_CBox.get())
                self.AllAtts.pop(i)
                self.AddAttribute_Options = sorted(self.AllAtts)
                self.AddAttribute_CBox.config(values=self.AddAttribute_Options, state='normal')
                self.AddAttribute_CBox.delete(0, "")
                if self.AllAtts != []:
                    self.AddAttribute_CBox.insert(0, self.AddAttribute_Options[0])
                else:
                    self.AddAttribute_CBox.insert(0, "")
                self.AddAttribute_CBox.config(state='readonly')

                self.RemoveAttribute_Options = sorted(self.AttToAdd)
                self.RemoveAttribute_CBox.config(values=self.RemoveAttribute_Options, state='normal')
                self.RemoveAttribute_CBox.delete(0, "")
                if self.AttToAdd != []:
                    self.RemoveAttribute_CBox.insert(0, self.RemoveAttribute_Options[0])
                else:
                    self.RemoveAttribute_CBox.insert(0, "")
                self.RemoveAttribute_CBox.config(state='readonly')
                break
            i = i + 1
        MainApp.uniqueAttributes = self.AttToAdd
        self.Out_Btn.config(state=NORMAL)

    def DeleteAttribute(self):
        i = 0
        for each in self.AllAtts:
            if self.AllAtts[i] == self.AddAttribute_CBox.get():
                self.AttToDel.append(self.AddAttribute_CBox.get())
                self.AllAtts.pop(i)
                self.AddAttribute_Options = sorted(self.AllAtts)
                self.AddAttribute_CBox.config(values=self.AddAttribute_Options, state='normal')
                self.AddAttribute_CBox.delete(0, "")
                if self.AllAtts != []:
                    self.AddAttribute_CBox.insert(0, self.AddAttribute_Options[0])
                else:
                    self.AddAttribute_CBox.insert(0, "")
                self.AddAttribute_CBox.config(state='readonly')

                self.AttributesToDelete_Options = sorted(self.AttToDel)
                self.AttributesToDelete_CBox.config(values=self.AttributesToDelete_Options, state='normal')
                self.AttributesToDelete_CBox.delete(0, "")
                if self.AttToDel != []:
                    self.AttributesToDelete_CBox.insert(0, self.AttributesToDelete_Options[0])
                else:
                    self.AttributesToDelete_CBox.insert(0, "")
                self.AttributesToDelete_CBox.config(state='readonly')
                break
            i = i + 1
        MainApp.attributesToDelete = self.AttToDel
        self.Out_Btn.config(state=NORMAL)

    def ClearAttSelection(self):

        for each in self.AttToAdd:
            self.AllAtts.append(each)

        for each in self.AttToDel:
            self.AllAtts.append(each)

        self.AttToAdd = []
        self.RemoveAttribute_Options = self.AttToAdd
        self.RemoveAttribute_CBox.config(values=self.RemoveAttribute_Options, state='normal')
        self.RemoveAttribute_CBox.delete(0, "")
        self.RemoveAttribute_CBox.config(state='readonly')

        self.AttToDel = []
        self.AttributesToDelete_Options = self.AttToDel
        self.AttributesToDelete_CBox.config(values=self.AttributesToDelete_Options, state='normal')
        self.AttributesToDelete_CBox.delete(0, "")
        self.AttributesToDelete_CBox.config(state='readonly')

        self.AllAtts.sort()
        self.AddAttribute_Options = self.AllAtts
        self.AddAttribute_CBox.config(values=self.AddAttribute_Options, state='normal')
        self.AddAttribute_CBox.delete(0, "")
        self.AddAttribute_CBox.insert(0, self.AddAttribute_Options[0])
        self.AddAttribute_CBox.config(state='readonly')

        MainApp.attributesToDelete = []
        MainApp.uniqueAttributes = []
            
        if self.RemoveAttribute_Options != []:
            self.Out_Btn.config(state=NORMAL)
        else:
            self.Out_Btn.config(state=DISABLED)

if __name__ == "__main__":

    root = tk.Tk()
    MainApp(root)
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    img = PhotoImage(data=iconData)
    root.tk.call('wm', 'iconphoto', root._w, img)

    def on_closing():
        root.destroy()
                
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()


