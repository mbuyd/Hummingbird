# Imports
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

categories = 3
temp = 'generated.csv'

dataset = loadtxt(temp, delimiter=',')
inputs = dataset[:,0:categories]
outputs = dataset[:,categories]

model = Sequential()
model.add(Dense(8, input_dim = categories, activation = 'relu'))
model.add(Dense(4, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid'))

model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
model.fit(inputs, outputs, epochs = 1500, batch_size = 250)

# Evaluation
_, accuracy = model.evaluate(inputs, outputs)
print('Accuracy: %2.f' % (accuracy * 100))
