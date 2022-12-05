import random
from animals import Bear, Fish

class River:
    
    def __init__(self, length = 15):
        self.river = ['0'] * length
        self.length = length
        self._riverdict = dict.fromkeys(self.river,[0])
    
    
    def _moveamount(self) -> int:
        move = random.randint(0,self.length)
        return move
    
    def _moveplayers(self, animal):
        
        for piece in self.river:
            place = self._moveamount()
            self._riverdict.insert(place, piece)
            
    def _gamelogic(self):
        
        for k,v in self._riverdict:
            if not all(v) and isinstance(v,Bear):
                v.remove(Bear)
            if all(v) and len(v) > 1:
                rndplayer = random.randint(0,len(rndplayer))
                self._moveplayers(v[rndplayer])
                del v[rndplayer]
