## Creativity questions

### C-1.14

Notice that the product of two even numbers is even and an odd and even number is still even so we only need to consider odd pairs. It is enough acknolwedge that there are 2 odd numbers in the list.

```python

def function(sequence:list) -> str:
    
    counter = 0 

    for integer in sequence:
        if integer % 2 != 0:
            tmp = integer
            counter += 1
            if counter == 2:
                return print("A distinct pair exists.")
    
    return print("No pair exists")

```

### C-1.15

```python

def function1(sequence:list) -> None:
    tmp = set(sequence)
    distinct = bool(len(sequence) == len(tmp))


    if distinct:
        print("There is a distinct pair of numbers in the sequence whose product is odd")
    else:
        print("There is not a distinct pair of numbers in the sequence whose product is odd")

    
    return None

def function2(sequence:list) -> None:
    tmp = set(sequence)

    print("Yes there is.") if len(sequence) == len(tmp) else print("No.")

    return None


```

### C-1.18

```python
print([i*(i+1) for i in range(10)])
```

### C-1.19

```python
from string import ascii_lowercase

print(list(ascii_lowercase))
```

### C-1.20

```python
import random
random.seed(0000)

def function(seq:list) -> list:
    len_ = len(seq) -1

    arr_ind = list()

    while len(arr_ind) != len(seq):
        shuffle_ = random.randint(0, len_)

        if shuffle_ not in arr_ind:
            arr_ind.append(shuffle_)


    tmp = list()

    for ind in arr_ind:
        tmp.append(seq[ind])

    return tmp

```

```python
import random

def function(seq:list) -> list:
    random.seed(0000)

    n = len(seq)
    arr_ind = range(0, n)
    ind = list(random.sample(arr_ind, n))

    tmp = [seq[i] for i in ind]

    return tmp


```

### C-1.21

```python

def function() -> None:
    
    e = False
    tmp = list()

    while not e:
        try:
            line = input()
            tmp.append(line)
            if line == "":
                print("Reversing string")
                tmp.reverse()
                
                for n in tmp:
                    print(n) 
                
                e = True
                
        except EOFError as e:
            print("End of File reached!")
            print("Reversing string")
            tmp.reverse()
            for n in tmp:
                print(n)
            break
            
    return None
```

### C-1.22

There is a typo in the question. Dot products return scalars

```python

def function(vec1:list, vec2:list) -> int:
    
    assert all(map(lambda n: isinstance(n, int), vec1)), "Must all be type int"
    assert all(map(lambda n: isinstance(n, int), vec2)), "Must all be type int"
    
    _product = sum([a*b for a,b in zip(vec1,vec2)])
    
    return _product

```

### C-1.23

```python
from typings import Any
def function(array:list, index:int, item:Any) -> list

    try:
        array.insert(index, item)
    except:
        print("Don’t try buffer overflow attacks in Python!")
    return array
```

### C-1.24

```python

def function(string:str) -> int:
    vowels = 'aeiou'
    count = 0 
    for n in string:
        
        if isinstance(n, str):
            
            if n in vowels:
                count +=1
    
    return count

```

### C-1.25

```python

def function() -> None:
    items = list()
    while len(items) != 3:
        item = input()
        items.append(item)
    
    a,b,c = list(map(int,items))
    
    print(f"{a+b==c}")
    print(f"{a-b==c}")
    print(f"{a*b==c}")
    print(f"{a/b==c}")
    print(f"{a%b==c}")
    print(f"{a==b+c}")
    print(f"{a==b-c}")
    print(f"{a==b*c}")
    print(f"{a==b/c}")
    print(f"{a==b%c}")

```

### C-1.27

```python
import math

def helpfunc(v:list) -> bool:
    
    logic = all(map(lambda n: isinstance(n, (int,float)), v))
    
    return logic

def function(v:list, p:int) -> float | None:
    
    if helpfunc(v):
        tmp = math.sqrt(sum([a**p for a in v]))
        tmp = round(tmp,2)
        return tmp
    else:
        pass 

    return None

```
