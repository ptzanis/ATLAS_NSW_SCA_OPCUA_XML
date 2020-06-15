source calibrateFEAST_MMG.sh $1
echo "FEAST calibration ready for MMG sector " $1
sleep 5
python generateXML_MMG.py -mode C -sector $1 -opcHost pcatlnswfelix04 -location BB5 -m -l -a -afs
echo "SCA OPC UA Server XML file ready for MMG sector " $1