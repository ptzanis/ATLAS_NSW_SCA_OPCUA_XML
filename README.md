# XMLCreator_OPCUASCA

Tool to create XML file for OPC UA SCA Server and calibrate FEAST temperature sensors (MMFE8,L1DDC,ADDC) for ATLAS NSW FELIX Readout

# How to run (Auto calibration+XML for MMG at BB5)
```
source autoXML_MMG.sh AXX
```

# How to run (XML creation)
```
python generateXML_MMG.py -mode U/C/S -sector A12 -opcHost pcatlnswfelix04 -location BB5 -m -l -a 
```
Mode Arguments:
*  U for Uncalibrated
*  C for Calibrated
*  S for Simulation

Sector Argument:
Endcap [A][C]
Sector 01-16
e.g. A12 for Endcap A and Sector 12

opcHost Argument:
e.g. pcatlnswfelix04

location Argument:
e.g. BB5 or 191

Enable Boards:
*  -m for MMFE8
*  -l for L1DDC
*  -a for ADDC

# How to run (FEAST calibration for MMG at BB5)
```
source calibrateFEAST_MMG.sh AXX
```
