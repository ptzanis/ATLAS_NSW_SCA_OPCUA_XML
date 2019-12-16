###################################################################################
# Developer: Polyneikis Tzanis (polyneikis.tzanis@cern.ch)
# Date 26/09/2019 : initial commit
# Date 22/10/2019 : Merge Normal/Calibration/Simulation
#                   Input arguments for boards selection
#                   Input arguments for mode selection
# Date 7/11/2019 :  Add Sector Input Argument
#					Add SCA OPC UA Server Host Input Argument
# Date 2/12/2019 :  Board/Elink per sector
# Date 6/12/2019 :  Add location argument e.g BB5/191/180
#					Arguements error handling
###################################################################################

# ----------------------  SCA templates -------------------------------------------------------

def templateL1DDC_ADDC_Uncalibrated():
	return """   
	 <SCA address="simple-netio://direct/%s.cern.ch/1234%s/1235%s/%s" name="%s" idConstraint="dont_care" supervised="true" recoveryActionScaStayedPowered="do_nothing" recoveryActionScaWasRepowered="reset_and_configure" managementFromAddressSpace="only_if_kaputt" >
	<CalculatedVariable name="constant_1V5" value="0.0" />
	<CalculatedVariable name="constant_2V5" value="0.0" />
        &SCA_%s;
    </SCA>
	"""
def templateMMFE8_Uncalibrated():
	return """   
	 <SCA address="simple-netio://direct/%s.cern.ch/1234%s/1235%s/%s" name="%s" idConstraint="dont_care" supervised="true" recoveryActionScaStayedPowered="do_nothing" recoveryActionScaWasRepowered="reset_and_configure" managementFromAddressSpace="only_if_kaputt" >
	<CalculatedVariable name="constant_1V2D" value="0.0" />
	<CalculatedVariable name="constant_1V3" value="0.0" />
	<CalculatedVariable name="constant_1V3E" value="0.0" />
        &SCA_%s;
    </SCA>
	"""
def templateL1DDC_ADDC_Calibrated():
	return """   
	 <SCA address="simple-netio://direct/%s.cern.ch/1234%s/1235%s/%s" name="%s" idConstraint="dont_care" supervised="true" recoveryActionScaStayedPowered="do_nothing" recoveryActionScaWasRepowered="reset_and_configure" managementFromAddressSpace="only_if_kaputt" >
	<CalculatedVariable name="constant_1V5" value="%s" />
	<CalculatedVariable name="constant_2V5" value="%s" />
        &SCA_%s;
    </SCA>
	"""
def templateMMFE8_Calibrated():
	return """   
	 <SCA address="simple-netio://direct/%s.cern.ch/1234%s/1235%s/%s" name="%s" idConstraint="dont_care" supervised="true" recoveryActionScaStayedPowered="do_nothing" recoveryActionScaWasRepowered="reset_and_configure" managementFromAddressSpace="only_if_kaputt" >
	<CalculatedVariable name="constant_1V2D" value="%s" />
	<CalculatedVariable name="constant_1V3" value="%s" />
	<CalculatedVariable name="constant_1V3E" value="%s" />
        &SCA_%s;
    </SCA>
	"""
def templateL1DDC_ADDC_Simulation():
	return """   
	 <SCA address="sca-simulator://%s" name="%s" idConstraint="dont_care" supervised="true" recoveryActionScaStayedPowered="do_nothing" recoveryActionScaWasRepowered="reset_and_configure" managementFromAddressSpace="only_if_kaputt" >
	<CalculatedVariable name="constant_1V5" value="0.0" />
	<CalculatedVariable name="constant_2V5" value="0.0" />
        &SCA_%s;
    </SCA>
	"""
def templateMMFE8_Simulation():
	return """   
	 <SCA address="sca-simulator://%s" name="%s" idConstraint="dont_care" supervised="true" recoveryActionScaStayedPowered="do_nothing" recoveryActionScaWasRepowered="reset_and_configure" managementFromAddressSpace="only_if_kaputt" >
	<CalculatedVariable name="constant_1V2D" value="0.0" />
	<CalculatedVariable name="constant_1V3" value="0.0" />
	<CalculatedVariable name="constant_1V3E" value="0.0" />
        &SCA_%s;
    </SCA>
	"""
# ----------------------  Function arguments -------------------------------------------------------

import argparse
import re
import sys

parser = argparse.ArgumentParser(description='Production of XML for SCA OPC UA Server per NSW sector')

parser.add_argument("-mode", "--mode", type=str, default="U",
   help="Choose mode: [U]ncalibration/[C]alibration/[S]imulation")
parser.add_argument("-sector", "--sector", type=str, 
   help="Insert Sector side and number  e.g. A12,C01,..")
parser.add_argument("-opcHost", "--opcHost", type=str, 
   help="Insert SCA OPC UA Server Host PC")
parser.add_argument("-location", "--location", type=str, 
   help="Insert SCA OPC UA Server location (BB5,191)")
parser.add_argument("-m", "--MMFE8", action='store_true',
   help="Enable MMFE8")
parser.add_argument("-l", "--L1DDC", action='store_true',
   help="Enable L1DDC")
parser.add_argument("-a", "--ADDC", action='store_true',
   help="Enable ADDC")
args = vars(parser.parse_args())

# ----------------------  Function arguments error handling -------------------------------------------------------

if not(re.compile("U|C|S").match(args['mode'])):
	print("********   Wrong Mode | Please provide a valid mode : U or C or S   ******** ")
	sys.exit()
if not(re.compile("(A|C)(0[1-9]|1[0-6])").match(args['sector'])):
	print("********   Wrong Sector ID | Please provide a valid sector ID: A01-16 or C01-16   ******** ")
	sys.exit()
if not(re.compile("BB5|191").match(args['location'])):
	print("********   Wrong Location | Please provide a valid location: BB5 or 191   ******** ")
	sys.exit()

# ----------------------  Selection Sector / FELIX machine -------------------------------------------------------

# Select Sector 
sector=args['sector'] 

# Select FELIX computer  
opcHost=args['opcHost'] 

# Select sector location  
location=args['location'] 

# ----------------------  Main Code -------------------------------------------------------

if(args['mode']=="U"):
   fileXML=open('sectorDB_MMG/'+sector+'/sector_'+sector+'_Uncalibration_MMG_'+location+'.xml',"w+")
if(args['mode']=="C"):
    fileXML=open('sectorDB_MMG/'+sector+'/sector_'+sector+'_Calibration_MMG_'+location+'.xml',"w+")
    feastL1DDCFile = open('sectorDB_MMG/'+sector+'/L1DDC_FEAST_CALIBRATION_'+sector+'.txt','r')
    feastMMFE8File = open('sectorDB_MMG/'+sector+'/MMFE8_FEAST_CALIBRATION_'+sector+'.txt','r')
    feastADDCFile  = open('sectorDB_MMG/'+sector+'/ADDC_FEAST_CALIBRATION_'+sector+'.txt','r')
		
    linesOffeastL1DDCFile=feastL1DDCFile.readlines()
    linesOffeastMMFE8File=feastMMFE8File.readlines()
    linesOffeastADDCFile=feastADDCFile.readlines()
    	
    boardL1DDC=[]
    constant_1V5_L1DDC=[]
    constant_2V5_L1DDC=[]
    
    boardADDC=[]
    constant_1V5_ADDC=[]
    constant_2V5_ADDC=[]
    
    boardMMFE8=[]
    constant_1V2D=[]
    constant_1V3=[]
    constant_1V3E=[]
    	
    for line in linesOffeastL1DDCFile:
       boardL1DDC.append(line.split()[0])
       constant_1V5_L1DDC.append(line.split()[1])
       constant_2V5_L1DDC.append(line.split()[2])   
    feastL1DDCFile.close()
    
    for line in linesOffeastMMFE8File:
       boardMMFE8.append(line.split()[0])
       constant_1V2D.append(line.split()[1])
       constant_1V3.append(line.split()[2])   
       constant_1V3E.append(line.split()[3])   
    feastMMFE8File.close()
    
    for line in linesOffeastADDCFile:
       boardADDC.append(line.split()[0])
       constant_1V5_ADDC.append(line.split()[1])
       constant_2V5_ADDC.append(line.split()[2])   
    feastADDCFile.close()
if(args['mode']=="S"):
   fileXML=open('sectorDB_MMG/'+sector+'/sector_'+sector+'_Simulation_MMG_'+location+'.xml',"w+")

elinksFile = open('sectorDB_MMG/'+sector+'/boards_elink_'+sector+'_'+location+'.txt','r')

linesOfElinksFile=elinksFile.readlines()

boards=[]
elinks=[]
for line in linesOfElinksFile:
   boards.append(line.split()[0])
   elinks.append(line.split()[1])
elinksFile.close()

fileXML.write("""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE configuration [
<!ENTITY SCA_L1DDC SYSTEM "SCA_L1DDC.xml">
<!ENTITY SCA_ADDC SYSTEM "SCA_ADDC.xml">
<!ENTITY SCA_MMFE8 SYSTEM "SCA_MMFE8.xml">
]>
<configuration xmlns="http://cern.ch/quasar/Configuration" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://cern.ch/quasar/Configuration Configuration.xsd ">
    <StandardMetaData>
        <Log>
            <GeneralLogLevel logLevel="INF"/>
        </Log>
    <SourceVariableThreadPool minThreads="0" maxThreads="100" maxJobs="10000"/>
    </StandardMetaData>
    <CalculatedVariableGenericFormula name="thermistorTemperature" formula="1/( 3.3540154*10^(-3)+(2.5627725*10^(-4)*log(1000*$thisObjectAddress.value/500))+(2.0829210*10^(-6)*(log(1000*$thisObjectAddress.value/500))^2)+(7.3003206*10^(-8)*(log(1000*$thisObjectAddress.value/500))^3)) -273.15"/>
    <CalculatedVariableGenericFormula name="scaTemperature" formula="(0.79-$thisObjectAddress.value)*545.454545455-40"/>
    <CalculatedVariableGenericFormula name="feastTemperature_1V3E" formula="($thisObjectAddress.value*1000-$parentObjectAddress(numLevelsUp=2).constant_1V3E )/8.43+25.0"/>
    <CalculatedVariableGenericFormula name="feastTemperature_1V2D" formula="($thisObjectAddress.value*1000-$parentObjectAddress(numLevelsUp=2).constant_1V2D )/8.43+25.0"/>
    <CalculatedVariableGenericFormula name="feastTemperature_1V3" formula="($thisObjectAddress.value*1000-$parentObjectAddress(numLevelsUp=2).constant_1V3 )/8.43+25.0"/>
    <CalculatedVariableGenericFormula name="feastTemperature_1V5" formula="($thisObjectAddress.value*1000-$parentObjectAddress(numLevelsUp=2).constant_1V5 )/8.43+25.0"/>
    <CalculatedVariableGenericFormula name="feastTemperature_2V5" formula="($thisObjectAddress.value*1000-$parentObjectAddress(numLevelsUp=2).constant_2V5 )/8.43+25.0"/>
    <CalculatedVariableGenericFormula name="vmmTemperature" formula="(725.0-(1.5*1000.0*$thisObjectAddress.value))/1.85"/>
    <CalculatedVariableGenericFormula name="rssiCurrentmA" formula="2.5-$thisObjectAddress.value"/>
    """)


mmmfe8Counter=addcCounter=l1ddcCounter=0
counter=0
felixDeviceId="0"

for board,elink in zip(boards,elinks):
    counter=counter+1
    if(location=="BB5" and re.compile("83f").match(elink)):
	  felixDeviceId="1"
    if(location=="191" and re.compile("9bf").match(elink)):
	  felixDeviceId="1"	  
    if(args['L1DDC']==True):
	  if(re.compile("L1DDC").match(board)):
	    l1ddcCounter=l1ddcCounter+1	
	    if(args['mode']=="U"):
	      fileXML.write(templateL1DDC_ADDC_Uncalibrated() % (opcHost,felixDeviceId,felixDeviceId,elink,board,"L1DDC"))
	    if(args['mode']=="C"):
	      fileXML.write(templateL1DDC_ADDC_Calibrated() % (opcHost,felixDeviceId,felixDeviceId,elink,board,constant_1V5_L1DDC[boardL1DDC.index(board)],constant_2V5_L1DDC[boardL1DDC.index(board)],"L1DDC"))
	    if(args['mode']=="S"):
	      fileXML.write(templateL1DDC_ADDC_Simulation() % (counter,board,"L1DDC"))
    if(args['ADDC']==True):
	  if(re.compile("ADDC").match(board)):
	    addcCounter=addcCounter+1	
	    if(args['mode']=="U"):
	      fileXML.write(templateL1DDC_ADDC_Uncalibrated() % (opcHost,felixDeviceId,felixDeviceId,elink,board,"ADDC"))
	    if(args['mode']=="C"):
	      fileXML.write(templateL1DDC_ADDC_Calibrated() % (opcHost,felixDeviceId,felixDeviceId,elink,board,constant_1V5_ADDC[boardADDC.index(board)],constant_2V5_ADDC[boardADDC.index(board)],"ADDC"))
	    if(args['mode']=="S"):
	      fileXML.write(templateL1DDC_ADDC_Simulation() % (counter,board,"ADDC"))		
    if(args['MMFE8']==True):
	  if(re.compile("MMFE8").match(board)):
	    mmmfe8Counter=mmmfe8Counter+1
	    if(args['mode']=="U"):
	      fileXML.write(templateMMFE8_Uncalibrated() % (opcHost,felixDeviceId,felixDeviceId,elink,board,"MMFE8"))
	    if(args['mode']=="C"):
	      fileXML.write(templateMMFE8_Calibrated() % (opcHost,felixDeviceId,felixDeviceId,elink,board,constant_1V2D[boardMMFE8.index(board)],constant_1V3[boardMMFE8.index(board)],constant_1V3E[boardMMFE8.index(board)],"MMFE8"))
	    if(args['mode']=="S"):
	      fileXML.write(templateMMFE8_Simulation() % (counter,board,"MMFE8"))		

fileXML.write("""
    <AdcSampler name="adcSamplerMechanism" maxNumberThreads="8" />

	</configuration>""")

print("********************************************************")

print("		Number of MMFE8 boards: "+str(mmmfe8Counter))
print("		Number of L1DDC boards: "+str(l1ddcCounter))
print("		Number of ADDC boards: "+str(addcCounter))

print("********************************************************")
print("*******        XML produced !!!!             ***********")
print("********************************************************")


fileXML.close()



# ----------------------  Create SCA XML Entities -------------------------------------------------------

fileSCA_MMFE8=open("SCA_MMFE8.xml","w+")
fileSCA_L1DDC=open("SCA_L1DDC.xml","w+")
fileSCA_ADDC=open("SCA_ADDC.xml","w+")



fileSCA_MMFE8.write("""
    <AnalogInputSystem generalRefreshRate="5" name="ai">
      <AnalogInput id="1" name="vmmPdo0">    <CalculatedVariable name="temperature" value="$applyGenericFormula(vmmTemperature)"  />  </AnalogInput>
      <AnalogInput id="2" name="vmmPdo1">    <CalculatedVariable name="temperature" value="$applyGenericFormula(vmmTemperature)"  />  </AnalogInput>
      <AnalogInput id="3" name="vmmPdo2">    <CalculatedVariable name="temperature" value="$applyGenericFormula(vmmTemperature)"  />  </AnalogInput>
      <AnalogInput id="4" name="vmmPdo3">    <CalculatedVariable name="temperature" value="$applyGenericFormula(vmmTemperature)"  />  </AnalogInput>
      <AnalogInput id="5" name="vmmPdo4">    <CalculatedVariable name="temperature" value="$applyGenericFormula(vmmTemperature)"  />  </AnalogInput>
      <AnalogInput id="6" name="vmmPdo5">    <CalculatedVariable name="temperature" value="$applyGenericFormula(vmmTemperature)"  />  </AnalogInput>
      <AnalogInput id="7" name="vmmPdo6">    <CalculatedVariable name="temperature" value="$applyGenericFormula(vmmTemperature)"  />  </AnalogInput>
      <AnalogInput id="8" name="vmmPdo7">    <CalculatedVariable name="temperature" value="$applyGenericFormula(vmmTemperature)"  />  </AnalogInput>
      <AnalogInput id="11" name="pTat1V3A">  <CalculatedVariable name="temperature" value="$applyGenericFormula(feastTemperature_1V3)" /> </AnalogInput>
      <AnalogInput id="12" name="pTat1V3AE"> <CalculatedVariable name="temperature" value="$applyGenericFormula(feastTemperature_1V3E)" /> </AnalogInput>
      <AnalogInput id="15" name="pTat1V2D">  <CalculatedVariable name="temperature" value="$applyGenericFormula(feastTemperature_1V2D)" /> </AnalogInput>
      <AnalogInput id="17" name="0V65for1V3A"> <CalculatedVariable name="power" value="$thisObjectAddress.value*2.0" />				      </AnalogInput>
      <AnalogInput id="18" name="0V65for1V3E"> <CalculatedVariable name="power" value="$thisObjectAddress.value*2.0" /> 			      </AnalogInput>
      <AnalogInput id="20" name="0V6for1V2D">  <CalculatedVariable name="power" value="$thisObjectAddress.value*2.0" />                               </AnalogInput>
      <AnalogInput id="31" name="internalTemperature"> <CalculatedVariable name="temperature" value="$applyGenericFormula(scaTemperature)" /> </AnalogInput>
    </AnalogInputSystem>
    <SpiSystem name="spi">
      <SpiSlave autoSsMode="true" busSpeed="20000000" lsbToMsb="false" name="vmm0" sampleAtFallingRxEdge="true" sampleAtFallingTxEdge="false" sclkIdleHigh="false" slaveId="0" toggleSs="true" transmissionSize="96"/>
      <SpiSlave autoSsMode="true" busSpeed="20000000" lsbToMsb="false" name="vmm1" sampleAtFallingRxEdge="true" sampleAtFallingTxEdge="false" sclkIdleHigh="false" slaveId="1" toggleSs="true" transmissionSize="96"/>
      <SpiSlave autoSsMode="true" busSpeed="20000000" lsbToMsb="false" name="vmm2" sampleAtFallingRxEdge="true" sampleAtFallingTxEdge="false" sclkIdleHigh="false" slaveId="2" toggleSs="true" transmissionSize="96"/>
      <SpiSlave autoSsMode="true" busSpeed="20000000" lsbToMsb="false" name="vmm3" sampleAtFallingRxEdge="true" sampleAtFallingTxEdge="false" sclkIdleHigh="false" slaveId="3" toggleSs="true" transmissionSize="96"/>
      <SpiSlave autoSsMode="true" busSpeed="20000000" lsbToMsb="false" name="vmm4" sampleAtFallingRxEdge="true" sampleAtFallingTxEdge="false" sclkIdleHigh="false" slaveId="4" toggleSs="true" transmissionSize="96"/>
      <SpiSlave autoSsMode="true" busSpeed="20000000" lsbToMsb="false" name="vmm5" sampleAtFallingRxEdge="true" sampleAtFallingTxEdge="false" sclkIdleHigh="false" slaveId="5" toggleSs="true" transmissionSize="96"/>
      <SpiSlave autoSsMode="true" busSpeed="20000000" lsbToMsb="false" name="vmm6" sampleAtFallingRxEdge="true" sampleAtFallingTxEdge="false" sclkIdleHigh="false" slaveId="6" toggleSs="true" transmissionSize="96"/>
      <SpiSlave autoSsMode="true" busSpeed="20000000" lsbToMsb="false" name="vmm7" sampleAtFallingRxEdge="true" sampleAtFallingTxEdge="false" sclkIdleHigh="false" slaveId="7" toggleSs="true" transmissionSize="96"/>
    </SpiSystem>
    <DigitalIOSystem name="gpio">
      <DigitalIO id="0" isInput="true" name="mmfe8Id0"/>
      <DigitalIO id="1" isInput="true" name="mmfe8Id1"/>
      <DigitalIO id="2" isInput="true" name="mmfe8Id2"/>
      <DigitalIO id="3" isInput="true" name="mmfe8Id3"/>
      <DigitalIO id="4" isInput="true" name="boardId"/>
      <DigitalIO id="5" isInput="true" name="sectorId"/>
      <DigitalIO id="6" isInput="true" name="panelId"/>
      <DigitalIO id="8" isInput="false" name="rocPllResetN"/>
      <DigitalIO id="9" isInput="false" name="rocSResetN"/>
      <DigitalIO id="10" isInput="false" name="rocCoreResetN"/>
      <DigitalIO id="11" isInput="true" name="rocPllRocLocked"/>
      <DigitalIO id="12" isInput="true" name="rocPllLocked"/>
      <DigitalIO id="13" isInput="true" name="rocSeu"/>
      <DigitalIO id="14" isInput="true" name="rocError"/>
      <DigitalIO id="15" isInput="true" name="transGate0"/>
      <DigitalIO id="16" isInput="true" name="transGate1"/>
      <DigitalIO id="17" isInput="true" name="rocCoreScl"/>
      <DigitalIO id="18" isInput="true" name="rocCoreSda"/>
      <DigitalIO id="19" isInput="true" name="rocPllScl"/>
      <DigitalIO id="20" isInput="true" name="rocPllSda"/>
    </DigitalIOSystem>
    <I2cMaster busSpeed="200" masterId="0" name="rocCoreDigital" sclPadCmosOutput="false">
      <I2cSlave address="0" addressingMode="10" name="reg000rocId" numberOfBytes="1"/>
      <I2cSlave address="1" addressingMode="10" name="reg001elinkSpeed" numberOfBytes="1"/>
      <I2cSlave address="2" addressingMode="10" name="reg002sRoc0VmmConnections" numberOfBytes="1"/>
      <I2cSlave address="3" addressingMode="10" name="reg003sRoc1VmmConnections" numberOfBytes="1"/>
      <I2cSlave address="4" addressingMode="10" name="reg004sRoc2VmmConnections" numberOfBytes="1"/>
      <I2cSlave address="5" addressingMode="10" name="reg005sRoc3VmmConnections" numberOfBytes="1"/>
      <I2cSlave address="6" addressingMode="10" name="reg006eopAndNullEventEnable" numberOfBytes="1"/>
      <I2cSlave address="7" addressingMode="10" name="reg007sRocEnable" numberOfBytes="1"/>
      <I2cSlave address="8" addressingMode="10" name="reg008vmmEnable" numberOfBytes="1"/>
      <I2cSlave address="9" addressingMode="10" name="reg009timeout" numberOfBytes="1"/>
      <I2cSlave address="10" addressingMode="10" name="reg010bcOffset0_txcSel" numberOfBytes="1"/>
      <I2cSlave address="11" addressingMode="10" name="reg011bcOffset1" numberOfBytes="1"/>
      <I2cSlave address="12" addressingMode="10" name="reg012bcRollover0" numberOfBytes="1"/>
      <I2cSlave address="13" addressingMode="10" name="reg013bcRollover1" numberOfBytes="1"/>
      <I2cSlave address="14" addressingMode="10" name="reg014eportEnable" numberOfBytes="1"/>
      <I2cSlave address="19" addressingMode="10" name="reg019fakeVmmFailure" numberOfBytes="1"/>
      <I2cSlave address="20" addressingMode="10" name="reg020busyAndTdcEnable" numberOfBytes="1"/>
      <I2cSlave address="21" addressingMode="10" name="reg021busyOnLimit0" numberOfBytes="1"/>
      <I2cSlave address="22" addressingMode="10" name="reg022busyOnLimit1" numberOfBytes="1"/>
      <I2cSlave address="23" addressingMode="10" name="reg023busyOffLimit0" numberOfBytes="1"/>
      <I2cSlave address="24" addressingMode="10" name="reg024busyOffLimit1" numberOfBytes="1"/>
      <I2cSlave address="31" addressingMode="10" name="reg031l1EventsWithoutComma" numberOfBytes="1"/>
      <I2cSlave address="32" addressingMode="10" name="reg022vmmCapture0Status" numberOfBytes="1"/>
      <I2cSlave address="33" addressingMode="10" name="reg033vmmCapture1Status" numberOfBytes="1"/>
      <I2cSlave address="34" addressingMode="10" name="reg034vmmCapture2Status" numberOfBytes="1"/>
      <I2cSlave address="35" addressingMode="10" name="reg035vmmCapture3Status" numberOfBytes="1"/>
      <I2cSlave address="36" addressingMode="10" name="reg036vmmCapture4Status" numberOfBytes="1"/>
      <I2cSlave address="37" addressingMode="10" name="reg037vmmCapture5Status" numberOfBytes="1"/>
      <I2cSlave address="38" addressingMode="10" name="reg038vmmCapture6Status" numberOfBytes="1"/>
      <I2cSlave address="39" addressingMode="10" name="reg039vmmCapture7Status" numberOfBytes="1"/>
      <I2cSlave address="40" addressingMode="10" name="reg040sRoc0Status" numberOfBytes="1"/>
      <I2cSlave address="41" addressingMode="10" name="reg041sRoc1Status" numberOfBytes="1"/>
      <I2cSlave address="42" addressingMode="10" name="reg042sRoc2Status" numberOfBytes="1"/>
      <I2cSlave address="43" addressingMode="10" name="reg043sRoc3Status" numberOfBytes="1"/>
      <I2cSlave address="44" addressingMode="10" name="reg044seu" numberOfBytes="1"/>
      <I2cSlave address="45" addressingMode="10" name="reg045parityCounterVmm0" numberOfBytes="1"/>
      <I2cSlave address="46" addressingMode="10" name="reg046parityCounterVmm1" numberOfBytes="1"/>
      <I2cSlave address="47" addressingMode="10" name="reg047parityCounterVmm2" numberOfBytes="1"/>
      <I2cSlave address="48" addressingMode="10" name="reg048parityCounterVmm3" numberOfBytes="1"/>
      <I2cSlave address="49" addressingMode="10" name="reg049parityCounterVmm4" numberOfBytes="1"/>
      <I2cSlave address="50" addressingMode="10" name="reg050parityCounterVmm5" numberOfBytes="1"/>
      <I2cSlave address="51" addressingMode="10" name="reg051parityCounterVmm6" numberOfBytes="1"/>
      <I2cSlave address="52" addressingMode="10" name="reg052parityCounterVmm7" numberOfBytes="1"/>
      <I2cSlave address="53" addressingMode="10" name="reg053seuCounter" numberOfBytes="1"/>
      <I2cSlave address="63" addressingMode="10" name="reg063timeoutStatus" numberOfBytes="1"/>
    </I2cMaster>
    <I2cMaster busSpeed="200" masterId="1" name="rocPllCoreAnalog" sclPadCmosOutput="false">
      <I2cSlave address="64" addressingMode="10" name="reg064ePllVmm0" numberOfBytes="1"/>
      <I2cSlave address="65" addressingMode="10" name="reg065ePllVmm0" numberOfBytes="1"/>
      <I2cSlave address="66" addressingMode="10" name="reg066ePllVmm0" numberOfBytes="1"/>
      <I2cSlave address="67" addressingMode="10" name="reg067ePllVmm0" numberOfBytes="1"/>
      <I2cSlave address="68" addressingMode="10" name="reg068ePllVmm0" numberOfBytes="1"/>
      <I2cSlave address="69" addressingMode="10" name="reg069ePllVmm0" numberOfBytes="1"/>
      <I2cSlave address="70" addressingMode="10" name="reg070ePllVmm0" numberOfBytes="1"/>
      <I2cSlave address="71" addressingMode="10" name="reg071ePllVmm0" numberOfBytes="1"/>
      <I2cSlave address="72" addressingMode="10" name="reg072ePllVmm0" numberOfBytes="1"/>
      <I2cSlave address="73" addressingMode="10" name="reg073ePllVmm0" numberOfBytes="1"/>
      <I2cSlave address="74" addressingMode="10" name="reg074ePllVmm0" numberOfBytes="1"/>
      <I2cSlave address="75" addressingMode="10" name="reg075ePllVmm0" numberOfBytes="1"/>
      <I2cSlave address="76" addressingMode="10" name="reg076ePllVmm0" numberOfBytes="1"/>
      <I2cSlave address="77" addressingMode="10" name="reg077ePllVmm0" numberOfBytes="1"/>
      <I2cSlave address="78" addressingMode="10" name="reg078ePllVmm0" numberOfBytes="1"/>
      <I2cSlave address="79" addressingMode="10" name="reg079ePllVmm0" numberOfBytes="1"/>
      <I2cSlave address="80" addressingMode="10" name="reg080ePllVmm1" numberOfBytes="1"/>
      <I2cSlave address="81" addressingMode="10" name="reg081ePllVmm1" numberOfBytes="1"/>
      <I2cSlave address="82" addressingMode="10" name="reg082ePllVmm1" numberOfBytes="1"/>
      <I2cSlave address="83" addressingMode="10" name="reg083ePllVmm1" numberOfBytes="1"/>
      <I2cSlave address="84" addressingMode="10" name="reg084ePllVmm1" numberOfBytes="1"/>
      <I2cSlave address="85" addressingMode="10" name="reg085ePllVmm1" numberOfBytes="1"/>
      <I2cSlave address="86" addressingMode="10" name="reg086ePllVmm1" numberOfBytes="1"/>
      <I2cSlave address="87" addressingMode="10" name="reg087ePllVmm1" numberOfBytes="1"/>
      <I2cSlave address="88" addressingMode="10" name="reg088ePllVmm1" numberOfBytes="1"/>
      <I2cSlave address="89" addressingMode="10" name="reg089ePllVmm1" numberOfBytes="1"/>
      <I2cSlave address="90" addressingMode="10" name="reg090ePllVmm1" numberOfBytes="1"/>
      <I2cSlave address="91" addressingMode="10" name="reg091ePllVmm1" numberOfBytes="1"/>
      <I2cSlave address="92" addressingMode="10" name="reg092ePllVmm1" numberOfBytes="1"/>
      <I2cSlave address="93" addressingMode="10" name="reg093ePllVmm1" numberOfBytes="1"/>
      <I2cSlave address="94" addressingMode="10" name="reg094ePllVmm1" numberOfBytes="1"/>
      <I2cSlave address="95" addressingMode="10" name="reg095ePllVmm1" numberOfBytes="1"/>
      <I2cSlave address="96" addressingMode="10" name="reg096ePllTdc" numberOfBytes="1"/>
      <I2cSlave address="97" addressingMode="10" name="reg097ePllTdc" numberOfBytes="1"/>
      <I2cSlave address="98" addressingMode="10" name="reg098ePllTdc" numberOfBytes="1"/>
      <I2cSlave address="99" addressingMode="10" name="reg099ePllTdc" numberOfBytes="1"/>
      <I2cSlave address="100" addressingMode="10" name="reg100ePllTdc" numberOfBytes="1"/>
      <I2cSlave address="101" addressingMode="10" name="reg101ePllTdc" numberOfBytes="1"/>
      <I2cSlave address="102" addressingMode="10" name="reg102ePllTdc" numberOfBytes="1"/>
      <I2cSlave address="103" addressingMode="10" name="reg103ePllTdc" numberOfBytes="1"/>
      <I2cSlave address="104" addressingMode="10" name="reg104ePllTdc" numberOfBytes="1"/>
      <I2cSlave address="105" addressingMode="10" name="reg105ePllTdc" numberOfBytes="1"/>
      <I2cSlave address="106" addressingMode="10" name="reg106ePllTdc" numberOfBytes="1"/>
      <I2cSlave address="107" addressingMode="10" name="reg107ePllTdc" numberOfBytes="1"/>
      <I2cSlave address="108" addressingMode="10" name="reg108ePllTdc" numberOfBytes="1"/>
      <I2cSlave address="109" addressingMode="10" name="reg109ePllTdc" numberOfBytes="1"/>
      <I2cSlave address="110" addressingMode="10" name="reg110ePllTdc" numberOfBytes="1"/>
      <I2cSlave address="111" addressingMode="10" name="reg111ePllTdc" numberOfBytes="1"/>
      <I2cSlave address="112" addressingMode="10" name="reg112" numberOfBytes="1"/>
      <I2cSlave address="113" addressingMode="10" name="reg113" numberOfBytes="1"/>
      <I2cSlave address="114" addressingMode="10" name="reg114" numberOfBytes="1"/>
      <I2cSlave address="115" addressingMode="10" name="reg115" numberOfBytes="1"/>
      <I2cSlave address="116" addressingMode="10" name="reg116" numberOfBytes="1"/>
      <I2cSlave address="117" addressingMode="10" name="reg117" numberOfBytes="1"/>
      <I2cSlave address="118" addressingMode="10" name="reg118" numberOfBytes="1"/>
      <I2cSlave address="119" addressingMode="10" name="reg119" numberOfBytes="1"/>
      <I2cSlave address="120" addressingMode="10" name="reg120" numberOfBytes="1"/>
      <I2cSlave address="121" addressingMode="10" name="reg121vmmBcrInv" numberOfBytes="1"/>
      <I2cSlave address="122" addressingMode="10" name="reg122vmmEnaInv" numberOfBytes="1"/>
      <I2cSlave address="123" addressingMode="10" name="reg123vmmL0Inv" numberOfBytes="1"/>
      <I2cSlave address="124" addressingMode="10" name="reg124vmmTpInv" numberOfBytes="1"/>
    </I2cMaster>
	""")

fileSCA_L1DDC.write("""
    <AnalogInputSystem generalRefreshRate="5" name="ai">
      <AnalogInput id="0" name="GBTX1_TEMP" enableCurrentSource="true" > <CalculatedVariable name="temperature" value="$applyGenericFormula(thermistorTemperature)" /> </AnalogInput>
      <AnalogInput id="1" name="GBTX2_TEMP" enableCurrentSource="true" > <CalculatedVariable name="temperature" value="$applyGenericFormula(thermistorTemperature)" /> </AnalogInput>
      <AnalogInput id="2" name="GBTX3_TEMP" enableCurrentSource="true" > <CalculatedVariable name="temperature" value="$applyGenericFormula(thermistorTemperature)" /> </AnalogInput>
      <AnalogInput id="3" name="1V5_PTAT">                               <CalculatedVariable name="temperature" value="$applyGenericFormula(feastTemperature_1V5)" />  </AnalogInput>
      <AnalogInput id="4" name="2V5_PTAT"> 			      	 <CalculatedVariable name="temperature" value="$applyGenericFormula(feastTemperature_2V5)" />  </AnalogInput>
      <AnalogInput id="5" name="P1V5_SCA"> 				 <CalculatedVariable name="power" value="$thisObjectAddress.value*3.0" />                      </AnalogInput>
      <AnalogInput id="6" name="P2V5_SCA"> 				 <CalculatedVariable name="power" value="$thisObjectAddress.value*5.0" />		       </AnalogInput>
      <AnalogInput id="7" name="VTRX1_RSSI"> 				 <CalculatedVariable name="power" value="$applyGenericFormula(rssiCurrentmA)" /> 	       </AnalogInput>
      <AnalogInput id="31" name="internalTemperature">                    <CalculatedVariable name="temperature" value="$applyGenericFormula(scaTemperature)" />       </AnalogInput>
    </AnalogInputSystem>    
    <I2cMaster sclPadCmosOutput="false" name="gbtx2" masterId="0" busSpeed="100">
      <I2cSlave numberOfBytes="3" address="2" addressingMode="7" name="gbtx2"></I2cSlave>
    </I2cMaster>
    <I2cMaster sclPadCmosOutput="false" name="gbtx3" masterId="1" busSpeed="100">
      <I2cSlave numberOfBytes="3" address="3" addressingMode="7" name="gbtx3"></I2cSlave>
    </I2cMaster>
	""")


fileSCA_ADDC.write("""
	<AnalogInputSystem name="ai" generalRefreshRate="5">
	<AnalogInput id="0" name="1v5TP0"> <CalculatedVariable name="power" value="$thisObjectAddress.value*2.0" /> </AnalogInput>
	<AnalogInput id="1" name="1v5TP1"> <CalculatedVariable name="power" value="$thisObjectAddress.value*2.0" /> </AnalogInput>
	<AnalogInput id="2" name="2v5TP0"> <CalculatedVariable name="power" value="$thisObjectAddress.value*3.0" /> </AnalogInput>
	<AnalogInput id="3" name="2v5TP1"> <CalculatedVariable name="power" value="$thisObjectAddress.value*3.0" /> </AnalogInput>
        <AnalogInput id="24" name="boardTemp" enableCurrentSource="true" >    <CalculatedVariable name="temperature" value="$applyGenericFormula(thermistorTemperature)" /> </AnalogInput>	
        <AnalogInput id="26" name="feastTemp1v5"> <CalculatedVariable name="temperature" value="$applyGenericFormula(feastTemperature_1V5)" />  </AnalogInput>
        <AnalogInput id="27" name="feastTemp2v5"> <CalculatedVariable name="temperature" value="$applyGenericFormula(feastTemperature_2V5)" />  </AnalogInput>
 	<AnalogInput id="28" name="gbtx0NTC" enableCurrentSource="true" >  <CalculatedVariable name="temperature" value="$applyGenericFormula(thermistorTemperature)" /> </AnalogInput>			
        <AnalogInput id="29" name="gbtx1NTC" enableCurrentSource="true" >  <CalculatedVariable name="temperature" value="$applyGenericFormula(thermistorTemperature)" /> </AnalogInput>     	   
 	<AnalogInput id="31" name="internalTemperature">  <CalculatedVariable name="temperature" value="$applyGenericFormula(scaTemperature)" />           </AnalogInput>
	</AnalogInputSystem>

		<DigitalIOSystem name="gpio">
			<DigitalIO name="art0Rstn" isInput="false" id="1"></DigitalIO>
			<DigitalIO name="art0CRstn" isInput="false" id="2"></DigitalIO>
			<DigitalIO name="art0SRstn" isInput="false" id="3"></DigitalIO>
			<DigitalIO name="art1Rstn" isInput="false" id="4"></DigitalIO>
			<DigitalIO name="art1CRstn" isInput="false" id="5"></DigitalIO>
			<DigitalIO name="art1SRstn" isInput="false" id="6"></DigitalIO>
			<DigitalIO name="gbtx0Rstn" isInput="false" id="7"></DigitalIO>
			<DigitalIO name="gbtx1Rstn" isInput="false" id="8"></DigitalIO>
			<DigitalIO name="gbtx0Rdy" isInput="true" id="10"></DigitalIO>
			<DigitalIO name="gbtx1Rdy" isInput="true" id="11"></DigitalIO>
			<DigitalIO name="art0DllLocked" isInput="true" id="16"></DigitalIO>
			<DigitalIO name="art0TtcErr" isInput="true" id="17"></DigitalIO>
			<DigitalIO name="art0SeuErr" isInput="true" id="18"></DigitalIO>
			<DigitalIO name="art1DllLocked" isInput="true" id="19"></DigitalIO>
			<DigitalIO name="art1TtcErr" isInput="true" id="20"></DigitalIO>
			<DigitalIO name="art1SeuErr" isInput="true" id="21"></DigitalIO>
			<DigitalIO name="gbtx0EfuseProgPulseSca" isInput="false" id="24"></DigitalIO>
			<DigitalIO name="gbtx1EfuseProgPulseSca" isInput="false" id="25"></DigitalIO>
			<DigitalIO name="feast25vPwrGood" isInput="true" id="26"></DigitalIO>
		</DigitalIOSystem>
		
		<I2cMaster sclPadCmosOutput="false" name="gbtx0" masterId="0" busSpeed="100">
			<I2cSlave numberOfBytes="3" address="1" addressingMode="7" name="gbtx0"></I2cSlave>
		</I2cMaster>
		<I2cMaster sclPadCmosOutput="false" name="gbtx1" masterId="1" busSpeed="100">
			<I2cSlave numberOfBytes="3" address="2" addressingMode="7" name="gbtx1"></I2cSlave>
		</I2cMaster>
		<I2cMaster sclPadCmosOutput="false" name="art0Ps" masterId="4" busSpeed="100">
			<I2cSlave numberOfBytes="2" address="24" addressingMode="7" name="art0Ps"></I2cSlave>
		</I2cMaster>
		<I2cMaster sclPadCmosOutput="false" name="art0Core" masterId="4" busSpeed="100">
			<I2cSlave numberOfBytes="2" address="16" addressingMode="7" name="art0Core"></I2cSlave>
		</I2cMaster>
		<I2cMaster sclPadCmosOutput="false" name="art1Ps" masterId="6" busSpeed="100">
			<I2cSlave numberOfBytes="2" address="24" addressingMode="7" name="art1Ps"></I2cSlave>
		</I2cMaster>
		<I2cMaster sclPadCmosOutput="false" name="art1Core" masterId="6" busSpeed="100">
			<I2cSlave numberOfBytes="2" address="16" addressingMode="7" name="art1Core"></I2cSlave>
		</I2cMaster>
	""")




fileSCA_MMFE8.close()
fileSCA_L1DDC.close()
fileSCA_ADDC.close()
