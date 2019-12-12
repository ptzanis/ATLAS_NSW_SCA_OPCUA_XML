###################################################################################
# Developer: Polyneikis Tzanis (polyneikis.tzanis@cern.ch)
# Date 12/12/2019 : initial commit for STG
###################################################################################

# ----------------------  SCA templates -------------------------------------------------------

def templateSFEB_PFEB_Uncalibrated():
	return """   
	 <SCA address="simple-netio://direct/%s.cern.ch/1234%s/1235%s/%s" name="%s" idConstraint="dont_care" supervised="true" recoveryActionScaStayedPowered="do_nothing" recoveryActionScaWasRepowered="reset_and_configure" managementFromAddressSpace="only_if_kaputt" >
        &SCA_%s;
    </SCA>
	"""
def templateSFEB_PFEB_Simulation():
	return """   
	 <SCA address="sca-simulator://%s" name="%s" idConstraint="dont_care" supervised="true" recoveryActionScaStayedPowered="do_nothing" recoveryActionScaWasRepowered="reset_and_configure" managementFromAddressSpace="only_if_kaputt" >
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
    <CalculatedVariableGenericFormula name="scaTemperature" formula="(0.79-$thisObjectAddress.value)*545.454545455-40"/>
    <CalculatedVariableGenericFormula name="vmmTemperature" formula="(725.0-(1000.0*$thisObjectAddress.value))/1.85"/>
    """)

sfebcounter=pfebcounter=0
counter=0
felixDeviceId="0"

for board,elink in zip(boards,elinks):
    counter=counter+1
    if(re.compile("83f").match(elink)):
	  felixDeviceId="1"
    if(args['SFEB']==True):
	  if(re.compile("SFEB").match(board)):
	    sfebcounter=sfebcounter+1	
	    if(args['mode']=="U"):
	      fileXML.write(templateSFEB_PFEB_Uncalibrated() % (opcHost,felixDeviceId,felixDeviceId,elink,board,"SFEB"))
	    if(args['mode']=="S"):
	      fileXML.write(templateSFEB_PFEB_Simulation() % (counter,board,"SFEB"))
    if(args['PFEB']==True):
	  if(re.compile("PFEB").match(board)):
	    pfebcounter=pfebcounter+1	
	    if(args['mode']=="U"):
	      fileXML.write(templateSFEB_PFEB_Uncalibrated() % (opcHost,felixDeviceId,felixDeviceId,elink,board,"PFEB"))
	    if(args['mode']=="S"):
	      fileXML.write(templateSFEB_PFEB_Simulation() % (counter,board,"PFEB"))		



fileXML.write("""
    <AdcSampler name="adcSamplerMechanism" maxNumberThreads="8" />

	</configuration>""")

print("********************************************************")

print("		Number of SFEB boards: "+str(sfebcounter))
print("		Number of PFEB boards: "+str(pfebcounter))

print("********************************************************")
print("*******        XML produced !!!!             ***********")
print("********************************************************")


fileXML.close()