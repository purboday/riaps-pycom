'''
Constants for the run-time system
Created on Oct 20, 2016

@author: riaps
'''
import riaps.consts.const as const

# Name of endpoint for actor-disco communication
const.discoEndpoint = 'tcp://127.0.0.1:9700'    # 'ipc:///tmp/riaps-disco'
# Timeout for actor-disco communication (-1: wait forever)
const.discoEndpointRecvTimeout = -1
const.discoEndpointSendTimeout = -1

# Name of endpoint for actor-depl communication
const.deplEndpoint = 'tcp://127.0.0.1:9780'     # 'ipc:///tmp/riaps-depl'
# Timeout for actor-depl communication (-1: wait forever)
const.deplEndpointRecvTimeout = 3000
const.deplEndpointSendTimeout = 3000

# Name of endpoint for actor-devm communication
const.devmEndpoint = 'tcp://127.0.0.1:9790'     # 'ipc:///tmp/riaps-devm
# Timeout for actor-depl communication (-1: wait forever)
const.devmEndpointRecvTimeout = 3000
const.devmEndpointSendTimeout = 3000

# Default host for disco redis host
const.discoRedisHost = 'localhost'
# Default port number for disco redis host
const.discoRedisPort = 6379

# Default host for the Controller
const.ctrlNode = 'localhost'
# Default port number for the Controller
const.ctrlPort = 8888

# Control service name
const.ctrlServiceName = 'RIAPSControl'
# Name of private key file
const.ctrlPrivateKey = 'id_rsa.key'
# SSH port
const.ctrlSSHPort = 22

# Nethog
const.nethogLibrary = 'libnethogs.so.master'
