###################################################################################
# Developer: Polyneikis Tzanis (polyneikis.tzanis@cern.ch)
# Date 12/12/2019 : initial commit for STG
###################################################################################

# ----------------------  SCA templates -------------------------------------------------------

def templateSFEB_PFEB_PADTRIGGER_Uncalibrated():
	return """   
	 <SCA address="simple-netio://direct/%s.cern.ch/1234%s/1235%s/%s" name="%s" idConstraint="dont_care" supervised="true" recoveryActionScaStayedPowered="do_nothing" recoveryActionScaWasRepowered="reset_and_configure" managementFromAddressSpace="only_if_kaputt" >
        &SCA_%s;
    </SCA>
	"""
def templateL1DDC_RIML1DDC1_RIML1DDC2_Uncalibrated():
	return """   
	 <SCA address="simple-netio://direct/%s.cern.ch/1234%s/1235%s/%s" name="%s" idConstraint="dont_care" supervised="true" recoveryActionScaStayedPowered="do_nothing" recoveryActionScaWasRepowered="reset_and_configure" managementFromAddressSpace="only_if_kaputt" >
	<CalculatedVariable name="constant_1V5" value="0.0" />
	<CalculatedVariable name="constant_2V5" value="0.0" />     
        &SCA_%s;
    </SCA>
	"""
def templateROUTER_Uncalibrated():
	return """   
	 <SCA address="simple-netio://direct/%s.cern.ch/1234%s/1235%s/%s" name="%s" idConstraint="dont_care" supervised="true" recoveryActionScaStayedPowered="do_nothing" recoveryActionScaWasRepowered="reset_and_configure" managementFromAddressSpace="only_if_kaputt" >
	<CalculatedVariable name="constant_feastVccIntTemp" value="0.0" />
	<CalculatedVariable name="constant_feastMgtVccTemp" value="0.0" /> 
	<CalculatedVariable name="constant_feastAuxTemp" value="0.0" /> 
	<CalculatedVariable name="constant_feastMgtVttTemp" value="0.0" />
	<CalculatedVariable name="constant_feastVcc2V5Temp" value="0.0" /> 
	<CalculatedVariable name="constant_feastVcc3V3Temp" value="0.0" />
	<CalculatedVariable name="constant_feastVcc1V5Temp" value="0.0" /> 	
	    &SCA_%s;
    </SCA>
	"""	
def templateSFEB_PFEB_PADTRIGGER_Simulation():
	return """   
	 <SCA address="sca-simulator://%s" name="%s" idConstraint="dont_care" supervised="true" recoveryActionScaStayedPowered="do_nothing" recoveryActionScaWasRepowered="reset_and_configure" managementFromAddressSpace="only_if_kaputt" >
        &SCA_%s;
    </SCA>
	"""
def templateL1DDC_RIML1DDC1_RIML1DDC2_Simulation():
	return """   
	 <SCA address="sca-simulator://%s" name="%s" idConstraint="dont_care" supervised="true" recoveryActionScaStayedPowered="do_nothing" recoveryActionScaWasRepowered="reset_and_configure" managementFromAddressSpace="only_if_kaputt" >
	 <CalculatedVariable name="constant_1V5" value="0.0" />
	 <CalculatedVariable name="constant_2V5" value="0.0" />     
        &SCA_%s;
    </SCA>
	"""	
def templateROUTER_Simulation():
	return """   
	 <SCA address="sca-simulator://%s" name="%s" idConstraint="dont_care" supervised="true" recoveryActionScaStayedPowered="do_nothing" recoveryActionScaWasRepowered="reset_and_configure" managementFromAddressSpace="only_if_kaputt" >
    <CalculatedVariable name="constant_feastVccIntTemp" value="0.0" />
	<CalculatedVariable name="constant_feastMgtVccTemp" value="0.0" /> 
	<CalculatedVariable name="constant_feastAuxTemp" value="0.0" /> 
	<CalculatedVariable name="constant_feastMgtVttTemp" value="0.0" />
	<CalculatedVariable name="constant_feastVcc2V5Temp" value="0.0" /> 
	<CalculatedVariable name="constant_feastVcc3V3Temp" value="0.0" />
	<CalculatedVariable name="constant_feastVcc1V5Temp" value="0.0" /> 	
        &SCA_%s;
    </SCA>
	"""
# ----------------------  Function arguments -------------------------------------------------------

import argparse
import re
import sys

parser = argparse.ArgumentParser(description='Production of XML for SCA OPC UA Server per NSW STG sector')

parser.add_argument("-mode", "--mode", type=str, default="U",
   help="Choose mode: [U]ncalibration/[S]imulation")
parser.add_argument("-sector", "--sector", type=str, 
   help="Insert Sector side and number  e.g. A12,C01,..")
parser.add_argument("-opcHost", "--opcHost", type=str, 
   help="Insert SCA OPC UA Server Host PC")
parser.add_argument("-location", "--location", type=str, 
   help="Insert SCA OPC UA Server location (180,191)")
parser.add_argument("-s", "--SFEB", action='store_true',
   help="Enable SFEB")
parser.add_argument("-p", "--PFEB", action='store_true',
   help="Enable PFEB")
parser.add_argument("-l", "--L1DDC", action='store_true',
   help="Enable L1DDC")
parser.add_argument("-rl1", "--RIML1DDC1", action='store_true',
   help="Enable RIML1DDC1")
parser.add_argument("-rl2", "--RIML1DDC2", action='store_true',
   help="Enable RIML1DDC2")
parser.add_argument("-r", "--ROUTER", action='store_true',
   help="Enable ROUTER")
parser.add_argument("-pad", "--PADTRIGGER", action='store_true',
   help="Enable PAD TRIGGER")
args = vars(parser.parse_args())	

# ----------------------  Function arguments error handling -------------------------------------------------------

if not(re.compile("U|S").match(args['mode'])):
	print("********   Wrong Mode | Please provide a valid mode : U or S   ******** ")
	sys.exit()
if not(re.compile("(A|C)(0[1-9]|1[0-6])").match(args['sector'])):
	print("********   Wrong Sector ID | Please provide a valid sector ID: A01-16 or C01-16   ******** ")
	sys.exit()
if not(re.compile("180|191").match(args['location'])):
	print("********   Wrong Location | Please provide a valid location: 180 or 191   ******** ")
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
   fileXML=open('sectorDB_STG/'+sector+'/sector_'+sector+'_Uncalibration_STG_'+location+'.xml',"w+")

if(args['mode']=="S"):
   fileXML=open('sectorDB_STG/'+sector+'/sector_'+sector+'_Simulation_STG_'+location+'.xml',"w+")


elinksFile = open('sectorDB_STG/'+sector+'/boards_elink_'+sector+'_'+location+'.txt','r')

linesOfElinksFile=elinksFile.readlines()

boards=[]
elinks=[]
for line in linesOfElinksFile:
   boards.append(line.split()[0])
   elinks.append(line.split()[1])
elinksFile.close()

fileXML.write("""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE configuration [
<!ENTITY SCA_SFEB SYSTEM "SCA_SFEB.xml">
<!ENTITY SCA_PFEB SYSTEM "SCA_PFEB.xml">
<!ENTITY SCA_L1DDC SYSTEM "SCA_L1DDC.xml">
<!ENTITY SCA_PADTRIGGER SYSTEM "SCA_PADTRIGGER.xml">
<!ENTITY SCA_ROUTER SYSTEM "SCA_ROUTER.xml">
<!ENTITY SCA_RIML1DDC1 SYSTEM "SCA_RIML1DDC1.xml">
<!ENTITY SCA_RIML1DDC2 SYSTEM "SCA_RIML1DDC2.xml">

]>
<configuration xmlns="http://cern.ch/quasar/Configuration" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://cern.ch/quasar/Configuration Configuration.xsd ">
    <StandardMetaData>
        <Log>
            <GeneralLogLevel logLevel="INF"/>
        </Log>
    <SourceVariableThreadPool minThreads="0" maxThreads="100" maxJobs="10000"/>
    </StandardMetaData>
    <CalculatedVariableGenericFormula name="scaTemperature" formula="(0.79-$thisObjectAddress.value)*545.454545455-40"/>
    <CalculatedVariableGenericFormula name="vmmTemperature" formula="(725.0-(1000.0*$thisObjectAddress.value))/1.85"/>
    <CalculatedVariableGenericFormula name="rssiCurrentmA" formula="2.5-$thisObjectAddress.value"/>
    <CalculatedVariableGenericFormula name="thermistorTemperature" formula="1/( 3.3540154*10^(-3)+(2.5627725*10^(-4)*log(1000*$thisObjectAddress.value/500))+(2.0829210*10^(-6)*(log(1000*$thisObjectAddress.value/500))^2)+(7.3003206*10^(-8)*(log(1000*$thisObjectAddress.value/500))^3)) -273.15"/>
    <CalculatedVariableGenericFormula name="feastTemperature_1V5" formula="($thisObjectAddress.value*1000-$parentObjectAddress(numLevelsUp=2).constant_1V5 )/8.43+25.0"/>
    <CalculatedVariableGenericFormula name="feastTemperature_2V5" formula="($thisObjectAddress.value*1000-$parentObjectAddress(numLevelsUp=2).constant_2V5 )/8.43+25.0"/>

    <CalculatedVariableGenericFormula name="feastTemperature_VccInt" formula="($thisObjectAddress.value*1000-$parentObjectAddress(numLevelsUp=2).constant_feastVccIntTemp )/8.43+25.0"/>
    <CalculatedVariableGenericFormula name="feastTemperature_MgtVcc" formula="($thisObjectAddress.value*1000-$parentObjectAddress(numLevelsUp=2).constant_feastMgtVccTemp )/8.43+25.0"/>
    <CalculatedVariableGenericFormula name="feastTemperature_AuxTemp" formula="($thisObjectAddress.value*1000-$parentObjectAddress(numLevelsUp=2).constant_feastAuxTemp )/8.43+25.0"/>
    <CalculatedVariableGenericFormula name="feastTemperature_MgtVtt" formula="($thisObjectAddress.value*1000-$parentObjectAddress(numLevelsUp=2).constant_feastMgtVttTemp )/8.43+25.0"/>
    <CalculatedVariableGenericFormula name="feastTemperature_Vcc2V5" formula="($thisObjectAddress.value*1000-$parentObjectAddress(numLevelsUp=2).constant_feastVcc2V5Temp )/8.43+25.0"/>
    <CalculatedVariableGenericFormula name="feastTemperature_Vcc3V3" formula="($thisObjectAddress.value*1000-$parentObjectAddress(numLevelsUp=2).constant_feastVcc3V3Temp )/8.43+25.0"/>
    <CalculatedVariableGenericFormula name="feastTemperature_Vcc1V5" formula="($thisObjectAddress.value*1000-$parentObjectAddress(numLevelsUp=2).constant_feastVcc1V5Temp )/8.43+25.0"/>


    """)

sfebcounter=pfebcounter=l1ddccounter=riml1ddc1counter=riml1ddc2counter=padtriggercounter=routercounter=0
counter=0
felixDeviceId="0"

for board,elink in zip(boards,elinks):
    counter=counter+1
    if(re.compile("9bf").match(elink)):
	  felixDeviceId="1"
    if(args['SFEB']==True):
	  if(re.compile("SFEB").match(board)):
	    sfebcounter=sfebcounter+1	
	    if(args['mode']=="U"):
	      fileXML.write(templateSFEB_PFEB_PADTRIGGER_Uncalibrated() % (opcHost,felixDeviceId,felixDeviceId,elink,board,"SFEB"))
	    if(args['mode']=="S"):
	      fileXML.write(templateSFEB_PFEB_PADTRIGGER_Simulation() % (counter,board,"SFEB"))
    if(args['PFEB']==True):
	  if(re.compile("PFEB").match(board)):
	    pfebcounter=pfebcounter+1	
	    if(args['mode']=="U"):
	      fileXML.write(templateSFEB_PFEB_PADTRIGGER_Uncalibrated() % (opcHost,felixDeviceId,felixDeviceId,elink,board,"PFEB"))
	    if(args['mode']=="S"):
	      fileXML.write(templateSFEB_PFEB_PADTRIGGER_Simulation() % (counter,board,"PFEB"))		
    if(args['PADTRIGGER']==True):
	  if(re.compile("PADTRIGGER").match(board)):
	    padtriggercounter=padtriggercounter+1	
	    if(args['mode']=="U"):
	      fileXML.write(templateSFEB_PFEB_PADTRIGGER_Uncalibrated() % (opcHost,felixDeviceId,felixDeviceId,elink,board,"PADTRIGGER"))
	    if(args['mode']=="S"):
	      fileXML.write(templateSFEB_PFEB_PADTRIGGER_Simulation() % (counter,board,"PADTRIGGER"))	
    if(args['L1DDC']==True):
	  if(re.compile("L1DDC").match(board)):
	    l1ddccounter=l1ddccounter+1	
	    if(args['mode']=="U"):
	      fileXML.write(templateL1DDC_RIML1DDC1_RIML1DDC2_Uncalibrated() % (opcHost,felixDeviceId,felixDeviceId,elink,board,"L1DDC"))
	    if(args['mode']=="S"):
	      fileXML.write(templateL1DDC_RIML1DDC1_RIML1DDC2_Simulation() % (counter,board,"L1DDC"))	
    if(args['RIML1DDC1']==True):
	  if(re.compile("RIML1DDC1").match(board)):
	    riml1ddc1counter=riml1ddc1counter+1	
	    if(args['mode']=="U"):
	      fileXML.write(templateL1DDC_RIML1DDC1_RIML1DDC2_Uncalibrated() % (opcHost,felixDeviceId,felixDeviceId,elink,board,"RIML1DDC1"))
	    if(args['mode']=="S"):
	      fileXML.write(templateL1DDC_RIML1DDC1_RIML1DDC2_Simulation() % (counter,board,"RIML1DDC1"))
    if(args['RIML1DDC2']==True):
	  if(re.compile("RIML1DDC2").match(board)):
	    riml1ddc2counter=riml1ddc2counter+1	
	    if(args['mode']=="U"):
	      fileXML.write(templateL1DDC_RIML1DDC1_RIML1DDC2_Uncalibrated() % (opcHost,felixDeviceId,felixDeviceId,elink,board,"RIML1DDC2"))
	    if(args['mode']=="S"):
	      fileXML.write(templateL1DDC_RIML1DDC1_RIML1DDC2_Simulation() % (counter,board,"RIML1DDC2"))
    if(args['ROUTER']==True):
	  if(re.compile("ROUTER").match(board)):
	    routercounter=routercounter+1	
	    if(args['mode']=="U"):
	      fileXML.write(templateROUTER_Uncalibrated() % (opcHost,felixDeviceId,felixDeviceId,elink,board,"ROUTER"))
	    if(args['mode']=="S"):
	      fileXML.write(templateROUTER_Simulation() % (counter,board,"ROUTER"))


fileXML.write("""
    <AdcSampler name="adcSamplerMechanism" maxNumberThreads="8" />

	</configuration>""")

print("********************************************************")

print("		Number of SFEB boards: "+str(sfebcounter))
print("		Number of PFEB boards: "+str(pfebcounter))
print("		Number of L1DDC boards: "+str(l1ddccounter))
print("		Number of RIML1DDC1 boards: "+str(riml1ddc1counter))
print("		Number of RIML1DDC2 boards: "+str(riml1ddc2counter))
print("		Number of Pad Trigger boards: "+str(padtriggercounter))
print("		Number of Router boards: "+str(routercounter))

print("********************************************************")
print("*******        XML produced !!!!             ***********")
print("********************************************************")


fileXML.close()

# ----------------------  Create SCA XML Entities -------------------------------------------------------

fileSCA_SFEB=open("SCA_SFEB.xml","w+")
fileSCA_PFEB=open("SCA_PFEB.xml","w+")
fileSCA_L1DDC=open("SCA_L1DDC.xml","w+")
fileSCA_PADTRIGGER=open("SCA_PADTRIGGER.xml","w+")
fileSCA_ROUTER=open("SCA_ROUTER.xml","w+")
fileRIML1DDC1=open("SCA_RIML1DDC1.xml","w+")
fileRIML1DDC2=open("SCA_RIML1DDC2.xml","w+")

fileSCA_SFEB.write("""
	        <AnalogInputSystem name="ai" generalRefreshRate="5">
            <AnalogInput name="vmmPdo0" id="0">   <CalculatedVariable name="temperature" value="$applyGenericFormula(vmmTemperature)"  />  </AnalogInput>
            <AnalogInput name="vmmPdo1" id="1">   <CalculatedVariable name="temperature" value="$applyGenericFormula(vmmTemperature)"  />  </AnalogInput>
            <AnalogInput name="vmmPdo2" id="2">   <CalculatedVariable name="temperature" value="$applyGenericFormula(vmmTemperature)"  />  </AnalogInput>
            <AnalogInput name="vmmPdo3" id="3">   <CalculatedVariable name="temperature" value="$applyGenericFormula(vmmTemperature)"  />  </AnalogInput>
            <AnalogInput name="vmmPdo4" id="4">   <CalculatedVariable name="temperature" value="$applyGenericFormula(vmmTemperature)"  />  </AnalogInput>
            <AnalogInput name="vmmPdo5" id="5">   <CalculatedVariable name="temperature" value="$applyGenericFormula(vmmTemperature)"  />  </AnalogInput>
            <AnalogInput name="vmmPdo6" id="6">   <CalculatedVariable name="temperature" value="$applyGenericFormula(vmmTemperature)"  />  </AnalogInput>
            <AnalogInput name="vmmPdo7" id="7">   <CalculatedVariable name="temperature" value="$applyGenericFormula(vmmTemperature)"  />  </AnalogInput>
            <AnalogInput name="internalTemperature" id="31"> <CalculatedVariable name="temperature" value="$applyGenericFormula(scaTemperature)" /> </AnalogInput>
        </AnalogInputSystem>

        <SpiSystem name="spi">
            <SpiSlave transmissionSize="96" name="vmm0"
                busSpeed="20000000" slaveId="0" sclkIdleHigh="false"
				sampleAtFallingRxEdge="false" toggleSs="true"
                sampleAtFallingTxEdge="false" lsbToMsb="false" autoSsMode="true">
            </SpiSlave>
            <SpiSlave autoSsMode="true" name="vmm1" busSpeed="20000000"
                lsbToMsb="false" slaveId="1" transmissionSize="96"
                sampleAtFallingTxEdge="false" sclkIdleHigh="false"
				sampleAtFallingRxEdge="false" toggleSs="true">
            </SpiSlave>
            <SpiSlave autoSsMode="true" name="vmm2" busSpeed="20000000"
                lsbToMsb="false" slaveId="2" transmissionSize="96"
                sampleAtFallingTxEdge="false" sclkIdleHigh="false"
				sampleAtFallingRxEdge="false" toggleSs="true">
            </SpiSlave>
            <SpiSlave autoSsMode="true" name="vmm3" busSpeed="20000000"
                lsbToMsb="false" slaveId="3" transmissionSize="96"
                sampleAtFallingTxEdge="false" sclkIdleHigh="false"
				sampleAtFallingRxEdge="false" toggleSs="true">
            </SpiSlave>
            <SpiSlave autoSsMode="true" name="vmm4" busSpeed="20000000"
                lsbToMsb="false" slaveId="4" transmissionSize="96"
                sampleAtFallingTxEdge="false" sclkIdleHigh="false"
				sampleAtFallingRxEdge="false" toggleSs="true">
            </SpiSlave>
            <SpiSlave autoSsMode="true" name="vmm5" busSpeed="20000000"
                lsbToMsb="false" slaveId="5" transmissionSize="96"
                sampleAtFallingTxEdge="false" sclkIdleHigh="false"
				sampleAtFallingRxEdge="false" toggleSs="true">
            </SpiSlave>
            <SpiSlave autoSsMode="true" name="vmm6" busSpeed="20000000"
                lsbToMsb="false" slaveId="6" transmissionSize="96"
                sampleAtFallingTxEdge="false" sclkIdleHigh="false"
				sampleAtFallingRxEdge="false" toggleSs="true">
            </SpiSlave>
            <SpiSlave autoSsMode="true" name="vmm7" busSpeed="20000000"
                lsbToMsb="false" slaveId="7" transmissionSize="96"
                sampleAtFallingTxEdge="false" sclkIdleHigh="false"
				sampleAtFallingRxEdge="false" toggleSs="true">
            </SpiSlave>
        </SpiSystem>
        
        <DigitalIOSystem name="gpio">
            <DigitalIO name="rocSeu" isInput="true" id="0"></DigitalIO>
            <DigitalIO name="rocError" isInput="true" id="1"></DigitalIO>
            <DigitalIO name="rocPllLocked" isInput="true" id="2"></DigitalIO>
            <DigitalIO name="rocPllRocLocked" isInput="true" id="3"></DigitalIO>
            <DigitalIO name="rocSResetN" isInput="false" id="4"></DigitalIO>
            <DigitalIO name="rocPllResetN" isInput="false" id="5"></DigitalIO>
            <DigitalIO name="rocCoreResetN" isInput="false" id="6"></DigitalIO>
            <DigitalIO name="idChip" isInput="true" id="9"></DigitalIO>
            <DigitalIO name="gfzSda" isInput="true" id="10"></DigitalIO>
            <DigitalIO name="rocBypassForce" isInput="false" id="12"></DigitalIO>
            <DigitalIO name="tdsMode" isInput="false" id="14"></DigitalIO>
            <DigitalIO name="tdsaReset" isInput="false" id="15"></DigitalIO>
            <DigitalIO name="tdsbReset" isInput="false" id="16"></DigitalIO>
            <DigitalIO name="rocScaReset" isInput="true" id="17"></DigitalIO>
            <DigitalIO name="sdaRocPll" isInput="true" id="18"></DigitalIO>
            <DigitalIO name="tdscReset" isInput="false" id="19"></DigitalIO>
            <DigitalIO name="tdsdReset" isInput="false" id="20"></DigitalIO>
            <DigitalIO name="sclRocPll" isInput="true" id="21"></DigitalIO>
            <DigitalIO name="sdaRocCore" isInput="true" id="30"></DigitalIO>
            <DigitalIO name="sclRocCore" isInput="true" id="31"></DigitalIO>
        </DigitalIOSystem>

        <I2cMaster sclPadCmosOutput="true" name="tds0" masterId="0" busSpeed="100">
            <I2cSlave numberOfBytes="4" address="0" addressingMode="7" name="register0"></I2cSlave>
            <I2cSlave numberOfBytes="2" address="1" addressingMode="7" name="register1"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="2" addressingMode="7" name="register2"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="3" addressingMode="7" name="register3"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="4" addressingMode="7" name="register4"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="5" addressingMode="7" name="register5"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="6" addressingMode="7" name="register6"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="7" addressingMode="7" name="register7"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="8" addressingMode="7" name="register8"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="9" addressingMode="7" name="register9"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="10" addressingMode="7" name="register10"></I2cSlave>
            <I2cSlave numberOfBytes="8" address="11" addressingMode="7" name="register11"></I2cSlave>
            <I2cSlave numberOfBytes="4" address="12" addressingMode="7" name="register12"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="13" addressingMode="7" name="register13"></I2cSlave>
            <I2cSlave numberOfBytes="6" address="14" addressingMode="7" name="register14"></I2cSlave>
            <I2cSlave numberOfBytes="4" address="15" addressingMode="7" name="register15"></I2cSlave>
        </I2cMaster>

        <I2cMaster sclPadCmosOutput="false" name="tds1" masterId="1" busSpeed="100">
            <I2cSlave numberOfBytes="4" address="0" addressingMode="7" name="register0"></I2cSlave>
            <I2cSlave numberOfBytes="2" address="1" addressingMode="7" name="register1"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="2" addressingMode="7" name="register2"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="3" addressingMode="7" name="register3"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="4" addressingMode="7" name="register4"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="5" addressingMode="7" name="register5"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="6" addressingMode="7" name="register6"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="7" addressingMode="7" name="register7"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="8" addressingMode="7" name="register8"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="9" addressingMode="7" name="register9"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="10" addressingMode="7" name="register10"></I2cSlave>
            <I2cSlave numberOfBytes="8" address="11" addressingMode="7" name="register11"></I2cSlave>
            <I2cSlave numberOfBytes="4" address="12" addressingMode="7" name="register12"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="13" addressingMode="7" name="register13"></I2cSlave>
            <I2cSlave numberOfBytes="6" address="14" addressingMode="7" name="register14"></I2cSlave>
            <I2cSlave numberOfBytes="4" address="15" addressingMode="7" name="register15"></I2cSlave>
        </I2cMaster>

        <I2cMaster sclPadCmosOutput="false" name="tds2" masterId="2" busSpeed="100">
            <I2cSlave numberOfBytes="4" address="0" addressingMode="7" name="register0"></I2cSlave>
            <I2cSlave numberOfBytes="2" address="1" addressingMode="7" name="register1"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="2" addressingMode="7" name="register2"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="3" addressingMode="7" name="register3"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="4" addressingMode="7" name="register4"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="5" addressingMode="7" name="register5"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="6" addressingMode="7" name="register6"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="7" addressingMode="7" name="register7"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="8" addressingMode="7" name="register8"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="9" addressingMode="7" name="register9"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="10" addressingMode="7" name="register10"></I2cSlave>
            <I2cSlave numberOfBytes="8" address="11" addressingMode="7" name="register11"></I2cSlave>
            <I2cSlave numberOfBytes="4" address="12" addressingMode="7" name="register12"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="13" addressingMode="7" name="register13"></I2cSlave>
            <I2cSlave numberOfBytes="6" address="14" addressingMode="7" name="register14"></I2cSlave>
            <I2cSlave numberOfBytes="4" address="15" addressingMode="7" name="register15"></I2cSlave>
        </I2cMaster>

        <I2cMaster sclPadCmosOutput="false" name="tds3" masterId="3" busSpeed="100">
            <I2cSlave numberOfBytes="4" address="0" addressingMode="7" name="register0"></I2cSlave>
            <I2cSlave numberOfBytes="2" address="1" addressingMode="7" name="register1"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="2" addressingMode="7" name="register2"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="3" addressingMode="7" name="register3"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="4" addressingMode="7" name="register4"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="5" addressingMode="7" name="register5"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="6" addressingMode="7" name="register6"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="7" addressingMode="7" name="register7"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="8" addressingMode="7" name="register8"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="9" addressingMode="7" name="register9"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="10" addressingMode="7" name="register10"></I2cSlave>
            <I2cSlave numberOfBytes="8" address="11" addressingMode="7" name="register11"></I2cSlave>
            <I2cSlave numberOfBytes="4" address="12" addressingMode="7" name="register12"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="13" addressingMode="7" name="register13"></I2cSlave>
            <I2cSlave numberOfBytes="6" address="14" addressingMode="7" name="register14"></I2cSlave>
            <I2cSlave numberOfBytes="4" address="15" addressingMode="7" name="register15"></I2cSlave>
        </I2cMaster>


        <I2cMaster sclPadCmosOutput="false" name="rocPllCoreAnalog" masterId="4" busSpeed="400">
            <I2cSlave numberOfBytes="1" address="64" addressingMode="10" name="reg064ePllVmm0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="65" addressingMode="10" name="reg065ePllVmm0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="66" addressingMode="10" name="reg066ePllVmm0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="67" addressingMode="10" name="reg067ePllVmm0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="68" addressingMode="10" name="reg068ePllVmm0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="69" addressingMode="10" name="reg069ePllVmm0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="70" addressingMode="10" name="reg070ePllVmm0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="71" addressingMode="10" name="reg071ePllVmm0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="72" addressingMode="10" name="reg072ePllVmm0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="73" addressingMode="10" name="reg073ePllVmm0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="74" addressingMode="10" name="reg074ePllVmm0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="75" addressingMode="10" name="reg075ePllVmm0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="76" addressingMode="10" name="reg076ePllVmm0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="77" addressingMode="10" name="reg077ePllVmm0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="78" addressingMode="10" name="reg078ePllVmm0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="79" addressingMode="10" name="reg079ePllVmm0"></I2cSlave>		
            <I2cSlave numberOfBytes="1" address="80" addressingMode="10" name="reg080ePllVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="81" addressingMode="10" name="reg081ePllVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="82" addressingMode="10" name="reg082ePllVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="83" addressingMode="10" name="reg083ePllVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="84" addressingMode="10" name="reg084ePllVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="85" addressingMode="10" name="reg085ePllVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="86" addressingMode="10" name="reg086ePllVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="87" addressingMode="10" name="reg087ePllVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="88" addressingMode="10" name="reg088ePllVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="89" addressingMode="10" name="reg089ePllVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="90" addressingMode="10" name="reg090ePllVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="91" addressingMode="10" name="reg091ePllVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="92" addressingMode="10" name="reg092ePllVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="93" addressingMode="10" name="reg093ePllVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="94" addressingMode="10" name="reg094ePllVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="95" addressingMode="10" name="reg095ePllVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="96" addressingMode="10" name="reg096ePllTdc"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="97" addressingMode="10" name="reg097ePllTdc"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="98" addressingMode="10" name="reg098ePllTdc"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="99" addressingMode="10" name="reg099ePllTdc"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="100" addressingMode="10" name="reg100ePllTdc"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="101" addressingMode="10" name="reg101ePllTdc"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="102" addressingMode="10" name="reg102ePllTdc"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="103" addressingMode="10" name="reg103ePllTdc"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="104" addressingMode="10" name="reg104ePllTdc"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="105" addressingMode="10" name="reg105ePllTdc"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="106" addressingMode="10" name="reg106ePllTdc"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="107" addressingMode="10" name="reg107ePllTdc"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="108" addressingMode="10" name="reg108ePllTdc"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="109" addressingMode="10" name="reg109ePllTdc"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="110" addressingMode="10" name="reg110ePllTdc"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="111" addressingMode="10" name="reg111ePllTdc"></I2cSlave>	
            <I2cSlave numberOfBytes="1" address="112" addressingMode="10" name="reg112"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="113" addressingMode="10" name="reg113"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="114" addressingMode="10" name="reg114"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="115" addressingMode="10" name="reg115"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="116" addressingMode="10" name="reg116"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="117" addressingMode="10" name="reg117"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="118" addressingMode="10" name="reg118"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="119" addressingMode="10" name="reg119"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="120" addressingMode="10" name="reg120"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="121" addressingMode="10" name="reg121vmmBcrInv"></I2cSlave>		
            <I2cSlave numberOfBytes="1" address="122" addressingMode="10" name="reg122vmmEnaInv"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="123" addressingMode="10" name="reg123vmmL0Inv"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="124" addressingMode="10" name="reg124vmmTpInv"></I2cSlave>
        </I2cMaster>

        <I2cMaster sclPadCmosOutput="false" name="rocCoreDigital" masterId="5" busSpeed="400">
            <I2cSlave numberOfBytes="1" address="0" addressingMode="10" name="reg000rocId"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="1" addressingMode="10" name="reg001elinkSpeed"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="2" addressingMode="10" name="reg002sRoc0VmmConnections"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="3" addressingMode="10" name="reg003sRoc1VmmConnections"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="4" addressingMode="10" name="reg004sRoc2VmmConnections"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="5" addressingMode="10" name="reg005sRoc3VmmConnections"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="6" addressingMode="10" name="reg006eopAndNullEventEnable"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="7" addressingMode="10" name="reg007sRocEnable"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="8" addressingMode="10" name="reg008vmmEnable"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="9" addressingMode="10" name="reg009timeout"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="10" addressingMode="10" name="reg010bcOffset0_txcSel"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="11" addressingMode="10" name="reg011bcOffset1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="12" addressingMode="10" name="reg012bcRollover0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="13" addressingMode="10" name="reg013bcRollover1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="14" addressingMode="10" name="reg014eportEnable"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="19" addressingMode="10" name="reg019fakeVmmFailure"></I2cSlave>		
            <I2cSlave numberOfBytes="1" address="20" addressingMode="10" name="reg020busyAndTdcEnable"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="21" addressingMode="10" name="reg021busyOnLimit0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="22" addressingMode="10" name="reg022busyOnLimit1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="23" addressingMode="10" name="reg023busyOffLimit0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="24" addressingMode="10" name="reg024busyOffLimit1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="31" addressingMode="10" name="reg031l1EventsWithoutComma"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="32" addressingMode="10" name="reg022vmmCapture0Status"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="33" addressingMode="10" name="reg033vmmCapture1Status"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="34" addressingMode="10" name="reg034vmmCapture2Status"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="35" addressingMode="10" name="reg035vmmCapture3Status"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="36" addressingMode="10" name="reg036vmmCapture4Status"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="37" addressingMode="10" name="reg037vmmCapture5Status"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="38" addressingMode="10" name="reg038vmmCapture6Status"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="39" addressingMode="10" name="reg039vmmCapture7Status"></I2cSlave>	
            <I2cSlave numberOfBytes="1" address="40" addressingMode="10" name="reg040sRoc0Status"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="41" addressingMode="10" name="reg041sRoc1Status"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="42" addressingMode="10" name="reg042sRoc2Status"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="43" addressingMode="10" name="reg043sRoc3Status"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="44" addressingMode="10" name="reg044seu"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="45" addressingMode="10" name="reg045parityCounterVmm0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="46" addressingMode="10" name="reg046parityCounterVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="47" addressingMode="10" name="reg047parityCounterVmm2"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="48" addressingMode="10" name="reg048parityCounterVmm3"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="49" addressingMode="10" name="reg049parityCounterVmm4"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="50" addressingMode="10" name="reg050parityCounterVmm5"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="51" addressingMode="10" name="reg051parityCounterVmm6"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="52" addressingMode="10" name="reg052parityCounterVmm7"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="53" addressingMode="10" name="reg053seuCounter"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="63" addressingMode="10" name="reg063timeoutStatus"></I2cSlave>
        </I2cMaster>
	""")

fileSCA_PFEB.write("""
        <AnalogInputSystem name="ai" generalRefreshRate="5">
            <AnalogInput name="vmmPdo0" id="0">   <CalculatedVariable name="temperature" value="$applyGenericFormula(vmmTemperature)"  />  </AnalogInput>
            <AnalogInput name="vmmPdo1" id="1">   <CalculatedVariable name="temperature" value="$applyGenericFormula(vmmTemperature)"  />  </AnalogInput>
            <AnalogInput name="vmmPdo2" id="2">   <CalculatedVariable name="temperature" value="$applyGenericFormula(vmmTemperature)"  />  </AnalogInput>
            <AnalogInput name="internalTemperature" id="31"> <CalculatedVariable name="temperature" value="$applyGenericFormula(scaTemperature)" /> </AnalogInput>
        </AnalogInputSystem>

        <SpiSystem name="spi">
            <SpiSlave transmissionSize="96" name="vmm0"
                busSpeed="20000000" slaveId="0" sclkIdleHigh="false"
				sampleAtFallingRxEdge="false" toggleSs="true"
                sampleAtFallingTxEdge="false" lsbToMsb="false" autoSsMode="true">
            </SpiSlave>
            <SpiSlave autoSsMode="true" name="vmm1" busSpeed="20000000"
                lsbToMsb="false" slaveId="2" transmissionSize="96"
                sampleAtFallingTxEdge="false" sclkIdleHigh="false"
				sampleAtFallingRxEdge="false" toggleSs="true">
            </SpiSlave>
            <SpiSlave autoSsMode="true" name="vmm2" busSpeed="20000000"
                lsbToMsb="false" slaveId="1" transmissionSize="96"
                sampleAtFallingTxEdge="false" sclkIdleHigh="false"
				sampleAtFallingRxEdge="false" toggleSs="true">
            </SpiSlave>
        </SpiSystem>

        <DigitalIOSystem name="gpio">
            <DigitalIO name="rocSeu" isInput="true" id="0"></DigitalIO>
            <DigitalIO name="rocError" isInput="true" id="1"></DigitalIO>
            <DigitalIO name="rocPllLocked" isInput="true" id="2"></DigitalIO>
            <DigitalIO name="rocPllRocLocked" isInput="true" id="3"></DigitalIO>
            <DigitalIO name="rocSResetN" isInput="false" id="4"></DigitalIO>
            <DigitalIO name="rocPllResetN" isInput="false" id="5"></DigitalIO>
            <DigitalIO name="rocCoreResetN" isInput="false" id="6"></DigitalIO>
            <DigitalIO name="idChip" isInput="true" id="9"></DigitalIO>
            <DigitalIO name="gfzSda" isInput="true" id="10"></DigitalIO>
            <DigitalIO name="rocBypassForce" isInput="false" id="12"></DigitalIO>
            <DigitalIO name="tdsMode" isInput="false" id="14"></DigitalIO>
            <DigitalIO name="tdsReset" isInput="false" id="15"></DigitalIO>
            <DigitalIO name="rocScaReset" isInput="true" id="17"></DigitalIO>
            <DigitalIO name="sdaRocPll" isInput="true" id="18"></DigitalIO>
            <DigitalIO name="sclRocPll" isInput="true" id="21"></DigitalIO>
            <DigitalIO name="sdaRocCore" isInput="true" id="30"></DigitalIO>
            <DigitalIO name="sclRocCore" isInput="true" id="31"></DigitalIO>
        </DigitalIOSystem>

        <I2cMaster sclPadCmosOutput="false" name="rocCoreDigital" masterId="5" busSpeed="400">
            <I2cSlave numberOfBytes="1" address="0" addressingMode="10" name="reg000rocId"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="1" addressingMode="10" name="reg001elinkSpeed"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="2" addressingMode="10" name="reg002sRoc0VmmConnections"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="3" addressingMode="10" name="reg003sRoc1VmmConnections"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="4" addressingMode="10" name="reg004sRoc2VmmConnections"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="5" addressingMode="10" name="reg005sRoc3VmmConnections"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="6" addressingMode="10" name="reg006eopAndNullEventEnable"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="7" addressingMode="10" name="reg007sRocEnable"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="8" addressingMode="10" name="reg008vmmEnable"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="9" addressingMode="10" name="reg009timeout"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="10" addressingMode="10" name="reg010bcOffset0_txcSel"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="11" addressingMode="10" name="reg011bcOffset1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="12" addressingMode="10" name="reg012bcRollover0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="13" addressingMode="10" name="reg013bcRollover1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="14" addressingMode="10" name="reg014eportEnable"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="19" addressingMode="10" name="reg019fakeVmmFailure"></I2cSlave>		
            <I2cSlave numberOfBytes="1" address="20" addressingMode="10" name="reg020busyAndTdcEnable"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="21" addressingMode="10" name="reg021busyOnLimit0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="22" addressingMode="10" name="reg022busyOnLimit1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="23" addressingMode="10" name="reg023busyOffLimit0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="24" addressingMode="10" name="reg024busyOffLimit1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="31" addressingMode="10" name="reg031l1EventsWithoutComma"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="32" addressingMode="10" name="reg022vmmCapture0Status"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="33" addressingMode="10" name="reg033vmmCapture1Status"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="34" addressingMode="10" name="reg034vmmCapture2Status"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="35" addressingMode="10" name="reg035vmmCapture3Status"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="36" addressingMode="10" name="reg036vmmCapture4Status"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="37" addressingMode="10" name="reg037vmmCapture5Status"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="38" addressingMode="10" name="reg038vmmCapture6Status"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="39" addressingMode="10" name="reg039vmmCapture7Status"></I2cSlave>	
            <I2cSlave numberOfBytes="1" address="40" addressingMode="10" name="reg040sRoc0Status"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="41" addressingMode="10" name="reg041sRoc1Status"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="42" addressingMode="10" name="reg042sRoc2Status"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="43" addressingMode="10" name="reg043sRoc3Status"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="44" addressingMode="10" name="reg044seu"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="45" addressingMode="10" name="reg045parityCounterVmm0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="46" addressingMode="10" name="reg046parityCounterVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="47" addressingMode="10" name="reg047parityCounterVmm2"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="48" addressingMode="10" name="reg048parityCounterVmm3"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="49" addressingMode="10" name="reg049parityCounterVmm4"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="50" addressingMode="10" name="reg050parityCounterVmm5"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="51" addressingMode="10" name="reg051parityCounterVmm6"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="52" addressingMode="10" name="reg052parityCounterVmm7"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="53" addressingMode="10" name="reg053seuCounter"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="63" addressingMode="10" name="reg063timeoutStatus"></I2cSlave>
        </I2cMaster>

        <I2cMaster sclPadCmosOutput="false" name="rocPllCoreAnalog" masterId="4" busSpeed="400">
            <I2cSlave numberOfBytes="1" address="64" addressingMode="10" name="reg064ePllVmm0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="65" addressingMode="10" name="reg065ePllVmm0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="66" addressingMode="10" name="reg066ePllVmm0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="67" addressingMode="10" name="reg067ePllVmm0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="68" addressingMode="10" name="reg068ePllVmm0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="69" addressingMode="10" name="reg069ePllVmm0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="70" addressingMode="10" name="reg070ePllVmm0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="71" addressingMode="10" name="reg071ePllVmm0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="72" addressingMode="10" name="reg072ePllVmm0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="73" addressingMode="10" name="reg073ePllVmm0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="74" addressingMode="10" name="reg074ePllVmm0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="75" addressingMode="10" name="reg075ePllVmm0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="76" addressingMode="10" name="reg076ePllVmm0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="77" addressingMode="10" name="reg077ePllVmm0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="78" addressingMode="10" name="reg078ePllVmm0"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="79" addressingMode="10" name="reg079ePllVmm0"></I2cSlave>		
            <I2cSlave numberOfBytes="1" address="80" addressingMode="10" name="reg080ePllVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="81" addressingMode="10" name="reg081ePllVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="82" addressingMode="10" name="reg082ePllVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="83" addressingMode="10" name="reg083ePllVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="84" addressingMode="10" name="reg084ePllVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="85" addressingMode="10" name="reg085ePllVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="86" addressingMode="10" name="reg086ePllVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="87" addressingMode="10" name="reg087ePllVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="88" addressingMode="10" name="reg088ePllVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="89" addressingMode="10" name="reg089ePllVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="90" addressingMode="10" name="reg090ePllVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="91" addressingMode="10" name="reg091ePllVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="92" addressingMode="10" name="reg092ePllVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="93" addressingMode="10" name="reg093ePllVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="94" addressingMode="10" name="reg094ePllVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="95" addressingMode="10" name="reg095ePllVmm1"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="96" addressingMode="10" name="reg096ePllTdc"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="97" addressingMode="10" name="reg097ePllTdc"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="98" addressingMode="10" name="reg098ePllTdc"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="99" addressingMode="10" name="reg099ePllTdc"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="100" addressingMode="10" name="reg100ePllTdc"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="101" addressingMode="10" name="reg101ePllTdc"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="102" addressingMode="10" name="reg102ePllTdc"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="103" addressingMode="10" name="reg103ePllTdc"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="104" addressingMode="10" name="reg104ePllTdc"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="105" addressingMode="10" name="reg105ePllTdc"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="106" addressingMode="10" name="reg106ePllTdc"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="107" addressingMode="10" name="reg107ePllTdc"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="108" addressingMode="10" name="reg108ePllTdc"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="109" addressingMode="10" name="reg109ePllTdc"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="110" addressingMode="10" name="reg110ePllTdc"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="111" addressingMode="10" name="reg111ePllTdc"></I2cSlave>	
            <I2cSlave numberOfBytes="1" address="112" addressingMode="10" name="reg112"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="113" addressingMode="10" name="reg113"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="114" addressingMode="10" name="reg114"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="115" addressingMode="10" name="reg115"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="116" addressingMode="10" name="reg116"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="117" addressingMode="10" name="reg117"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="118" addressingMode="10" name="reg118"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="119" addressingMode="10" name="reg119"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="120" addressingMode="10" name="reg120"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="121" addressingMode="10" name="reg121vmmBcrInv"></I2cSlave>		
            <I2cSlave numberOfBytes="1" address="122" addressingMode="10" name="reg122vmmEnaInv"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="123" addressingMode="10" name="reg123vmmL0Inv"></I2cSlave>
            <I2cSlave numberOfBytes="1" address="124" addressingMode="10" name="reg124vmmTpInv"></I2cSlave>
        </I2cMaster>

        <I2cMaster sclPadCmosOutput="false" name="tds0" masterId="0" busSpeed="100">
            <I2cSlave numberOfBytes="4" address="0" addressingMode="7" name="register0"></I2cSlave>
            <I2cSlave numberOfBytes="2" address="1" addressingMode="7" name="register1"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="2" addressingMode="7" name="register2"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="3" addressingMode="7" name="register3"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="4" addressingMode="7" name="register4"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="5" addressingMode="7" name="register5"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="6" addressingMode="7" name="register6"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="7" addressingMode="7" name="register7"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="8" addressingMode="7" name="register8"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="9" addressingMode="7" name="register9"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="10" addressingMode="7" name="register10"></I2cSlave>
            <I2cSlave numberOfBytes="8" address="11" addressingMode="7" name="register11"></I2cSlave>
            <I2cSlave numberOfBytes="4" address="12" addressingMode="7" name="register12"></I2cSlave>
            <I2cSlave numberOfBytes="16" address="13" addressingMode="7" name="register13"></I2cSlave>
            <I2cSlave numberOfBytes="6" address="14" addressingMode="7" name="register14"></I2cSlave>
            <I2cSlave numberOfBytes="4" address="15" addressingMode="7" name="register15"></I2cSlave>
        </I2cMaster>	
	""")

fileSCA_L1DDC.write("""
		<AnalogInputSystem name="ai" generalRefreshRate="5">
           <AnalogInput id="0" name="GBTX1_TEMP" enableCurrentSource="true" > <CalculatedVariable name="temperature" value="$applyGenericFormula(thermistorTemperature)" /> </AnalogInput>
           <AnalogInput id="1" name="GBTX2_TEMP" enableCurrentSource="true" > <CalculatedVariable name="temperature" value="$applyGenericFormula(thermistorTemperature)" /> </AnalogInput>
           <AnalogInput id="3" name="1V5_PTAT">                               <CalculatedVariable name="temperature" value="$applyGenericFormula(feastTemperature_1V5)" />  </AnalogInput>
           <AnalogInput id="4" name="2V5_PTAT"> 			      	  		  <CalculatedVariable name="temperature" value="$applyGenericFormula(feastTemperature_2V5)" />  </AnalogInput>
           <AnalogInput id="5" name="P1V5_SCA"> 							  <CalculatedVariable name="power" value="$thisObjectAddress.value*3.0" />                      </AnalogInput>
           <AnalogInput id="6" name="P2V5_SCA"> 						      <CalculatedVariable name="power" value="$thisObjectAddress.value*5.0" />		      		    </AnalogInput>
           <AnalogInput id="7" name="VTRX1_RSSI"> 				 			  <CalculatedVariable name="power" value="$applyGenericFormula(rssiCurrentmA)" /> 	            </AnalogInput>
           <AnalogInput id="8" name="VTRX2_RSSI"> 							  <CalculatedVariable name="power" value="$applyGenericFormula(rssiCurrentmA)" /> 	            </AnalogInput>
			<AnalogInput name="internalTemperature" id="31">                  <CalculatedVariable name="temperature" value="$applyGenericFormula(scaTemperature)" />        </AnalogInput>
		</AnalogInputSystem>
		<I2cMaster sclPadCmosOutput="false" name="gbtx1" masterId="0" busSpeed="100">
			<I2cSlave numberOfBytes="3" address="1" addressingMode="7" name="gbtx1"></I2cSlave>
		</I2cMaster>
		<I2cMaster sclPadCmosOutput="false" name="gbtx2" masterId="1" busSpeed="100">
			<I2cSlave numberOfBytes="3" address="2" addressingMode="7" name="gbtx2"></I2cSlave>
		</I2cMaster>	
		""")

fileSCA_PADTRIGGER.write("""
		<AnalogInputSystem name="ai" generalRefreshRate="5">
			<AnalogInput name="P2V5_2" id= "20"> <CalculatedVariable name="power" value="$thisObjectAddress.value*1.0" />	 </AnalogInput>
			<AnalogInput name="P1V8A" id= "21"> <CalculatedVariable name="power" value="$thisObjectAddress.value*1.0" />	 </AnalogInput>
			<AnalogInput name="P1V2A" id= "23"> <CalculatedVariable name="power" value="$thisObjectAddress.value*1.0" />	 </AnalogInput>
			<AnalogInput name="P1V0A" id= "24"> <CalculatedVariable name="power" value="$thisObjectAddress.value*1.0" />	 </AnalogInput>
			<AnalogInput name="P2V5_1" id= "26"> <CalculatedVariable name="power" value="$thisObjectAddress.value*1.0" />	 </AnalogInput>
            <AnalogInput name="P1V8" id= "27"> <CalculatedVariable name="power" value="$thisObjectAddress.value*1.0" />	 </AnalogInput>
            <AnalogInput name="P1V5" id= "29"> <CalculatedVariable name="power" value="$thisObjectAddress.value*1.0" />	 </AnalogInput>
            <AnalogInput name="P1V0" id= "30"> <CalculatedVariable name="power" value="$thisObjectAddress.value*1.0" />	 </AnalogInput>
			<AnalogInput name="internalTemperature" id="31"> <CalculatedVariable name="temperature" value="$applyGenericFormula(scaTemperature)" /> </AnalogInput>
		</AnalogInputSystem>

		<DigitalIOSystem name="gpio">
		    <DigitalIO name="clock160_pri_sec" isInput="false" id="0"></DigitalIO>
		    <DigitalIO name="clock_xo160_enable" isInput="false" id="1"></DigitalIO>
		    <DigitalIO name="VTTx_disable" isInput="false" id="2"></DigitalIO>
		    <DigitalIO name="FPGA_PROGRAM" isInput="true" id="3"></DigitalIO>
		    <DigitalIO name="FPGA_INIT" isInput="true" id="4"></DigitalIO>
		    <DigitalIO name="FPGA_DONE" isInput="true" id="5"></DigitalIO>
		   	<DigitalIO name="gpio-repeaterChip1" isInput="false" id="6"></DigitalIO>
		    <DigitalIO name="gpio-repeaterChip2" isInput="false" id="7"></DigitalIO>
		    <DigitalIO name="gpio-repeaterChip3" isInput="false" id="8"></DigitalIO>
		    <DigitalIO name="gpio-repeaterChip4" isInput="false" id="9"></DigitalIO>
		    <DigitalIO name="gpio-repeaterChip5" isInput="false" id="10"></DigitalIO>
		    <DigitalIO name="gpio-repeaterChip6" isInput="false" id="11"></DigitalIO>
		    <DigitalIO name="FPGA_general12" isInput="false" id="12"></DigitalIO>
		    <DigitalIO name="FPGA_general13" isInput="false" id="13"></DigitalIO>
		    <DigitalIO name="FPGA_general14" isInput="false" id="14"></DigitalIO>
		    <DigitalIO name="FPGA_general15" isInput="false" id="15"></DigitalIO>
		    <DigitalIO name="FPGA_general16" isInput="false" id="16"></DigitalIO>
		    <DigitalIO name="FPGA_general17" isInput="false" id="17"></DigitalIO>
		    <DigitalIO name="FPGA_general18" isInput="false" id="18"></DigitalIO>
		    <DigitalIO name="FPGA_general19" isInput="false" id="19"></DigitalIO>
		    <DigitalIO name="FPGA_general20" isInput="false" id="20"></DigitalIO>
		    <DigitalIO name="FPGA_general21" isInput="false" id="21"></DigitalIO>
		    <DigitalIO name="FPGA_general22" isInput="false" id="22"></DigitalIO>
		    <DigitalIO name="FPGA_general23" isInput="false" id="23"></DigitalIO>
		</DigitalIOSystem>
		
        <I2cMaster sclPadCmosOutput="true" name="fpga" masterId="0" busSpeed="100">
           <I2cSlave numberOfBytes="1" address="127" addressingMode="7" name="fpga"></I2cSlave>
        </I2cMaster>
		<I2cMaster sclPadCmosOutput="false" name="repeaterChip1" masterId="3" busSpeed="100">
	    	<I2cSlave numberOfBytes="1" address="86" addressingMode="7" name="repeaterChip1"></I2cSlave>
		</I2cMaster>
		<I2cMaster sclPadCmosOutput="false" name="repeaterChip2" masterId="4" busSpeed="100">
			<I2cSlave numberOfBytes="1" address="86" addressingMode="7" name="repeaterChip2"></I2cSlave>
		</I2cMaster>
		<I2cMaster sclPadCmosOutput="false" name="repeaterChip3" masterId="5" busSpeed="100">
			<I2cSlave numberOfBytes="1" address="86" addressingMode="7" name="repeaterChip3"></I2cSlave>
		</I2cMaster>
		<I2cMaster sclPadCmosOutput="false" name="repeaterChip4" masterId="6" busSpeed="100">
			<I2cSlave numberOfBytes="1" address="86" addressingMode="7" name="repeaterChip4"></I2cSlave>
		</I2cMaster>
		<I2cMaster sclPadCmosOutput="false" name="repeaterChip5" masterId="7" busSpeed="100">
			<I2cSlave numberOfBytes="1" address="86" addressingMode="7" name="repeaterChip5"></I2cSlave>
		</I2cMaster>
		<I2cMaster sclPadCmosOutput="false" name="repeaterChip6" masterId="8" busSpeed="100">
			<I2cSlave numberOfBytes="1" address="86" addressingMode="7" name="repeaterChip6"></I2cSlave>
		</I2cMaster>

         <JtagSystem name="jtag">
            <XilinxFpga name="fpga" jtagClockMhz="10"/>
         </JtagSystem>	
		""")

fileSCA_ROUTER.write("""
		<AnalogInputSystem name="ai" generalRefreshRate="5">
			<AnalogInput name="VCC5VA" id="0"> <CalculatedVariable name="power" value="$thisObjectAddress.value*10.0/11.0" />	 </AnalogInput>
			<AnalogInput name="VCC5V" id="1"> <CalculatedVariable name="power" value="$thisObjectAddress.value*10.0/11.0" /> </AnalogInput>
			<AnalogInput name="mgtVccVoltage" id="2"> <CalculatedVariable name="power" value="$thisObjectAddress.value*1.0/2.0" /> </AnalogInput>
			<AnalogInput name="vcc3V3Voltage" id="3"> <CalculatedVariable name="power" value="$thisObjectAddress.value*4.7/5.7" /> </AnalogInput>
			<AnalogInput name="vcc1V5Voltage" id="5"> <CalculatedVariable name="power" value="$thisObjectAddress.value*2.0/3.0" /> </AnalogInput>
			<AnalogInput name="vcc2V5Voltage" id="6"> <CalculatedVariable name="power" value="$thisObjectAddress.value*4.7/5.7" /> </AnalogInput>
			<AnalogInput name="mgtVttVoltage" id="8"> <CalculatedVariable name="power" value="$thisObjectAddress.value*1.0/2.0" /> </AnalogInput>
			<AnalogInput name="vccAuxVoltage" id="9"> <CalculatedVariable name="power" value="$thisObjectAddress.value*2.0/3.0" /> </AnalogInput>
			<AnalogInput name="feastVccIntTemp" id="11"> <CalculatedVariable name="temperature" value="$applyGenericFormula(feastTemperature_VccInt)" /> </AnalogInput>
			<AnalogInput name="vccIntVoltage" id="12"> <CalculatedVariable name="power" value="$thisObjectAddress.value*1.0" /> </AnalogInput>
			<AnalogInput name="feastMgtVccTemp" id="15"> <CalculatedVariable name="temperature" value="$applyGenericFormula(feastTemperature_MgtVcc)" /> </AnalogInput>
			<AnalogInput name="feastAuxTemp" id="18"> <CalculatedVariable name="temperature" value="$applyGenericFormula(feastTemperature_AuxTemp)" /> </AnalogInput>
			<AnalogInput name="feastMgtVttTemp" id="21"> <CalculatedVariable name="temperature" value="$applyGenericFormula(feastTemperature_MgtVtt)" /> </AnalogInput>
			<AnalogInput name="boardTemp2_closeToFeast" id="23"> <CalculatedVariable name="temperature" value="$applyGenericFormula(thermistorTemperature)" /> </AnalogInput>
			<AnalogInput name="feastVcc2V5Temp" id="24"> <CalculatedVariable name="temperature" value="$applyGenericFormula(feastTemperature_Vcc2V5)" /> </AnalogInput>
			<AnalogInput name="boardTemp3_closeToMTx" id="26">  <CalculatedVariable name="temperature" value="$applyGenericFormula(thermistorTemperature)" /> </AnalogInput>
			<AnalogInput name="feastVcc3V3Temp" id="27"> <CalculatedVariable name="temperature" value="$applyGenericFormula(feastTemperature_Vcc3V3)" /> </AnalogInput>
			<AnalogInput name="boardTemp1_closeToFpga" id="29"> <CalculatedVariable name="temperature" value="$applyGenericFormula(thermistorTemperature)" /> </AnalogInput>
			<AnalogInput name="feastVcc1V5Temp" id="30"> <CalculatedVariable name="temperature" value="$applyGenericFormula(feastTemperature_Vcc1V5)" /> </AnalogInput>
			<AnalogInput name="internalTemperature" id="31"> <CalculatedVariable name="temperature" value="$applyGenericFormula(scaTemperature)" /> </AnalogInput>
		</AnalogInputSystem>
		
        <DigitalIOSystem name="gpio">
            <DigitalIO name="fpgaConfigOK" isInput="true" id="0"></DigitalIO>
            <DigitalIO name="routerId0" isInput="false" id="1"></DigitalIO>
            <DigitalIO name="routerId1" isInput="false" id="2"></DigitalIO>
            <DigitalIO name="routerId2" isInput="false" id="3"></DigitalIO>
            <DigitalIO name="routerId3" isInput="false" id="4"></DigitalIO>
            <DigitalIO name="routerId4" isInput="false" id="5"></DigitalIO>
            <DigitalIO name="routerId5" isInput="false" id="6"></DigitalIO>
            <DigitalIO name="routerId6" isInput="false" id="7"></DigitalIO>
            <DigitalIO name="routerId7" isInput="false" id="8"></DigitalIO>
            <DigitalIO name="mmcmBotLock" isInput="true" id="9"></DigitalIO>
            <DigitalIO name="designNum0" isInput="true" id="10"></DigitalIO>
            <DigitalIO name="designNum1" isInput="true" id="11"></DigitalIO>
            <DigitalIO name="designNum2" isInput="true" id="12"></DigitalIO>
            <DigitalIO name="fpgaInit" isInput="true" id="13"></DigitalIO>
            <DigitalIO name="mmcmReset" isInput="false" id="14"></DigitalIO>
            <DigitalIO name="softReset" isInput="false" id="15"></DigitalIO>
            <DigitalIO name="rxClkReady" isInput="true" id="16"></DigitalIO>
            <DigitalIO name="txClkReady" isInput="true" id="17"></DigitalIO>
            <DigitalIO name="cpllTopLock" isInput="true" id="18"></DigitalIO>
            <DigitalIO name="cpllBotLock" isInput="true" id="19"></DigitalIO>
            <DigitalIO name="mmcmTopLock" isInput="true" id="20"></DigitalIO>
            <DigitalIO name="semFatalError" isInput="true" id="21"></DigitalIO>
            <DigitalIO name="semHeartBeat" isInput="true" id="22"></DigitalIO>
            <DigitalIO name="debugEnable" isInput="false" id="23"></DigitalIO>
            <DigitalIO name="notConnected" isInput="true" id="24"></DigitalIO>
            <DigitalIO name="mtxRst" isInput="false" id="25"></DigitalIO>
            <DigitalIO name="masterChannel0" isInput="true" id="26"></DigitalIO>
            <DigitalIO name="masterChannel1" isInput="true" id="27"></DigitalIO>
            <DigitalIO name="masterChannel2" isInput="true" id="28"></DigitalIO>
            <DigitalIO name="ctrlMod0" isInput="false" id="29"></DigitalIO>
            <DigitalIO name="ctrlMod1" isInput="false" id="30"></DigitalIO>
            <DigitalIO name="multibootTrigger" isInput="false" id="31"></DigitalIO>
        </DigitalIOSystem>

        <I2cMaster sclPadCmosOutput="false" name="MTx1" masterId="0" busSpeed="100">
                <I2cSlave numberOfBytes="1" address="160" addressingMode="7" name="register0"></I2cSlave>
                <I2cSlave numberOfBytes="1" address="161" addressingMode="7" name="register1"></I2cSlave>
                <I2cSlave numberOfBytes="1" address="162" addressingMode="7" name="register2"></I2cSlave>
                <I2cSlave numberOfBytes="1" address="163" addressingMode="7" name="register3"></I2cSlave>
        </I2cMaster>

        <I2cMaster sclPadCmosOutput="false" name="MTx2" masterId="1" busSpeed="100">
                <I2cSlave numberOfBytes="1" address="160" addressingMode="7" name="register0"></I2cSlave>
                <I2cSlave numberOfBytes="1" address="161" addressingMode="7" name="register1"></I2cSlave>
                <I2cSlave numberOfBytes="1" address="162" addressingMode="7" name="register2"></I2cSlave>
                <I2cSlave numberOfBytes="1" address="163" addressingMode="7" name="register3"></I2cSlave>
        </I2cMaster>	
		""")

fileRIML1DDC1.write("""
		<AnalogInputSystem name="ai" generalRefreshRate="0">
			<AnalogInput name="GBTX1_TEMP" id="0" enableCurrentSource="true" >  <CalculatedVariable name="temperature" value="$applyGenericFormula(thermistorTemperature)" /> </AnalogInput>
			<AnalogInput name="1V5_PTAT1" id="3">                               <CalculatedVariable name="temperature" value="$applyGenericFormula(feastTemperature_1V5)" />  </AnalogInput>
			<AnalogInput name="2V5_PTAT1" id="4">                               <CalculatedVariable name="temperature" value="$applyGenericFormula(feastTemperature_2V5)" />  </AnalogInput>
			<AnalogInput name="P1V5_SCA1" id="5"> 							    <CalculatedVariable name="power" value="$thisObjectAddress.value*3.0" />                      </AnalogInput>
			<AnalogInput name="P2V5_SCA1" id="6"> 							    <CalculatedVariable name="power" value="$thisObjectAddress.value*5.0" />                      </AnalogInput>
			<AnalogInput name="VTRX1_RSSI" id="7">     			 			    <CalculatedVariable name="power" value="$applyGenericFormula(rssiCurrentmA)" /> 	            </AnalogInput>
			<AnalogInput name="VTRX1_REF_RSSI" id="8">				 		    <CalculatedVariable name="power" value="$applyGenericFormula(rssiCurrentmA)" /> 	            </AnalogInput>
			<AnalogInput name="internalTemperature1" id="31">  					<CalculatedVariable name="temperature" value="$applyGenericFormula(scaTemperature)" />         </AnalogInput>
		</AnalogInputSystem>
		
		<I2cMaster sclPadCmosOutput="false" name="vtrx3" masterId="0" busSpeed="100">
			<I2cSlave numberOfBytes="3" address="1" addressingMode="7" name="vtrx3"></I2cSlave>
		</I2cMaster>
		
		<DigitalIOSystem name="gpio">
			<DigitalIO name="feast_en1_r1" isInput="false" id="0"></DigitalIO>
			<DigitalIO name="feast_en1_r2" isInput="false" id="1"></DigitalIO>
			<DigitalIO name="feast_en1_r3" isInput="false" id="2"></DigitalIO>
			<DigitalIO name="feast_en1_r4" isInput="false" id="3"></DigitalIO>
			<DigitalIO name="feast_en1_r5" isInput="false" id="4"></DigitalIO>
			<DigitalIO name="feast_en1_r6" isInput="false" id="5"></DigitalIO>	
			<DigitalIO name="feast_en1_r7" isInput="false" id="6"></DigitalIO>
			<DigitalIO name="feast_en1_r8" isInput="false" id="7"></DigitalIO>	
			<DigitalIO name="feast_en1_pad" isInput="false" id="8"></DigitalIO>	
			<DigitalIO name="sca1_sel0" isInput="false" id="9"></DigitalIO>	
			<DigitalIO name="sca1_sel1" isInput="false" id="10"></DigitalIO>
			<DigitalIO name="sca1_sel" isInput="false" id="11"></DigitalIO>	
		</DigitalIOSystem>	
		""")

fileRIML1DDC2.write("""
		<AnalogInputSystem name="ai" generalRefreshRate="0">
			<AnalogInput name="GBTX2_TEMP" id="0" enableCurrentSource="true" >  <CalculatedVariable name="temperature" value="$applyGenericFormula(thermistorTemperature)" /> </AnalogInput>
			<AnalogInput name="1V5_PTAT2" id="3">                               <CalculatedVariable name="temperature" value="$applyGenericFormula(feastTemperature_1V5)" />  </AnalogInput>
			<AnalogInput name="2V5_PTAT2" id="4">                               <CalculatedVariable name="temperature" value="$applyGenericFormula(feastTemperature_2V5)" />  </AnalogInput>
			<AnalogInput name="P1V5_SCA2" id="5"> 							    <CalculatedVariable name="power" value="$thisObjectAddress.value*3.0" />                      </AnalogInput>
			<AnalogInput name="P2V5_SCA2" id="6"> 							    <CalculatedVariable name="power" value="$thisObjectAddress.value*5.0" />                      </AnalogInput>
			<AnalogInput name="VTRX2_RSSI" id="7">     			 			    <CalculatedVariable name="power" value="$applyGenericFormula(rssiCurrentmA)" /> 	            </AnalogInput>
			<AnalogInput name="VTRX2_REF_RSSI" id="8">				 		    <CalculatedVariable name="power" value="$applyGenericFormula(rssiCurrentmA)" /> 	            </AnalogInput>
			<AnalogInput name="internalTemperature2" id="31">  					<CalculatedVariable name="temperature" value="$applyGenericFormula(scaTemperature)" />         </AnalogInput>
		</AnalogInputSystem>
		
		<I2cMaster sclPadCmosOutput="false" name="vtrx4" masterId="0" busSpeed="100">
			<I2cSlave numberOfBytes="3" address="1" addressingMode="7" name="vtrx4"></I2cSlave>
		</I2cMaster>
		
		<DigitalIOSystem name="gpio">
			<DigitalIO name="feast_en2_r1" isInput="false" id="0"></DigitalIO>
			<DigitalIO name="feast_en2_r2" isInput="false" id="1"></DigitalIO>
			<DigitalIO name="feast_en2_r3" isInput="false" id="2"></DigitalIO>
			<DigitalIO name="feast_en2_r4" isInput="false" id="3"></DigitalIO>
			<DigitalIO name="feast_en2_r5" isInput="false" id="4"></DigitalIO>
			<DigitalIO name="feast_en2_r6" isInput="false" id="5"></DigitalIO>	
			<DigitalIO name="feast_en2_r7" isInput="false" id="6"></DigitalIO>
			<DigitalIO name="feast_en2_r8" isInput="false" id="7"></DigitalIO>	
			<DigitalIO name="feast_en2_pad" isInput="false" id="8"></DigitalIO>	
			<DigitalIO name="sca2_sel0" isInput="false" id="9"></DigitalIO>	
			<DigitalIO name="sca2_sel1" isInput="false" id="10"></DigitalIO>
			<DigitalIO name="sca2_sel" isInput="false" id="11"></DigitalIO>	
		</DigitalIOSystem>	
		""")

fileSCA_SFEB.close()
fileSCA_PFEB.close()
fileSCA_L1DDC.close()
fileSCA_PADTRIGGER.close()
fileSCA_ROUTER.close()
fileRIML1DDC1.close()
fileRIML1DDC2.close()
