# XMLCreator_OPCUASCA

Tool to create XML file for OPC UA SCA Server and calibrate FEAST temperature sensors (MMFE8,L1DDC,ADDC) for ATLAS NSW FELIX Readout

# How to run
```
python generateXML.py -mode U/C/S -sector A12 -opcHost pcatlnswfelix04 -m -l -a 
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

Enable Boards:
*  -m for MMFE8
*  -l for L1DDC
*  -a for ADDC