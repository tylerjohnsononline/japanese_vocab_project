
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
LB.grid(row=10, column=0, columnspan=3)
# japanese word 
japanese_word_displayable = tk.StringVar(root)
japanese_word_displayable.set("")
japanese_label = tk.Label(root, textvariable = japanese_word_displayable)
japanese_label.grid(row=1, column=1, )

english_word = tk.StringVar(root)
english_word.set("")
english_word_button = tk.Label(root, textvariable = english_word)
english_word_button.grid(row=1, column=2)

pronunciation = tk.StringVar(root)
pronunciation.set("")
romanji_button = tk.Label(root, textvariable = pronunciation)
romanji_button.grid(row=1, column=3, )


class WordManager():
  def __init__(self, path = "vocab_data\japanese_vocabulary_words.csv"):
    self.data = pd.read_csv(path)
    self.active_word_location = 0
    # japanese,pronunciation,english

    # print(self.active_word)
  def load_words(self, path = "vocab_data\japanese_vocabulary_words.csv"):
    self.data = pd.read_csv(path)
  def get_word(self): #, place = False# if != False:set active_word_location
    df = self.data
    # max_location = df.index - 1
    # df.Index.size
    # max_location = 0
    max_location = df.index.size -1
    location = r.randint(0, max_location)
    all_word_data = df.loc[location]
    self.active_word_location = location
    string_variable.set(f"{all_word_data}")
  def show_japanese(self):
    df  = self.data
    japanese_word = df.loc[self.active_word_location]["japanese"]
    japanese_word_displayable.set(f"{japanese_word}")
    # japanese_label.configure(text = japanese_word_displayable)
  def show_english(self):
    df  = self.data
    english = df.loc[self.active_word_location]["english"]
    english_word.set(f"{english}")
  def show_romanji(self):
    df  = self.data
    romanji = df.loc[self.active_word_location]["pronunciation"]
    pronunciation.set(f"{romanji}")
  def get_no_show(self):
    df = self.data
    # max_location = df.index - 1
    # df.Index.size
    # max_location = 0
    max_location = df.index.size -1
    location = r.randint(0, max_location)
    all_word_data = df.loc[location]
    self.active_word_location = location
    # string_variable.set(f"{all_word_data}")



def clear_label(the_label = LB):
  string_variable.set('')


# def new_word():
#   pass
  
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
  vocab_functions = [[VocabManager.get_no_show,VocabManager.get_word, clear_label],
          [VocabManager.show_japanese],[VocabManager.show_english],[VocabManager.show_romanji]
  # , new_word  
                      ]
  texts = [["new\nword", "example", "clear",], # answer
           ["show\njapanese\nnew"],["show\nenglish"],["show\nphonetic"],
  #  "new word"
  ]
  btns = make_function_array_into_buttons(root, vocab_functions, texts = texts)
  for outer_index, xx in enumerate(texts):
    for inner_index, __  in enumerate(xx):
      print(btns[outer_index][inner_index])
      btns[outer_index][inner_index].configure(width=10)
      btns[outer_index][inner_index].grid(row=inner_index,column=outer_index)
      # btns[outer_index][inner_index].configure(row=inner_index,column=outer_index)
  root.mainloop()

if __name__ == "__main__":
  main()