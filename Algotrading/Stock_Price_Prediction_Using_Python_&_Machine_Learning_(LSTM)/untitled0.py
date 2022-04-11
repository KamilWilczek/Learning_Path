# Description: This program uses an artificial recurrent neural network called Long Short Term Memory (LSTM)
#              to predict the closing stock price of a corporation (Apple Inc.) using past 60 day stock price.

# Import the libraries
import math
import pandas_datareader as web
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import RMSprop,Adam


# Get the stock quote
df = pd.read_csv(r'/home/kamil/Documents/ML/Stock_Price_Prediction_LSTM-computer_science_yt/archive/BTCUSD_day.csv')
df = df.iloc[::-1].reset_index(drop=True)

# Get the stock quote
df = web.DataReader("BTC-USD", data_source='yahoo', start='2012-01-01', end='2022-01-13')
# Show the data
df


# Get the numbers of rows and columns in the data set
df.shape


# Visualize the closing price hisotory
plt.figure(figsize=(16,8))
plt.title('Close price history')
plt.plot(df['Close'])
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close price USD ($)', fontsize=18)
# Visualize the open price hisotory
plt.figure(figsize=(16,8))
plt.title('Open price history')
plt.plot(df['Open'])
plt.xlabel('Date', fontsize=18)
plt.ylabel('Open price USD ($)', fontsize=18)
# Visualize the low price hisotory
plt.figure(figsize=(16,8))
plt.title('Low price history')
plt.plot(df['Low'])
plt.xlabel('Date', fontsize=18)
plt.ylabel('Low price USD ($)', fontsize=18)
# Visualize the high price hisotory
plt.figure(figsize=(16,8))
plt.title('High price history')
plt.plot(df['High'])
plt.xlabel('Date', fontsize=18)
plt.ylabel('High price USD ($)', fontsize=18)

# Create new dataframe with only the 'Close" column
data = df.filter(['Close', 'Open', 'High', 'Low'])
# Convert the dataframe to a numpy array
dataset = data.values
# Get the number of rows to train the model on
training_data_len = math.ceil(len(dataset) * .8)

training_data_len




# Create the training data set
# Create the scaled trainng data set
train_data = dataset[0:training_data_len, :]


# Create the testing data set
# Create a new array containing scaled values from index 1543 to 2003
test_data = dataset[training_data_len-60:, :]

# Scale the train data
scaler = MinMaxScaler(feature_range=(0,1))
scaled_train_data = scaler.fit_transform(train_data)

# Scale the test data
scaled_test_data = scaler.fit_transform(test_data)



# Split the data into x_train and y_train data sets
x_train_high = []
y_train_high = []
x_train_open = []
y_train_open = []
x_train_close = []
y_train_close = []
x_train_low = []
y_train_low = []



for i in range(60, len(scaled_train_data)):
    x_train_close.append(scaled_train_data[i-60:i, 0])
    y_train_close.append(scaled_train_data[i, 0])
    if i <= 60:
        print(x_train_close)
        print(y_train_close)
        print()

for i in range(60, len(scaled_train_data)):
    x_train_open.append(scaled_train_data[i-60:i, 1])
    y_train_open.append(scaled_train_data[i, 1])
    if i <= 60:
        print(x_train_open)
        print(y_train_open)
        print()

for i in range(60, len(scaled_train_data)):
    x_train_high.append(scaled_train_data[i-60:i, 2])
    y_train_high.append(scaled_train_data[i, 2])
    if i <= 60:
        print(x_train_high)
        print(y_train_high)
        print()

for i in range(60, len(scaled_train_data)):
    x_train_low.append(scaled_train_data[i-60:i, 3])
    y_train_low.append(scaled_train_data[i, 3])
    if i <= 60:
        print(x_train_low)
        print(y_train_low)
        print()


# Convert the x_train and y_train to numpy arrays
x_train_close, y_train_close = np.array(x_train_close), np.array(y_train_close)
x_train_open, y_train_open = np.array(x_train_open), np.array(y_train_open)
x_train_high, y_train_high = np.array(x_train_high), np.array(y_train_high)
x_train_low, y_train_low = np.array(x_train_low), np.array(y_train_low)


# Reshape the data
x_train_close = np.reshape(x_train_close, (x_train_close.shape[0], x_train_close.shape[1], 1))
x_train_close.shape
x_train_open = np.reshape(x_train_open, (x_train_open.shape[0], x_train_open.shape[1], 1))
x_train_open.shape
x_train_high = np.reshape(x_train_high, (x_train_high.shape[0], x_train_high.shape[1], 1))
x_train_high.shape
x_train_low = np.reshape(x_train_low, (x_train_low.shape[0], x_train_low.shape[1], 1))
x_train_low.shape



# Build the LSTM model
def buildModel(dataLength,labelLength):
  p_close = tf.keras.Input(shape=(1,1),name='close')
  p_open = tf.keras.Input(shape=(1,1),name='open')
  p_high = tf.keras.Input(shape=(1,1),name='high')
  p_low = tf.keras.Input(shape=(1,1),name='low')


  p_close_layers = LSTM(100,return_sequences=False)(p_close)
  p_open_layers = LSTM(100,return_sequences=False)(p_open)
  p_high_layers = LSTM(100,return_sequences=False)(p_high)
  p_low_layers = LSTM(100,return_sequences=False)(p_low)
  


  output = tf.keras.layers.concatenate(inputs=[p_close_layers,p_open_layers, p_high_layers, p_low_layers],axis=1)

  output = Dense(labelLength,activation='relu',name='weightedAverage_output_3')(output)
  model = Model(inputs=[p_close,p_open,p_high,p_low],outputs=[output])
  optimizer = Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999)
  model.compile(optimizer=optimizer,loss='mse',metrics=['accuracy'])
  return model

# Create the data sets x_test and y_test
x_test_close = []
y_test_close = dataset[training_data_len:, :]
y_test_close = y_test_close[:, [0]]
for i in range(60, len(scaled_test_data)):
    x_test_close.append(scaled_test_data[i-60:i, 0])


# Convert the data to a numpy array
x_test_close = np.array(x_test_close)


# reshape the data
x_test_close = np.reshape(x_test_close, (x_test_close.shape[0], x_test_close.shape[1], 1))


rnn = buildModel(training_data_len,1)
rnn.fit([x_train_close,x_train_open,x_train_high, x_train_low],
        [x_test_close],
        validation_data = ([y_train_close,y_train_open,y_train_high, y_train_low],[y_test_close]),
        epochs = 1,
        batch_size = 10,
        )



































