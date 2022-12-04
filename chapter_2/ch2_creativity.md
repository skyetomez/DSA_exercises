## Creativity questions

### C-2.24

Buy book

View lists

Read book

### C-2.25

```python

  def __mul__(self, other):
    
    if isinstance(other, int) or isinstance(other,float): 
      result = Vector(len(self))
      for n in range(len(self)):
          result[n] = n * other
      return result 

    elif isinstance(other, Vector): 
        dot_prod = 0
        if len(self) == len(other):
            for n in range(len(self)):
                dot_prod += self[n] + other[n]
            return dot_prod
        else: 
            raise ValueError("Vectors must be of the same dimension")
    else:
        raise ValueError("Improper value")


```


### C-2.26

```python
class ReversedSequenceIterator:
  """A reversed iterator for any of Python's sequence types."""

  def __init__(self, sequence):
    """Create an iterator for the given sequence."""
    self._seq = sequence          # keep a reference to the underlying data
    self._k = len(list(sequence)) + 1                  # will increment to 0 on first call to next

  def __str__(self):
    result = list(map(str, list(self._seq)))
    string = ",".join(result)
    return string
  
  def __next__(self):
    """Return the next element, or else raise StopIteration error."""
    self._k -= 1                  # advance to next index
    if self._k > -1:
      return(self._seq[self._k])  # return the data element
    else:
      raise StopIteration()       # there are no more elements

  def __iter__(self):
    """By convention, an iterator must return itself as an iterator."""
    return self

```

### C-2.27

```python
def __contains__(self, val):
    """Return True if val found in the sequence; False otherwise."""
    if val in self:                          # found match
        return True
    else:
        return False

```

### C-2.28
```python
class PredatoryCreditCard(CreditCard):
  """An extension to CreditCard that compounds interest and fees."""
  
  def __init__(self, customer, bank, acnt, limit, apr):
    """Create a new predatory credit card instance.

    The initial balance is zero.

    customer  the name of the customer (e.g., 'John Bowman')
    bank      the name of the bank (e.g., 'California Savings')
    acnt      the acount identifier (e.g., '5391 0375 9387 5309')
    limit     credit limit (measured in dollars)
    apr       annual percentage rate (e.g., 0.0825 for 8.25% APR)
    """
    super().__init__(customer, bank, acnt, limit)  # call super constructor
    self._apr = apr
    self._uses = 0
    self._penalty = False
    self._surcharge = 1
    
  def charge(self, price):
    """Charge given price to the card, assuming sufficient credit limit.

    Return True if charge was processed.
    Return False and assess $5 fee if charge is denied.
    """
    self.uses()
    success = super().charge(price)          # call inherited method

    if self._penalty:
      success = super().charge(self._surcharge)
    if not success:
      self._balance += 5                     # assess penalty
    return success                           # caller expects return value

  def process_month(self):
    """Assess monthly interest on outstanding balance."""
    if self._balance > 0:
      # if positive balance, convert APR to monthly multiplicative factor
      monthly_factor = pow(1 + self._apr, 1/12)
      self._balance *= monthly_factor
      
  def uses(self):
    
    if self._uses == 10:
      self._penalty = True
      pass
    self._uses +=1
```

### C-2.29

```python

class PredatoryCreditCard(CreditCard):
  """An extension to CreditCard that compounds interest and fees."""
  
  def __init__(self, customer, bank, acnt, limit, apr):
    """Create a new predatory credit card instance.

    The initial balance is zero.

    customer  the name of the customer (e.g., 'John Bowman')
    bank      the name of the bank (e.g., 'California Savings')
    acnt      the acount identifier (e.g., '5391 0375 9387 5309')
    limit     credit limit (measured in dollars)
    apr       annual percentage rate (e.g., 0.0825 for 8.25% APR)
    """
    super().__init__(customer, bank, acnt, limit)  # call super constructor
    self._apr = apr
    self._uses = 0
    self._penalty = False
    self._surcharge = 1
    
  def charge(self, price):
    """Charge given price to the card, assuming sufficient credit limit.

    Return True if charge was processed.
    Return False and assess $5 fee if charge is denied.
    """
    self.uses()
    success = super().charge(price)          # call inherited method

    if self._penalty:
      success = super().charge(self._surcharge)
    if not success:
      self._balance += 5                     # assess penalty
    return success                           # caller expects return value

  def process_month(self):
    """Assess monthly interest on outstanding balance."""

    if self._balance > 0:
      # if positive balance, convert APR to monthly multiplicative factor
      monthly_factor = pow(1 + self._apr, 1/12)
      self._balance *= monthly_factor
      self._monthly_payment_check()
      self._set_monthly_payment()
      
  def uses(self):
    
    if self._uses == 10:
      self._penalty = True
      pass
    self._uses +=1

  def _set_monthly_payment(self):
    self._monthly_payment = self._balance * 0.1

  def _monthly_payment_check(self):
    late_fee = 10.00
    if self.monthly_payment !=0:
        super().charge(late_fee)



```

### C-2.30

```python
def _set_balance(self, new):
    self._balance = new
```

### C-2.31

```python
class AbsoluteDifferenceProgression(Progression):
  
  def __init__(self, first = 2, second = 200):
    
    super().__init__(first)
    self._prev1 = abs(first - second)
    self._prev2 = 0
    
  def _advance(self):
      self._prev2 = self._prev1
      self._prev1 = self._current
      self._current = self._current +  abs(self._prev1 - self._prev2)

```

### C-2.32

```python

import math      
class SquareRootProgression(Progression):
  
  def __init__(self, start = 65536):
    
    super().__init__(start)
    self._prev1 = 0
    
  def _advance(self):
      self._prev1 = self._current
      self._current = math.sqrt(self._current)

```