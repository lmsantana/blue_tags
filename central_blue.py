from bluepy.btle import Scanner, DefaultDelegate, Peripheral, Service, Characteristic, UUID
from time import gmtime, strftime
import os
import sys

##############################################
# BluePy Library Notes
##############################################

# 1 -

##############################################
# TODO list
##############################################

# TODO: 

##############################################
# Global values for Bluetooth
##############################################

# Using for general storage
SPIRO_MAC_ADDR = 'd0:4f:8f:c9:d0:57'
BNDSW_MAC_ADDR = 'ec:5b:e7:e0:96:c2'
DRILL_MAC_ADDR = 'df:c5:a5:de:ee:9a'
MILLI_MAC_ADDR = 'c6:73:0d:c1:66:ba'
CIRCS_MAC_ADDR = 'ca:58:f6:d6:2f:ae'

ESTIMOTE_LBLUE_MAC_ADDR = "c2:79:3c:a4:ea:1a"
ESTIMOTE_PURPL_MAC_ADDR = "fe:45:d7:8b:a7:77"
ESTIMOTE_GREEN_MAC_ADDR = "d5:53:5d:fc:eb:6b"

# Using for friendly programming // NOT USED IN THIS IMPLEMENTATION
MAC_DIC = {'BENDSAW':BNDSW_MAC_ADDR, 'DRILL_PRESS':DRILL_MAC_ADDR,
			'MILL':MILLI_MAC_ADDR, 'CIRCULAR_SAW':CIRCS_MAC_ADDR,
			'SPIROMETER':SPIRO_MAC_ADDR}

TAG_DIC = {'AUSTIN': ESTIMOTE_LBLUE_MAC_ADDR,
           'HALEY' : ESTIMOTE_PURPL_MAC_ADDR,
           'JOSE'  : ESTIMOTE_GREEN_MAC_ADDR}

# UUID for the Bluetooth UART Service based on Nordic Semiconductors Chip
UART_UUID = UUID('6E400001-B5A3-F393-E0A9-E50E24DCCA9E')

# Global dictionary to hold Peripheral objects to nodes
nodes = {}

##############################################
# Global general variables
##############################################
counter = 0

##############################################
# Override for Scanner Class
##############################################
class ScanDelegate(DefaultDelegate):
    def __inti__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print "Discovered device", dev.addr
        elif isNewData:
            print "Received new data from", dev.addr


###############################################
# General Functions
###############################################



###############################################
# Scanning Devices
###############################################

# Scanning was moved to the main loop

###############################################
# Connecting Devices
###############################################

# There is no connection to devices

###############################################
# Main loop routine
###############################################
# Delete old file for testing
os.system("sudo rm data/data_from_rpi.csv")
# Creating new file
file = open("data/data_from_rpi.csv", "a")

while 1:
    try:
        os.system("sudo hciconfig hci0 down")
        os.system("sudo hciconfig hci0 up")
        print " "
        print "Scanning devices... (time frame of 10 seconds)"
        scanner = Scanner().withDelegate(ScanDelegate())
        devices = scanner.scan(10.0)

        print " "
        print "Checking which tags were sensed..."
        counter = counter + 1
        for dev in devices:
            if dev.addr == TAG_DIC['AUSTIN']:
                if dev.rssi >= -80:
                    print "Austin was sensed with RSSI of %d dB" %(dev.rssi)
                    file.write("Austin, "+ strftime("%Y-%m-%d %H:%M:%S", gmtime())+ (", %d \n" %counter))
            if dev.addr == TAG_DIC['HALEY']:
                if dev.rssi >= -80:
                    print "Haley was sensed with RSSI of %d dB" %(dev.rssi)
                    file.write("Haley, "+ strftime("%Y-%m-%d %H:%M:%S", gmtime())+ (", %d \n" %counter))
            if dev.addr == TAG_DIC['JOSE']:
                if dev.rssi >= -80:
                    print "Jose was sensed with RSSI of %d dB" %(dev.rssi)
                    file.write("Jose, "+ strftime("%Y-%m-%d %H:%M:%S", gmtime())+ (", %d \n" %counter))
        
    except KeyboardInterrupt:
        print " "
        print "Python script was killed, closing file..."
        file.close()
        sys.exit()
