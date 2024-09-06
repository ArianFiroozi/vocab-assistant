import pandas as pd

with open("word.txt", "r") as file:
    words = file.readlines()

words = [word.strip() for word in words]