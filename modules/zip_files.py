import gzip
import bz2
import zipfile
from zipfile import ZipFile



with ZipFile('sample.zip') as input_file:
    print(input_file.namelist()) #['recipe.txt', 'scrabble.txt']
    input_file.extractall()




