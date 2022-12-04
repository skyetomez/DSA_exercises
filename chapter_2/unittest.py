class Flower:
    """ 
    This is a python Flower. It can change in price, petal count and value

    set_type        updates type of flower
    set_npetals     updates number of petals
    set_price       updates price 
    """
    def __init__(self, species = "bud", npetals = 0, price= 0.00):
        self.species = "bud"
        self.npetals = 0
        self.price = 0.
    
    def set_type(self, type:str):
        
        assert isinstance(type, str), "n must be a string"
        
        self.species = type

    def set_npetals(self, n:int):
        
        assert isinstance(n, int), "n must be an integer"
        
        self.npetals = n

    def set_price(self, new_price:float):
        
        assert isinstance(new_price, float), "new_price must be of type float"
        
        self.price = new_price

    def get_type(self):
        return self.species

    def get_npetals(self):
        return self.npetals

    def get_price(self):
        
        price = '$' + str(round(self.price, 2))
        return price
      