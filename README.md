# AI-Network

# Создание сети

Сеть состоит из одного и более слоев. Каждый слой состоит из одного или более нейронов

## Нейроны

Конструктор нейрона 
``` Neuron(inputs, weights, activation, normalize) ```

- inputs - список входных значений;
- weights - веса;
- activation - функция активации. Рекомедуется Activations.sigmoid;
- normalize - нормализация значений сети. Рекомендуется False

Пример:
```Python
#Создание переменной neuron, в которую записывается ссылка на созданный нейрон
neuron = Neuron(input_values, weights, Activations.sigmoid, False)
```

## Слои

Конструктор слоя
``` Layer(neurons)```

- neurons - список нейронов для создания слоя;

Пример:
```Python
#Создание списка neurons для хранения и передачи нейронов в слой
neurons = []

#Создание переменной neuron, в которую записывается ссылка на созданный нейрон
neuron = Neuron(input_values, weightsM, Activations.sigmoid, False)
#Добавление neuron в список
neurons.append(neuron)

#Создание нового neuron
neuron = Neuron(input_values, weightsR, Activations.sigmoid, False)
#Добавление neuron в список
neurons.append(neuron)

#Создание слоя
layer = Layer(neurons)

```

## Сеть

Конструктор сети
``` Network(layers) ```

- inputs - список слоев для создания сети;

Пример:
```Python
#Создание списка layers для хранения и передачи слоев в сеть
layers = []

#Создание слоя layer
layer = Layer(neurons)

#Добавление слоя layer в список слоев layers
layers.append(layer)

#Создание дополнительного слоя layer с одним нейроном с тремя входами
layer = Layer([Neuron([0, 0, 0], [-0.43, 0.1, 0.22], Activations.sigmoid, False)])

#Добавление дополнительного слоя layer в список слоев layers
layers.append(layer)

#Создание нейронной сети
network = Network(layers)
```

# Запуск сети

Сеть, как и любой ее элемент (слой, нейрон) можно запустить вызовом метода ```calculate()```\
Входные значения определяются полем ```inputs```\
При выполнении метода рассчитываются выходные значения. Получить результат можно через поле ```outputs```

Пример для сети:
```Python
#Создание сети
network = Network(layers)
#Задание входных значений
network.inputs = input_values
#Запуск сети
network.calculate()
#Вывод результатов работы
print(network.outputs)
```
Пример для нейрона:
```Python
#Создание нейрона
neuron = Neuron(input_values, weightsM, Activations.sigmoid, False)
#Запуск нейрона
neuron.calculate()
#Вывод результатов работы
print(neuron.outputs)
```
# Обучение сети
 
Обучение сети происходит методом обратного распространения ошибки.\
Для запуска процесса обучения используется метод ```learn()```

Сигнатура метода
```learn(target_values, learning_rate, epochs)```

- target_values - целевые выходные значения, используемые для корректировки выходных значений сети;
- learning_rate - скорость обучения. Подбирается экспериментально. Рекомендуется от 0.01 до 0.8
- epochs - количество эпох (циклов обучения) сети. 

Пример:
```Python
#Обучение сети network. Целевое значение - 2, скорость обучения - 0.05, количество эпох - 1000
network.learn([2], 0.05, 1000)
```