
import random as r
import numpy as np
import pandas as pd

from user_interface_tool import make_function_array_into_buttons

import tkinter 
import tkinter as tk

root = tk.Tk()
string_variable = tk.StringVar(root)
string_variable.set("")
LB = tk.Label(root, textvariable = string_variable)
LB.grid(row=2, column=0, columnspan=3)

class WordManager():
  def __init__(self, path = "vocab_data\japanese_vocabulary_words.csv"):
    self.data = pd.read_csv(path)
  def load_words(self, path = "vocab_data\japanese_vocabulary_words.csv"):
    self.data = pd.read_csv(path)
  


def clear_label(the_label = LB):
  string_variable.set('')

def get_word():
  df = VocabManager.data
  # max_location = df.index - 1
  # df.Index.size
  # max_location = 0
  max_location = df.index.size -1
  location = r.randint(0, max_location)
  all_word_data = df.loc[location]
  string_variable.set(f"{all_word_data}")

def new_word():
  pass
  
VocabManager = WordManager()




"""expect to use
pandas to read csv data

tkinter to display a gui
buttons, label

data in 
romanji, japanese characters, and english words

random for getting a random japanese word to test on
"""

def main():
  vocab_functions = [[get_word, clear_label
  # , new_word  
  ]]
  texts = [["example", "clear",
  #  "new word"
  ]]
  make_function_array_into_buttons(root, vocab_functions, texts = texts)
  root.mainloop()

if __name__ == "__main__":
  main()
