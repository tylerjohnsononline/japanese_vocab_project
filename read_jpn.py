
import numpy as np
import pandas as pd

save_location = "vocab_data\\japanese_vocabulary_words.csv"
# df.to_csv(save_location)

data = pd.read_csv(save_location)
print(data)