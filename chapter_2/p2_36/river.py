import random
from animals import Bear, Fish

class River:
    """
    This class is the game board for the fish and bear game. 
    """
    def __init__(self, length = 15):
        self.length = length
        self.empty_tile = [[] for _ in range(length)] 
        self.river = list(range(1, self.length + 1))
        self._riverdict = dict(zip(self.river, self.empty_tile))
        
   
    def start(self, animal1, animal2):
        self._riverdict[1].append(animal1)
        self._riverdict[15].append(animal2)
    
    def _moveamount(self) -> int:
        move = random.randint(0,3)
        return move
    
    def _moveplayers(self):
        for tile, piece in self._riverdict.items():
            
            if len(piece) > 0 and isinstance(piece[-1], (Bear,Fish)):
                tmp = piece[-1]
                self._riverdict[tile].remove(piece[-1])
                new_spot = ((tile + self._moveamount()) % self.length) + 1
                self._riverdict[new_spot].append(tmp)
            
            elif len(piece) > 1: 
                for i in piece:
                    self._riverdict[tile].remove(i)
                    new_spot = ((tile + self._moveamount()) % self.length) + 1
                    self._riverdict[new_spot].append(i)
            else:
                pass
            
        self._gamelogic()
            
    def _gamelogic(self):
        
        for k,v in self._riverdict.items():
            bear_filter = list(map(lambda n: isinstance(n, Bear), v))
            fish_filter = list(map(lambda n: isinstance(n, Fish), v))
            
            if not all(bear_filter):
                v = [i for (i, j) in zip(v, bear_filter) if j]
                self._riverdict[k] = v   
                                 
            if all(fish_filter) and len(fish_filter) > 1 or all(bear_filter) and len(bear_filter) > 1:
                rndplayer = random.randint(0,len(v))
                self._moveplayers(v[rndplayer])
                del v[rndplayer]
