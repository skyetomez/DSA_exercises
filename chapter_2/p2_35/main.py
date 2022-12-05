import iot
import users





if __name__ == "__main__":

    alice = users.Alice()
    bob = users.Bob()
    
    facebook = iot.Application("facebook")
    
    alice.begin_action(facebook)
    print(facebook._packetheap)
    
    bob.begin_action(facebook)