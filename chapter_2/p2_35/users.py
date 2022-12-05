# from abc import abstractmethod
import iot

class User:
    """abstract baseclass for users of applications"""
    def __init__(self,name:str):
        self.name = name
        self.packets = []
        self.actions = ["read", "delete"]
    
   
    def _delete(self, app:iot):
        name  = str(app._packetheap[0].keys())
        packets = str(app._packetheap[0].values())
        print(f"packets {packets} from {name} were deleted")
    
    def _read(self, app:iot):
        print(f"The packets are: {app._packetheap}")
   
    # @abstractmethod
    def begin_action(self, app):
        return
    
    # @abstractmethod
    def end_action(self, app, target):
        return
    
    
class Alice(User):
    
    def __init__(self, name = "Alice"):
        self.name = name

    def begin_action(self, app:iot):
        print(f"{self.name} is using an application.")
        app._sendpackets('Bob')
    
class Bob(User):
    def __init__(self, name="Bob"):
        self.name = name
                                 
    def begin_action(self, app:iot):
        print(f"{self.name} is using an application.")
        # read packets
        super()._read(app)
        # delete packets
        super()._delete(app)
    