"""
Write a Python program that inputs a document and then outputs a bar-
chart plot of the frequencies of each alphabet character that appears in
that document.
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import os
from string import ascii_lowercase

TEST_DOC = "/home/gear/Github/DSA_exercises/chapter_2/ipsum.txt"

class File:
    """Prepare a file object to output a barchart of the frequencies of each alphabet
    character in a text document
    This requires seaborn, pandas, matplotlib.pyplot, os and ascii_lowercase from the
    python string module 
    """
    def __init__(self, file_path:str):
        self._fpath  = file_path
        self._raw_object = self._openfile()
    """
    
    file_path           the absolute path to the textdocument
    frequenc_plot()     call to plot the frequencies of letters
    """

    def _openfile(self): #opens file in read mode
        with open(self._fpath, 'r') as fn:
            data = fn.read()
        return data
    
    def _clean(self): #removes new line characters
        self._clean_object = self._raw_object.replace("\n", "")

    def _count_letters(self) -> dict: #counts the letters 
        self._clean()
        
        count = 0 
        letter_counts = list()
        for letter in ascii_lowercase:
            for n in self._clean_object:
                if letter == n:
                    count += 1
            
            letter_counts.append(count)
        
        self._dict = dict(zip(list(ascii_lowercase), letter_counts))
        
        return self._dict
    
    def frequency_plot(self):
        """
        Returns a plot of the letter frequencies in the document
        """
        counts = self._count_letters()
        
        name = os.path.split(TEST_DOC)[-1]
        
        self.df = pd.DataFrame(counts, index = [0], columns=list(ascii_lowercase))
        
        sns.barplot(data =self.df,
                    errorbar= "sd")
        
        
        plt.title(f"Bar chart of frequency of letters in {name}")
        plt.xlabel("letter")
        plt.ylabel("number of occurances")
        plt.show()
        
    def print(self):
        print(self._object)
        



if __name__ == "__main__":

    tmp = File(TEST_DOC)

    tmp.frequency_plot()

