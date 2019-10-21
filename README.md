# XMLCreator_OPCUASCA

Tool to create XML file for OPC UA SCA Server and calibrate FEAST temperature sensors (MMFE8,L1DDC,ADDC) for ATLAS NSW FELIX Readout

# How to run
```
python generateXML.py -mode U/C/S -m -l -a 
```
Mode Arguments:
*  U for Uncalibrated
*  C for Calibrated
*  S for Simulation

Enable Boards:
*  -m for MMFE8
*  -l for L1DDC
*  -a for ADDC