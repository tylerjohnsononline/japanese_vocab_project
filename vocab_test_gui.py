
import random as r
import numpy as np
import pandas as pd

from user_interface_tool import make_function_array_into_buttons

import tkinter 
import tkinter as tk
# from tkinter import *
from tkinter import filedialog

root = tk.Tk()
string_variable = tk.StringVar(root)
string_variable.set("")
LB = tk.Label(root, textvariable = string_variable)
LB.grid(row=10, column=0, columnspan=3)
# japanese word 
active_language = tk.StringVar(root)
active_language.set("")
language_show = tk.Label(root, textvariable = active_language)
language_show.grid(row=1, column=1, )

non_english_word = tk.StringVar(root)
non_english_word.set("")
non_english_label = tk.Label(root, textvariable = non_english_word)
non_english_label.grid(row=1, column=1, )

english_word = tk.StringVar(root)
english_word.set("")
english_word_button = tk.Label(root, textvariable = english_word)
english_word_button.grid(row=1, column=2)

pronunciation = tk.StringVar(root)
pronunciation.set("")
pronunciation_show = tk.Label(root, textvariable = pronunciation)
pronunciation_show.grid(row=1, column=3, )
#####
example1 = tk.StringVar(root)
example1.set("")
example1_show = tk.Label(root, textvariable = example1)
example1_show.grid(row=2, column=1, )

example2 = tk.StringVar(root)
example2.set("")
example2_show = tk.Label(root, textvariable = example2)
example2_show.grid(row=2, column=2, )

example3 = tk.StringVar(root)
example3.set("")
example3_show = tk.Label(root, textvariable = example3)
example3_show.grid(row=2, column=3, )

class WordManager():
  def __init__(self, path = "vocab_data\\japanese_vocabulary_words.csv"):
    self.current_path = path
    self.data = pd.read_csv(self.current_path)
    self.active_word_location = 0
    # japanese,pronunciation,english

    # print(self.active_word)
  def load_words(self):
    self.data = pd.read_csv(self.current_path)
  def load_given_words(self, path = "vocab_data\\japanese_vocabulary_words.csv"):
    self.data = pd.read_csv(path)
  def get_word(self): #, place = False# if != False:set active_word_location
    df = self.data
    max_location = df.index.size -1
    location = r.randint(0, max_location)
    all_word_data = df.loc[location]
    self.active_word_location = location
    string_variable.set(f"{all_word_data}")
  def example_shower(self):
    df  = self.data
    example1.set(df.loc[self.active_word_location][df.columns[0]])
    example2.set( df.loc[self.active_word_location]["english"])
    example3.set(df.loc[self.active_word_location]["pronunciation"])

  def show_japanese(self):
    df  = self.data
    japanese_word = df.loc[self.active_word_location]["japanese"]
    non_english_word.set(f"{japanese_word}")
    # non_english_label.configure(text = non_english_word)
  def show_active_non_english(self):
    df  = self.data
    languages_word = df.loc[self.active_word_location][df.columns[0]]
    non_english_word.set(f"{languages_word}")

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
    max_location = df.index.size -1
    location = r.randint(0, max_location)
    all_word_data = df.loc[location]
    self.active_word_location = location
  def get_and_show_nonenglish(self):
    df = self.data
    max_location = df.index.size -1
    location = r.randint(0, max_location)
    all_word_data = df.loc[location]
    self.active_word_location = location
    self.show_active_non_english()
  def choose_your_csv_data(self):
    self.current_path = filedialog.askopenfilename()
    self.load_words()
  def show_all(self):
    pass
  def clear_tkinter_shown(self):
    non_english_word.set("")
    english_word.set(f"")
    pronunciation.set(f"")
    self.show_active_non_english()

def clear_label(the_label = LB):
  string_variable.set('')
def clear_example():
    example1.set(f"")
    example2.set(f"")
    example3.set(f"")

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

[VocabManager.clear_tkinter_shown,VocabManager.show_active_non_english,VocabManager.choose_your_csv_data]
def nonfunction():
  pass
def main():
  vocab_functions = [[VocabManager.get_and_show_nonenglish,nonfunction,VocabManager.example_shower, clear_example],
          [VocabManager.show_active_non_english],[VocabManager.show_english],[VocabManager.show_romanji],
          # [VocabManager.choose_your_csv_data],
          [VocabManager.clear_tkinter_shown,VocabManager.show_active_non_english,VocabManager.choose_your_csv_data]
          # [VocabManager.clear_tkinter_shown],[VocabManager.show_active_non_english],[VocabManager.choose_your_csv_data]
                      ]
  
  # current_language = f"show\n{VocabManager.data.columns[0]}\nnew"

  texts = [["new\nword", "","example", "clear\nexample",], # answer
           ["non-english"],["show\nenglish"],["show\nphonetic"],
          #  [f"new language"],
          ["clear non_active word","nonenglish","new_data"]

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