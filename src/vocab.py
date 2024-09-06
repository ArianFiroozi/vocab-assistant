import pandas as pd
import pickle
import random
from src.word import Word

class Vocab:
    def __init__(self, address="../vocab.txt"):
        self.address=address
        self.words=self.read_file(address)

    def get_new_words(self, num=10, random_order=False):
        new_words=[]
        if random_order:
            for word in random.sample(self.words, len(self.words)):
                if word.show_again==True and word.read==False:
                    word.set_read(True)
                    new_words.append(word)

                if len(new_words)==num:
                    return new_words
        else:
            for word in self.words:
                if word.show_again==True and word.read==False:
                    word.set_read(True)
                    new_words.append(word)

                if len(new_words)==num:
                    return new_words

        print("Not that many words left!")
        return new_words

    def get_read_words(self, num=10, random_order=False):
        read_words=[]
        if random_order:
            for word in random.sample(self.words, len(self.words)):
                if word.show_again==True and word.read==True:
                    read_words.append(word)

                if len(read_words)==num:
                    return read_words
        else:
            for word in self.words:
                if word.show_again==True and word.read==True:
                    read_words.append(word)

                if len(read_words)==num:
                    return read_words

        print("Not that many words read!")
        return read_words

    def read_file(self, address):
        with open("./vocab.txt", "r") as file:
            words = file.readlines()
        return [Word(word.strip()) for word in words]

    def save(self, address="./src/cache/history.pkl"):
        with open(address, "wb") as file:
            pickle.dump(self.words, file)

    def load(self, address="./src/cache/history.pkl"):
        try:
            with open(address, "rb") as file:
                self.words = pickle.load(file)
        except:
            print("No file to load!")

    def reset(self):
        self.words.clear()
        self.words=self.read_file(self.address)
