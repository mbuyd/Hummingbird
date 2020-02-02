# Imports
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

def Learn():
    categories = 3
    temp = 'generated.csv'

    dataset = loadtxt(temp, delimiter=',')
    inputs = dataset[:,0:categories]
    outputs = dataset[:,categories]

    model = Sequential()
    model.add(Dense(12, input_dim = categories, activation = 'relu'))
    model.add(Dense(8, activation = 'relu'))
    model.add(Dense(1, activation = 'sigmoid'))

    model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
    model.fit(inputs, outputs, epochs = 150, batch_size = 10)

    # Evaluation
    _, accuracy = model.evaluate(inputs, outputs)
    print('Accuracy: %2.f' % (accuracy * 100))

def main():
    print("Learn has been activited! It should do nothing.")

main()