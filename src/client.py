#!/usr/bin/python

import time
import datetime
import dcs_opc_ua
from pyuaf.util             import opcuastatuscodes, DateTime
import re
import sys
import argparse

parser = argparse.ArgumentParser(description='Production of FEAST calibration parameters per Micromegas sector')

parser.add_argument("-sector", "--sector", type=str, 
   help="Insert Sector side and number  e.g. A12,C01,..")
args = vars(parser.parse_args())

if not(re.compile("(A|C)(0[1-9]|1[0-6])").match(args['sector'])):
  print("********   Wrong Sector ID | Please provide a valid sector ID: A01-16 or C01-16   ******** ")
  sys.exit()

sector=args['sector'] 

dcs_opc_ua.connect()

location='BB5'
boardListFile = open('sectorDB_MMG/'+sector+'/boards_elink_'+sector+'_'+location+'.txt','r')

mmfe8File=open('sectorDB_MMG/'+sector+'/MMFE8_FEAST_CALIBRATION_'+sector+'.txt','w+')
l1ddcFile=open('sectorDB_MMG/'+sector+'/L1DDC_FEAST_CALIBRATION_'+sector+'.txt','w+')
addcFile=open('sectorDB_MMG/'+sector+'/ADDC_FEAST_CALIBRATION_'+sector+'.txt','w+')

numberOfBoards=str(len(open('sectorDB_MMG/'+sector+'/boards_elink_'+sector+'_'+location+'.txt').readlines()))

print "---> Looping over the "+numberOfBoards+" boards of Micromegas Sector "+sector

for i,board in enumerate(boardListFile):
    boardName=board.split()[0]
    if(re.compile("MMFE8").match(board)):
      pTat1V2D=dcs_opc_ua.read ([dcs_opc_ua.addr(boardName+'.ai.pTat1V2D.value')])
      pTat1V3A=dcs_opc_ua.read ([dcs_opc_ua.addr(boardName+'.ai.pTat1V3A.value')])
      pTat1V3AE=dcs_opc_ua.read ([dcs_opc_ua.addr(boardName+'.ai.pTat1V3AE.value')])
      feast1V2DValue = float(str(pTat1V2D.targets[0].data))
      feast1V3Value = float(str(pTat1V3A.targets[0].data))
      feast1V3EValue = float(str(pTat1V3AE.targets[0].data))
      internalTemperature=dcs_opc_ua.read ([dcs_opc_ua.addr(boardName+'.ai.internalTemperature.temperature')])
      scaTemp = float(str(internalTemperature.targets[0].data))   
      mmfe8File.write("%s %4.7f %4.7f %4.7f \n" % (boardName,feast1V2DValue*1000.0-8.43*(scaTemp-25.0),feast1V3Value*1000.0-8.43*(scaTemp-25.0),feast1V3EValue*1000.0-8.43*(scaTemp-25.0)))    
    if(re.compile("ADDC").match(board)):
      feastTemp1v5 = dcs_opc_ua.read ([dcs_opc_ua.addr(boardName+'.ai.feastTemp1v5.value')])
      feastTemp2v5=dcs_opc_ua.read ([dcs_opc_ua.addr(boardName+'.ai.feastTemp2v5.value')])
      feast1V5ValueADDC = float(str(feastTemp1v5.targets[0].data))
      feast2V5ValueADDC = float(str(feastTemp2v5.targets[0].data))
      internalTemperature=dcs_opc_ua.read ([dcs_opc_ua.addr(boardName+'.ai.internalTemperature.temperature')])
      scaTemp = float(str(internalTemperature.targets[0].data))
      addcFile.write("%s %4.7f %4.7f \n" % (boardName,feast1V5ValueADDC*1000.0-8.43*(scaTemp-25.0),feast2V5ValueADDC*1000.0-8.43*(scaTemp-25.0))); 
    if(re.compile("L1DDC").match(board)):
      pTat1V5 = dcs_opc_ua.read([dcs_opc_ua.addr(boardName+'.ai.1V5_PTAT.value')])
      pTat2V5 = dcs_opc_ua.read([dcs_opc_ua.addr(boardName+'.ai.2V5_PTAT.value')])
      feast1V5ValueL1DDC = float(str(pTat1V5.targets[0].data))
      feast2V5ValueL1DDC = float(str(pTat2V5.targets[0].data))
      internalTemperature=dcs_opc_ua.read ([dcs_opc_ua.addr(boardName+'.ai.internalTemperature.temperature')])
      scaTemp = float(str(internalTemperature.targets[0].data))
      l1ddcFile.write("%s %4.7f %4.7f \n" % (boardName,feast1V5ValueL1DDC*1000.0-8.43*(scaTemp-25.0),feast2V5ValueL1DDC*1000.0-8.43*(scaTemp-25.0))); 
    sys.stdout.write('\r')
    sys.stdout.write("[%-100s] %d%%" % ('='*int(101*i/160), 101*i/160))
    sys.stdout.flush()
    time.sleep(0.01)

boardListFile.close()
mmfe8File.close()
addcFile.close()
l1ddcFile.close()

print "\n"
print "** The FEAST calibration files for MMFE8, L1DDC and ADDC boards are ready! Have fun!"
