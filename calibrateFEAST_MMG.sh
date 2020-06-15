export PYTHONPATH=src/PyUAF/:$PYTHONPATH
export LD_LIBRARY_PATH=src/PyUAF/:$LD_LIBRARY_PATH
SCRIPT=src/client.py
/usr/bin/python $SCRIPT -sector $1

