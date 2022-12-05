import re 

#contextual parsing strategy#

class Function:
    """
    This is a base class to handle arithmetic and creation of the polynomials
    """
    def __init__(self, polynomial:str):
        self._poly = polynomial
        self._poly_str = polynomial.strip().replace(" ","")
        self._poly_dict = self._make_dict_()
        
        
    def __str__(self):
        return self._poly_str
    
    def _powers(self):
        reg = re.compile(r"x(\^\-?\d*\/?\d*)?")
        m = re.search(reg, self._poly_str)
        self._powers = [ float(o.replace("^", "")) for o in m]
        self._powers += "0"
        return self._powers
        
    def _constant(self):
        reg = re.compile(r"")
    
    def _make_dict_(self):
        
        for power in self._powers:
            
            if power == "0":
                power = float(power)
                self._poly_dict[power] = #constant in string
            else:    
                power_index = self._poly_str.find(power)
                coeff_index = power_index-2
                coeff = float(self._poly_str[coeff_index])
                
            if power not in self._poly_dict:
                power = float(power)
                self._poly_dict[power] = coeff
            else:
                power = float(power)
                self._poly_dict[power] += coeff
        
        return self._poly_dict
    
    def _make_str_(self):
        
        sorted_dict = sorted(self._poly_dict.items())
        string = ""
        
        for k, v in sorted_dict:
            tmp = str(v) + "x^" + str(k)
            string+= tmp
        return string
    
class Polynomial:
    """
    This is s class for a general polynomial x
    This has ways for editing and displaying them. 
    """
    def __init__(self, polynomial:str):
        self._poly = polynomial
    
    def __str__(self) -> str:
        return self._poly.strip().replace(" ","")
    
    def __len__(self):
        pass
    
    def __getitem__(self):
        pass
     
    

if __name__ == "__main__":
    
    tmp =  Polynomial("x^2+3x + 2x+3")
    print(tmp)