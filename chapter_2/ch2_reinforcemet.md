## Reinforcement

### R-2.1

```python


```

### R-2.2


```python

```

### R-2.3


```python

```

### R-2.4

```python
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
      

```

### R-2.5
to revise the charge and make payment methods of the CreditCard class to ensure that the caller sends a number as a parameter.

```python

self.CORRECT_IDENTIFIER = "0000 0000 0000 0000"

def charge(self, price, identifier):
”””Charge given price to the card, assuming sufficient credit limit.
Return True if charge was processed; False if charge was denied.
”””
    if identifier == self.CORRECT_IDENTIFIER:
        if price + self. balance > self. limit:
            # if charge would exceed limit,
            return False
            # cannot accept charge
        else:
            self. balance += price
            return True
    else:
        raise ValueError("correct card number must be given")


def make payment(self, amount, identifier):
”””Process customer payment that reduces balance.”””

    
    if identifier == self.CORRECT_IDENTIFIER:
        self. balance −= amount
    else:
        raise ValueError("correct card number must be given")
```

### R-2.6

```python

def make payment(self, amount, identifier):
”””Process customer payment that reduces balance.”””

    assert amount >= 0, "amount added must be positive"
    
    if identifier == self.CORRECT_IDENTIFIER:
        self. balance −= amount
    else:
        raise ValueError("correct card number must be given")

```

### R-2.7

```python

class CreditCard:
”””A consumer credit card.”””
    def init (self, customer, bank, acnt, limit, inital_balance = 0):
    ”””Create a new credit card instance.
    The initial balance is zero.    customer the name of the customer (e.g., John Bowman )
    bank    the name of the bank (e.g., California Savings )
    acnt    the acount identifier (e.g., 5391 0375 9387 5309 )
    limit   credit limit (measured in dollars)
    ”””
    self. customer = customer
    self. bank = bank
    self. account = acnt
    self. limit = limit
    self. balance = 0 + initial_balance

```

### R-2.8


```python

```

### R-2.9

```python

def __sub__(self, other):
    if len(self) != len(other):
        raise ValueError("Vector must be of the same length")
    else:
        answer = Vector(len(self))
        for n in range(len(self)):
            answer[n] = self[n] - other[0]
        return answer
```

### R-2.10

```python

def __neg__(self):
    for n in range(len(self)):
        self[n] = -self[n]
    return self 

```

### R-2.11


```python

```

### R-2.12


```python

```

### R-2.13


```python

```

### R-2.14


```python

```

### R-2.15


```python

```

### R-2.16


```python

```

### R-2.17


```python

```

### R-2.18


```python

```

### R-2.19


```python

```

### R-2.20


```python

```

### R-2.21


```python

```

### R-2.22


```python

```

### R-2.23


```python

```
