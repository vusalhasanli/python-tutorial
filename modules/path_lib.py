from pathlib import Path
import os
import time

p = Path('.')

# print( [x for x in p.iterdir() if x.is_dir()]) # list dirs in current dir
# print( [x for x in p.iterdir() if x.is_file()]) # list files in current dir


# recipe = p / 'recipe.txt'
# print(recipe)

# ------>> iterating through dir and reading files

for x in p.iterdir():
    if x.is_file():
        print("Opening {}... ".format(x))
        time.sleep(2)
        with x.open() as input_file:
            files = input_file.readlines()
            # str(recipes.strip())
            for r in files:
                print(r)