

import numpy as np
import pandas as pd

# data = [["私","watashi","I"], ["助けて","Tasukete", "help me"]]
data = {"japanese" : ["私", "助けて"],
        "pronunciation/romanji":["watashi", "tasukete"],
        "english": ["I", "help me"]
        }
df= pd.DataFrame(data)

print(df)


save_location = "vocab_data\\japanese_vocabulary_words.csv"
df.to_csv(save_location)
# data = pd.read_csv("")
