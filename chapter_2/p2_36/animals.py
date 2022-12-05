import random
from string import ascii_uppercase, digits

class Animal:
    id_list = list()
    
    def __init__(self) -> None:
        self.id = self._genid()

    def _genid(self):
        rnd = list(ascii_uppercase + digits)
        id = "".join(map(str,random.choices(rnd, k=8)))
        
        self._checkid(id)
        self.id_list.append(id)
        return id
    
    def _checkid(self, id):
        if id in self.id_list:
            print("generating new id")
            self._genid()
            
class Bear(Animal):
    def __init__(self) -> None:
        super().__init__()
        
    def __str__(self):
        return "Bear" + '#' + self.id
    def __repr__(self):
        return "Bear" + '#' +self.id
    
class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()
  
    def __str__(self):
        return "Fish" + '#' + self.id
    def __repr__(self):
        return "Fish" + '#' + self.id

    
    

if __name__ == "__main__":
    
    bears = list()
    fishes = list()
    
    for _ in range(30):
        bears.append(Bear())
        fishes.append(Fish())
    
    for n in range(len(bears)):
        print(bears[n].id)
        
    for n in range(len(fishes)):
        print(fishes[n].id)
