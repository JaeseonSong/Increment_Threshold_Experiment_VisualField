'''
This experiment was created using PsychoPy v.2021.2.3 for a monitor with an 85-Hz refresh rate and a screen resolution of 800 x 600. 
The monitor was calibrated using a Photo Research PR-650 Spectrophotometer, and the viewing distance was 70 cm.
Each observer was allocated pre-determined (psuedorandomized) experimental conditions (see VF_conds.py).
'''
from __future__ import division, print_function
from psychopy import visual, core, data, event, sound, logging, gui, prefs
from psychopy import monitors
from psychopy.visual import ShapeStim, Line, TextStim
from psychopy.constants import * #things like STARTED, FINISHED
from psychopy.preferences import prefs
import os #handy system and path functions
import sys
import csv
import math
from math import *
from builtins import next, range
import copy, time #from the std python libs
from psychopy.data import MultiStairHandler
import random
import VF_conds # Conditions for pulsed- and steady-pedestal paradigms

random.seed()
   
#logging.console.setLevel(logging.DEBUG)  # get messages about the sound lib as it loads

# To allow the participant to quit the experiment at any time by pressing the 'escape' key:
event.globalKeys.add(key='escape', func=core.quit) 

# Contrast was calculated using this equation: opacity*stimRGB + (1-opacity)*backgroundRGB


#============================= setup files for saving ===================================================#
expName='Sqr'
expInfo={'1. Participant Number':'','2. Nth Set':'','3. Nth Experiment':''}
dlg=gui.DlgFromDict(dictionary=expInfo,title=expName)

if dlg.OK==False: core.quit() #user pressed cancel
expInfo['date']=data.getDateStr()#add a simple timestamp
expInfo['expName']=expName

sbjIdx = str(expInfo['1. Participant Number'])
setIdx = str(expInfo['2. Nth Set'])
expIdx = str(expInfo['3. Nth Experiment'])
myDlg = gui.Dlg(title="Information check")
myDlg.addText('Is this information correct?')
myDlg.addText('Participant Number:'+ sbjIdx)
myDlg.addText('Nth Set:' + setIdx)
myDlg.addText('Nth Experiment:' + expIdx)

ok_data = myDlg.show()  # show dialog and wait for OK or Cancel
if myDlg.OK:  # or if ok_data is not None
    pass
else:
    print('user cancelled')
    core.quit()
   
#============================= Conditions ========================================#
Numframe = 3 # Test period (85HZ : 11.77 *3 frames = 35.31 ms)

OpColorR=(255,0,0); OpColorG=(0,103,0) 
# The pixel value of green was adjusted to match the maximum luminance level of red (31.721cd).

size = 1.6
lenSQR = size/2 # center of the square
bwSQR = 0.2 # distance between tangent point and a square

trialN = 40 # The maximum number of trials to be conducted should exceed the number of attempts typically taken in previous experiments..
adaptTime = 30 # Pre-adaptation period for the first trial of a block

beforebeep=3 # Pre-adaptation period for the rest trials of a block
BeepDur=0.2; afterbeep=0.3

Textheight = 0.6; Tcolor= 'black'; textPos=(0,1)
lineWid = 0.6  # Fixation

ThisExp=VF_conds.participants[int(sbjIdx)-1][int(setIdx)-1][int(expIdx)-1]
print(ThisExp)

color = ThisExp[0]        # color
PulsedSteady = ThisExp[1] # Pulsed or Steady
opac = ThisExp[2]         # contrast
posit = ThisExp[3]        # Position

# Random location of Target: Left or Right 
preLR=list(range(60)) 
random.shuffle(preLR)
TargRan=[];
for randomLR in preLR:
    #print(preLR[randomLR]%2)
    if preLR[randomLR]%2 == 0: #Target on Left
        TargRan.append([0,1])
    else: #Target on Right
        TargRan.append([1,0])
print(TargRan)

# =========== startVals for QUEST =========== #
if opac == VF_conds.c1: # 0
    startV = opac+0.06
elif opac == VF_conds.c2: # 0.08
    startV = opac+0.06
elif opac == VF_conds.c3: # 0.16
    startV = opac+0.07
elif opac == VF_conds.c4: # 0.32
    startV = opac+0.09
elif opac == VF_conds.c5: # 0.48
    startV = opac+0.1
elif opac == VF_conds.c6: # 0.64
    startV = 0.78

# ======= To print out the details of the current condition that the observer has started ===== #

if color == VF_conds.re:
    colorStr='R'
    colorfStr='Red'
elif color == VF_conds.gn:
    colorStr='G'
    colorfStr='Green'
if PulsedSteady == VF_conds.pulsed:
    pedStr='P'
    pedfStr='Pulsed'
elif PulsedSteady == VF_conds.steady:
    pedStr='S'
    pedfStr='Steady'
if posit==VF_conds.upperR:
    poStr='UR'
    pofStr='UpperRight'
elif posit==VF_conds.lowerL:
    poStr='LL'
    pofStr='LowerLeft'

def sum():
    print("="*20+" SUMMARY "+"="*21) 
    print("Participant number: %s" %sbjIdx)
    print("Set Number: %s" %setIdx)
    print("Experiment number: %s" %expIdx)
    print(colorfStr+', ', pedfStr+', ', pofStr+', ', "%0.2f" % opac)
    print("Start luminance value is: %s" %round(startV,2))
    print("="*50) 
sum()
#==============================================================

# Directory
if int(sbjIdx) == 1:
    Pdir = "P1"
elif int(sbjIdx) == 2:
    Pdir = "P2"
elif int(sbjIdx) == 3:
    Pdir = "P3"
elif int(sbjIdx) == 4:
    Pdir = "P4"
elif int(sbjIdx) == 5:
    Pdir = "P5"
elif int(sbjIdx) == 6:
    Pdir = "P6"
elif int(sbjIdx) == 7:
    Pdir = "P7"

if int(setIdx) == 1:
    Sdir = "Set1"
elif int(setIdx) == 2:
    Sdir = "Set2"
elif int(setIdx) == 3:
    Sdir = "Set3"

# Set parent directory path
# Change the path below to the folder of your choice
parent_dir = r"C:\Users\UserName\Desktop\Gabor_data"

# Create parent directory if it doesn't exist
if not os.path.exists(parent_dir + os.path.sep + Pdir):
    path = os.path.join(parent_dir, Pdir)
    os.makedirs(path) 
    
# Create subdirectory if it doesn't exist
if not os.path.exists(parent_dir + os.path.sep + Pdir+ os.path.sep + Sdir):
    path = parent_dir + os.path.sep + Pdir
    subpath= os.path.join(path, Sdir)
    os.makedirs(subpath)
    
# Generate file name based on experiment information
fileName = parent_dir+ os.path.sep + Pdir + os.path.sep + Sdir + os.path.sep + '%s_%s%0.2f_P%s_Set%s_Exp%s_%s' %(expName, colorStr+pedStr+poStr, opac, sbjIdx, setIdx, expIdx, expInfo['date'])
print(fileName)

# Create a text file to save data
dataFile = open(fileName+'.txt', 'w')

# Write experiment details to the file
dataFile.write('P%s-Set%s-Exp%s: ' '%s, %s, %s, %0.2f\n\n' 
    % (sbjIdx, setIdx, expIdx, colorfStr, pedfStr, pofStr, opac))
    
# Write column headers to the file
dataFile.write('trial\t' 'QuestV\t' 'resp\t' 'correct\n')

# Set global clock for timing
globalClock = core.Clock()

# =============== Create a window for displaying stimuli =============== #

#DON'T FORGET TO CHECK YOUR MONITOR SETTING
win = visual.Window(monitor='testMonitor', colorSpace='rgb255', color = color, allowGUI=False)

# Set parameters for recording frame intervals and dropped frames
win.recordFrameIntervals = True
win.refreshThreshold = 1/85 + 0.005

# Set logging level to warning and print number of dropped frames
logging.console.setLevel(logging.WARNING)
print('Overall, %i frames were dropped.' % win.nDroppedFrames)

# Create text stimuli for display in the window
afterAdapt = TextStim(win, text='Press the spacebar when you are ready \n\n'
    'to start to find your threshold.', colorSpace= "rgb255", height=Textheight, 
    pos=textPos, units='deg', color=Tcolor)
startText = TextStim(win, text='Adaptation for 30sec? \n\n\n' 
    '   <-- Yes / No-->' , 
    colorSpace= 'rgb255', pos=textPos, height=Textheight, units='deg', color=Tcolor)

#----------------------- Draw Fixation Guides ------------------------------------------#
Line1= Line(win, colorSpace='rgb255',start=(-0.5, 0), end=(0.5,0), 
    units= 'deg', lineWidth= lineWid, lineColor=(20,20,20), interpolate=True)
Line2= Line(win, colorSpace='rgb255',start=(0,-0.5), end=(0,0.5), 
    units= 'deg', lineWidth= lineWid, lineColor=(20,20,20), interpolate=True)
def Fixation():
    Line1.draw()
    Line2.draw()

#========================================== QUEST ==================================================================== #

quest = data.QuestHandler(startV, 0.05, pThreshold=0.7, ntrials=trialN, gamma=0.01, stopInterval=0.095, minVal=opac, maxVal=0.78)

#===================================================================================================================== #

# Calculate the locations of stimuli on a invisible circle with a radius of 3.6 degrees.
# The radius of the circle is perpendicular to the tangent point at the point of contact.
angle45=math.radians(45)
tanX= round(math.cos(angle45)*VF_conds.upperR, 2) # upperR = 3.6 = abs(lowerL)
tanY= round(math.sin(angle45)*VF_conds.upperR, 2)
#print(tanX,tanY)

# Calculate the Slope of the Tangent 
# It is perpendicular to the slope of radius = (tanY-0)/(tanX-0)
slopeT = round(-tanX/tanY, 2)
#print(slopeT)

# Find the equation of the tangent line through the point (tanX, tanY) on the circle.
# The equation of a line can be expressed as y = mx + b, where m is the slope and b is the y-intercept.
# The y-intercept can be found by plugging in the x and y values of the point.
# y=slopeT*x+b
b = round(tanY-slopeT*tanX, 2)
#print(b)

# Calculate the coordinates of the upper and lower points on the circle.
# The coordinates can be found using the slope-intercept form of the equation of the tangent line.
UpRx=round(math.sqrt(((bwSQR+lenSQR)**2)/2)+tanX, 2)
UpRy=round(-UpRx+b, 2)
UpLx=UpRy
UpLy=UpRx

LoLx=-UpRx
LoLy=-UpRy
LoRx=LoLy
LoRy=LoLx
#print(UpLx,UpLy,UpRx,UpRy)
#print(LoLx,LoLy,LoRx,LoRy)

#Determine the position of the stimulus.
#The position of the stimulus is determined by its location on the circle.
if posit == VF_conds.upperR:
    posH=[(UpLx,UpLy), (UpRx,UpRy)]
elif posit == VF_conds.lowerL:
    posH=[(LoLx,LoLy), (LoRx,LoRy)]
    
   
# Create two square stimuli with the given properties.
# The stimuli are positioned at posH[0] and posH[1] and are rotated by 45 degrees.

if color == VF_conds.re:
    SqrL = visual.Rect(win, size=size, pos=posH[0], ori=45,
        colorSpace="rgb255", fillColor=OpColorR, units = 'deg', lineWidth= 0) #Left
    SqrR = visual.Rect(win, size=size, pos=posH[1], ori=45,
        colorSpace="rgb255", fillColor=OpColorR, units = 'deg', lineWidth= 0) #Right
    # SqrLa is for steady paradigm 
    SqrLa = visual.Rect(win, size=size, colorSpace="rgb255", pos=posH[0],ori=45,
         opacity=opac, fillColor=OpColorR, units = 'deg', lineWidth= 0) #Left
    SqrRa = visual.Rect(win, size=size, colorSpace="rgb255", pos=posH[1],ori=45,
         opacity=opac, fillColor=OpColorR, units = 'deg', lineWidth= 0) #Right

elif color == VF_conds.gn:
    SqrL = visual.Rect(win, size=size, pos=posH[0],ori=45,
        colorSpace="rgb255", fillColor=OpColorG, units = 'deg', lineWidth= 0) #Left
    SqrR = visual.Rect(win, size=size, pos=posH[1],ori=45,
        colorSpace="rgb255", fillColor=OpColorG, units = 'deg', lineWidth= 0) #Right
    # SqrLa is for steady paradigm 
    SqrLa = visual.Rect(win, size=size, colorSpace="rgb255", pos=posH[0],ori=45,
        opacity=opac, fillColor=OpColorG, units = 'deg', lineWidth= 0) #Left
    SqrRa = visual.Rect(win, size=size, colorSpace="rgb255", pos=posH[1],ori=45,
        opacity=opac, fillColor=OpColorG, units = 'deg', lineWidth= 0) #Right
    
#--------------------------< Start Experiment >--------------------------------#
event.Mouse(visible=False, newPos=None, win=None)
trial = 0; trialDesign  = []; responses = ['left', 'right']
response = 0; correct= 0

def MMM():
    """
    Calculates the mean, mode, and median of a given set of data.

    Returns:
    bool: A Boolean value indicating whether the data has been successfully written to a file.
    """
    Mean=quest.mean()
    Mode=quest.mode()
    Median=quest.quantile(0.5)  # gets the median
    mmm=[round(Mean, 3), round(Mode, 3), round(Median,3)]
    
    # Ensure that the calculated values are not less than a given opacity value.
    if Mean < opac:
        Mean = opac
    elif Mode < opac:
        Mode = opac
    elif  Median < opac:
        Median = opac
         
    # Print the mean value to the console.
    print("Threshold (mean): %0.3f" %Mean)
      
    # Add the calculated values to the data file.
    dataFile.write('Mean: %s\t Mode: %s\t Median: %s'% (mmm[0], mmm[1], mmm[2]))
    dataFile.flush()
    os.fsync(dataFile)
    written =True

def Beep():
    """
    Plays a high pitched beep sound and displays stimuli on the screen.

    If the platform is Windows, a fixation point is displayed on the screen.
    If the PulsedSteady variable is equal to Pedestal[1], two stimuli are displayed on the screen.
    Finally, a 'ding' sound is played and the screen is flipped.
    """
      
    # Create a high pitched beep sound.
    highA = sound.Sound('A', octave=5, sampleRate=44100, secs=BeepDur, stereo=True)
    highA.setVolume(0.6)
    highA.play()
      
    # Check if the platform is Windows.
    if sys.platform == 'win32':
        Fixation()
      
        # Display two stimuli on the screen if it is a steady-pedestal condition.
        if PulsedSteady == VF_conds.Pedestal[1]:
            SqrLa.draw()
            SqrRa.draw()
            
        # Play a 'ding' sound.
        ding = sound.Sound('ding')
        ding.play()
        win.flip()

def Mainloop():
    global trial, response, correct

    tarLR=TargRan[trial]
    TA=int(tarLR[0])
    TB=int(tarLR[1])
    
    T1=round(core.getTime(), 1)
    T2=round(core.getTime(), 1)
    while T2-T1 < beforebeep:
        T2=round(core.getTime(), 1)
        if PulsedSteady == VF_conds.Pedestal[1]:
            SqrLa.draw()
            SqrRa.draw()
        Fixation()
        win.flip() 
    
    Beep()
    
    if PulsedSteady == VF_conds.pulsed:
        SqrL.opacity=opacities[TA]
        SqrR.opacity=opacities[TB]
        T3=round(core.getTime(), 1)
        T4=round(core.getTime(), 1)
        while T4-T3 < afterbeep:
            T4=round(core.getTime(), 1)
            Fixation()
            win.flip() 
        for frameN in range(Numframe): #for exactly 'Numframe'
            Fixation()
            SqrL.draw()
            SqrR.draw()
            win.flip()
        Fixation()
        win.flip()
         
    elif PulsedSteady == VF_conds.steady:
        SqrL.opacity=opacities[TA]
        SqrR.opacity=opacities[TB]
        T3=round(core.getTime(), 1)
        T4=round(core.getTime(), 1)
        while T4-T3 < afterbeep:
            T4=round(core.getTime(), 1)
            Fixation()
            SqrLa.draw()
            SqrRa.draw()
            win.flip() 
        for frameN in range(Numframe): #for exactly 'Numframe'
            Fixation()
            SqrL.draw()
            SqrR.draw()
            win.flip()
        SqrLa.draw()
        SqrRa.draw()
        Fixation()
        win.flip()

    # wait for response
    keys = []
    while not keys:
        keys = event.waitKeys(keyList=['left', 'right'])
        #print(keys, GratingT.opacity, GratingB.opacity)
    # check if it's the correct response:
    if opacities[TA] > opacities[TB]: 
        #print("SqrL.opacity > SqrR.opacity")
        if responses[0] in keys:
            response = 0 #Left
            correct = 1
        else:
            response = 1 #Right
            correct = 0
    elif opacities[TB] > opacities[TA]:
        #print("SqrL.opacity < SqrR.opacity")
        if responses[1] in keys:
            response = 1 # Right
            correct = 1
        else:
            response = 0 # Left
            correct = 0
    elif opacities[TB] == opacities[TA]:
            correct = 0
    
    #print(T_Opacity, response, correct) 
    
    # inform QUEST of the response, needed to calculate next level
    quest.addResponse(correct)
    trial = trial+1
    trialDesign.append([trial])
    trialDesign[trial-1].append(T_Opacity)
    trialDesign[trial-1].append(response)
    trialDesign[trial-1].append(correct)
    
    line = '\t'.join(str(i) for i in trialDesign[trial-1])
    line += '\n'
    dataFile.write(line)
    dataFile.flush()
    os.fsync(dataFile)
    written =True
    
    event.clearEvents()
    Fixation()
    win.flip()
    event.waitKeys(keyList=['space'])
    win.flip()

def adapt():
    Fixation()
    win.flip()
    core.wait(adaptTime)
    win.flip()
    
startText.draw()
win.flip()
KL = event.waitKeys(keyList=['left', 'right']) #Yes/No
#print(KL)
if KL == ['left']:
    adapt()
elif KL == ['right']:
    pass

afterAdapt.draw()
win.flip()
event.waitKeys()
win.flip()

for thisOpacity in quest:
    T_Opacity=round(thisOpacity,4)
    opacities = [T_Opacity, opac]
    Mainloop()
win.close() #closes the window
sum()
print("Number of trials: %s" %(trial))
MMM()
print("P%s-Set%s-Exp%s completed" %(sbjIdx, setIdx, expIdx))
core.quit()
