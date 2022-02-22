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

# Get the stock quote
df = web.DataReader("AAPL", data_source='yahoo', start='2012-01-01', end='2022-01-12')
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
data = df.filter(['Close'])
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
x_train = []
y_train = []

for i in range(60, len(scaled_train_data)):
    x_train.append(scaled_train_data[i-60:i, 0])
    y_train.append(scaled_train_data[i, 0])
    if i <= 60:
        print(x_train)
        print(y_train)
        print()

# Convert the x_train and y_train to numpy arrays
x_train, y_train = np.array(x_train), np.array(y_train)


# Reshape the data
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
x_train.shape



# Build the LSTM model
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))


# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')


# Train the model
model.fit(x_train, y_train, batch_size=1, epochs=1)

# Create the data sets x_test and y_test
x_test = []
y_test = dataset[training_data_len:, :]
for i in range(60, len(scaled_test_data)):
    x_test.append(scaled_test_data[i-60:i, 0])


# Convert the data to a numpy array
x_test = np.array(x_test)


# reshape the data
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))


# Get models predicted price values
predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)


# Get the root mean squared error (RMSE)
rmse = np.sqrt(np.mean(((predictions- y_test)**2)))
rmse


# Plot the data
train = data[:training_data_len]
valid = data[training_data_len:]
valid['Predictions'] = predictions
# Visualize the data
plt.figure(figsize=(16,8))
plt.title('Model')
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close price USD ($)', fontsize=18)
plt.plot(train['Close'])
plt.plot(valid[['Close', 'Predictions']])
plt.legend(['Train', 'Val', 'Predictions'], loc='lower right')
plt.show()



# Show the valid and predicted prices
valid



# Get the qoute
apple_quote = web.DataReader('AAPL', data_source='yahoo', start='2012-01-01', end='2022-01-12')
# Create a new dataframe
new_df = apple_quote.filter(['Close'])
# Get the last 60 day closing price values and convert the dataframe to an array
last_60_days = new_df[-60:].values
# Scale the data to be values between 0 and 1
last_60_days_scaled = scaler.transform(last_60_days)
# Create an empty list
X_test = []
# Append the past 60 days
X_test.append(last_60_days_scaled)
# Convert the X_test data set to a numpy array
X_test = np.array(X_test)
# Reshape the data
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
# Get the predicted scaled price
pred_price = model.predict(X_test)
# Undo the scaling
pred_price = scaler.inverse_transform(pred_price)
print(pred_price)


# Get actual price
apple_quote2 = web.DataReader('AAPL', data_source='yahoo', start='2022-01-12', end='2022-01-12')
print(apple_quote2['Close'])



# rozpietość danych została zmieniona w stosunku do tutriala
# dane pociągnięto od 2012-01-01 do 2022-01-12

# zmieniono sposób skalowania danych, w tutorialu cały data set został zeskalowany
# co może prowadzić do "data leakage". Z tego powodu najpier dane zostały podzielone na
# uczące i testowe a następnie zeskalowano tym samym skalerem.


# Kolejnym krokiem powinno być sprawdzenie jaka działa algorytm kiedy do danych wsadowych
# zostaną dodane dane open price, low price, high price

# Następny krok to dodanie wolumenu













