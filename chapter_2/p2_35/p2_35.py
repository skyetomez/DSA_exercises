"""
Write a set of Python classes that can simulate an Internet application in
which one party, Alice, is periodically creating a set of packets that she
wants to send to Bob. An Internet process is continually checking if Alice
has any packets to send, and if so, it delivers them to Bob’s computer, and
Bob is periodically checking if his computer has a packet from Alice, and,
if so, he reads and deletes it

"""
from abc import abstractmethod


class Internet:
    """abstract base class on which applications run and users use"""
    def __init__(self):
        self._status = True #internet is turned on
   
    def _allowconnections(self):
        self._connectionstatus = True
    
    @abstractmethod
    def _makepackets(self):
         """make packet item to be sent"""
    
    @abstractmethod
    def _sendpackets(self, target):
        """send packets to next application"""
        
    def _trackpackets(self,packet_dict:dict):
        pass
    
        

class Application(Internet):
    """Application class. Needs to be named and connected to internet to be used"""
    def __init__ (self, name:str):
        self.name = name
        
    def _connect(self):
        if super()._allowconnections():
            return True
        else:
            print("Connections are not allowed at this time")
    
    def _checkinternetstatus(self):
        if super()._status:
            print("Internt is turned on")
            print("trying to connect")
            if self._connect:
                print("Connection success!")
        else: 
            print("Internt is turned off")
            
    def _makepackets(self):
        return super()._makepackets()
    
    def _sendpackets(self, target):
        return super()._sendpackets(target)
    
    
class User:
    """abstract baseclass for users of applications"""
    def __init__(self,name:str):
        self.name = name
        
    @abstractmethod
    def begin_action(self, app):
        return
    
    @abstractmethod
    def end_action(self, app, target):
        return
    
    
class Alice(User):
    id = 0
    def __init__(self, name: str):
        super().__init__(name + str(id))
        id += 1

    def begin_action(self, app):
        #make packets
        return super().begin_action(app)
    
    def end_action(self, app, target):
        # send packets to bob
        return super().end_action(app, target)
    
class Bob(User):
    id = 0
    def __init__(self, name: str):
        super().__init__(name + str(id))
        id += 1
            