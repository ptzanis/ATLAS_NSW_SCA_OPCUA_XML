import time
import pyuaf

from pyuaf.util             import Address, NodeId, opcuaidentifiers
from pyuaf.client           import Client
from pyuaf.client.settings  import ClientSettings, SessionSettings
from pyuaf.util             import loglevels, opcuastatuscodes

#Constants (??)

server_address='opc.tcp://pcatlnswfelix02:48020'
server_uri='urn:CERN:OpcUaScaServer'
server_ns=2

client = []
def connect():
	global client
	cs = ClientSettings("myClient", [server_address])
# Uncomment below for session logging
#	cs.logToStdOutLevel = loglevels.Info 
	max_attempts=40
	num_attempts=0
	while (True):
		print "Trying to connect to the OPC UA Server. Attempt #"+str(num_attempts)
		result=None
		try:
			client = Client(cs)
			rootNode = Address( NodeId(opcuaidentifiers.OpcUaId_RootFolder, 0), server_uri )
			result=client.browse ([ rootNode ])
		except Exception as e:
			print "Got exception: "+str(e)
			num_attempts = num_attempts+1
			if num_attempts > max_attempts:
				msg = 'Despite '+str(max_attempts)+ ' attempts couldnt establish OPC UA connection: exception is '+str(e)
				print msg
				dcs_test_utils.log_detail(False,msg,'')
				raise msg
			time.sleep(3)
			continue
		print 'Connected to OPC UA Server'
		return
			
		

def addr(sa):
	return Address(NodeId(sa,server_ns), server_uri)


def addr_to_str(address):
	return address.getExpandedNodeId().nodeId().identifier().idString

def map_errors(targets):
        return ' '.join(map (lambda x: str(x.status), targets))

def read(addresses):
        rv = client.read(addresses)
        if not rv.overallStatus.isGood():
                raise Exception ("read failed with the following error code: "+str(rv.overallStatus)+" specific error code(s):"+map_errors(rv.targets) )
        return rv

def write(addresses, values):
        rv = client.write(addresses, values)
        if not rv.overallStatus.isGood():
                raise Exception ("write failed with the following error code: "+str(rv.overallStatus)+" specific error code(s):"+map_errors(rv.targets))
        return rv
