# from abc import abstractmethod
import heapq, random
from time import sleep
from users import User

class Internet:
    """abstract base class on which applications run and users use"""
    def __init__(self):
        self._status = True #internet is turned on
        self._packetheap = []
   
    def _allowconnections(self):
        """Flavor text to check if connections are allowed"""
        self._connectionstatus = True
        return self._connectionstatus
    
    def _updatestatus(self):
        """Flavor text to check Internet status"""
        self._status = True
        return self._status
    
    def _packethandler(self, package):
        """adds to heap"""
        self._packetheap.append(package)
        return print("package added to heap")
    
    def _sendpacket(self, person:User):
        """directs packet to correct person"""
        # for ele in heap, check name, send to correct person. 
        for packet in self._packetheap:
            for key, value in packet:
                if 'Bob' in key:
                    print("sending packet to Bob")
                    person.packets.append(value)
                else: 
                    print("sending packet to Alice")
                    person.packets.append(value)
                    
    
    # @abstractmethod
    def _makepackets(self):
        """makes random list of 0's and 1s to be sent"""
        bits = [random.randint(0,1) for _ in range(8)]
        bits = list(map(str,bits))
        packets = "".join(bits)
        return packets
    
    # @abstractmethod
    def _preppackets(self, target, packets):
        """send packets to next application"""
        packet_buffer = {target: packets}
        return packet_buffer
        

    
        

class Application(Internet):
    """Application class. Needs to be named and connected to internet to be used"""
    def __init__ (self, name:str):
        self.name = name
        super().__init__()
        
    def _connect(self):
        """check to see if connections are currently allowed """
        if super()._allowconnections():
            print("Connections are allowed at this time")
            return True
        else:
            print("Connections are not allowed at this time")
            return 1
    
    def _checkinternetstatus(self):
        """Checks to see if the internet itself is turned on."""
        if super()._updatestatus():
            print("Internt is turned on.\n Trying to connect...")
            sleep(1)
            if self._connect():
                print("Connection success!")
                return 0 
        else: 
            print("Internt is turned off")
            return 1
        
    def _makepackets(self):
        return super()._makepackets()
    
    def _sendpackets(self, target):
        packets = self._makepackets()
        tmp_packets = super()._preppackets(self.name, packets)
        tmp_packets = super()._preppackets(target, packets)
        super()._packethandler(tmp_packets)
        print("packets sent")
