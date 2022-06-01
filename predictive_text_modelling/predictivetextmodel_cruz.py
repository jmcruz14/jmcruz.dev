#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -------

# import, export, plotting libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sms_raw_df = pd.read_csv("/Users/jccruz/Desktop/School Documents/UP Diliman/AY 2021-2022/IE 198/Capstone Case/Spam.csv",
                     encoding= 'unicode_escape')

spam_msg = sms_raw_df[sms_raw_df.Class == 'spam']
legit_msg = sms_raw_df[sms_raw_df.Class == 'legit']
#%%
# Downsampling legit messages
legit_msg_df = legit_msg.sample(n = len(spam_msg), random_state = 30)
spam_msg_df = spam_msg
sms_df = spam_msg.append(legit_msg_df).reset_index(drop=True)
#%%
# Mapping into array
sms_df['msg_type'] = sms_df['Class'].map({'legit': 0, 'spam': 1})
sms_label = sms_df['msg_type'].values
sms_label = np.asarray(sms_label).astype(np.int32)

#%%
# library for train test split
from sklearn.model_selection import train_test_split

# Split into Train and Test Data
train_sms, test_sms, train_labels, test_labels = train_test_split(sms_df['Text'], sms_label, test_size = 0.25, random_state = 100) #75/25 split (train / test)
#%%
# deep learning libraries for text pre-processing
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Hyperparameters for Tokenization
max_len = 60 # Maximum length of each sentence when tokenized and fed to the model
trunc_type = "post"
padding_type = "post"
oov_tok = "<X>"
vocab_size = 1000

# Turn into array
#train_labels = np.asarray(train_labels).astype(np.float32)
#test_labels = np.asarray(test_labels).astype(np.float32)

# Tokenizer Parameters
tokenizer = Tokenizer(num_words = vocab_size, char_level = False, oov_token = oov_tok)
tokenizer.fit_on_texts(train_sms)
tokenizer.fit_on_texts(test_sms)

# Sequencing representation
train_sequences = tokenizer.texts_to_sequences(train_sms)
train_padded = pad_sequences(train_sequences, maxlen = max_len, padding = padding_type,
                             truncating = trunc_type)

test_sequences = tokenizer.texts_to_sequences(test_sms)
test_padded = pad_sequences(test_sequences, maxlen = max_len, padding = padding_type,
                            truncating = trunc_type)
#%%

# Modeling with Neural Networks
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Dense, Dropout, Conv1D, GlobalAveragePooling1D

vocab_size = 1000
embeding_dim = 32

Model = Sequential()
Model.add(Embedding(vocab_size, embeding_dim, input_length=60))
Model.add(GlobalAveragePooling1D())
Model.add(Dense(24, activation='relu'))
Model.add(Dense(48, activation='relu'))
Model.add(Dropout(0.20)) # Prevent overfitting
Model.add(Dense(1, activation='sigmoid')) # Predict average class accuracy of spam and legit

Model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy', 'mean_squared_error'])

early_stop = EarlyStopping(monitor='val_loss',patience=2) #Overfitting account 2
Model.fit(train_padded, train_labels, epochs=15, validation_data=(test_padded, test_labels),
          callbacks=[early_stop], verbose=2)
Model.metrics_names

print(Model.summary())

loss = pd.DataFrame(Model.history.history)
loss[['accuracy','loss']].plot() 
loss[['val_accuracy','val_loss']].plot()
loss[['val_mean_squared_error', 'val_loss']].plot()

#%% 
from sklearn.metrics import confusion_matrix, classification_report

text_predictions = Model.predict(test_padded)
text_predictions_rounded = np.round(text_predictions)
cm = confusion_matrix(np.round(test_labels), text_predictions_rounded)

print("Confusion Matrix:", "\n", confusion_matrix(np.round(test_labels),text_predictions_rounded))
print(classification_report(np.round(test_labels), text_predictions_rounded))

print("'Spam' accuracy: {}%".format(round((cm[0][0]/(cm[0][0] + cm[0][1])*100), 2)))
print("'Legit' accuracy: {}%".format(round(((cm[1][1]/(cm[1][0]+cm[1][1])))*100, 2)))

