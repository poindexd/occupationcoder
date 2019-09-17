import nltk
import pandas as pd
from occupationcoder.coder import coder

nltk.download('wordnet')
nltk.download('punkt')

myCoder = coder.Coder()

if __name__ == '__main__':
    print(myCoder.codejobrow('Physicist','Calculations of the universe','Professional scientific'))
    print(myCoder.codejobrow('Software Engineer','',''))