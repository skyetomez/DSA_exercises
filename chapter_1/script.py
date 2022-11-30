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



if __name__ == '__main__':

    print("Testing".center(4,"$"))

    tests = [
        [1,3,2,4,5,6,7],
        [1]*3,
        list(range(0,128,14)),
        [1,2,34,5,'a'],
        "This iss a sentence",
        "aaaaaeeeeeiiioooouuu",
        "abcedicefjaoalkj",
        "adlfj;ljaldkfadf81028alsfj123[]"

    ]
    for n in tests:
        print(function(n, 3))
    
    # function()


    print("complete")