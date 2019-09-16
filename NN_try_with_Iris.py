# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:05:56 2019

@author: Vovan-i-Venera
"""
from NN_initialize import Neural_Network, Neural_Read_n_Write
from NN_calculations import Neural_answer, NN_performace_estimation
from NN_evolution import Genetic_cross_breeding

"""
Загрузку датасета
его разделение на тренировочный и тестовый набор
его нормализацию - всё это пока возьмём стандартное из склёрн
"""
import random
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler #OneHotEncoder пока не юзаем
    

iris = load_iris()
x = iris['data']
y = iris['target']
x_scaled = StandardScaler().fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(
    x_scaled, y, test_size=0.5, random_state=2)

print(y)
NN = Neural_Network(n_neurons = [4,6], input_sample = x_train[0],n_out = len(set(y_train)), activation_func = "relu")
NN.build_random_NN ()
print(NN)

procreation = Genetic_cross_breeding(NN)

random_NNs_initial = []
for _number_of_initial_NNs in range(50):
    NN.build_random_NN()
    NN_for_writing = Neural_Read_n_Write(NN)
    random_NNs_initial.append(NN_for_writing.write())
#print(random_NNs_initial)
estimate_NN = NN_performace_estimation(NN)
initial_NNs_evaluated = []
#print("это до того или после того?")
for random_initial_NN in random_NNs_initial:
    #print("как так?",random_initial_NN)
    initial_NNs_evaluated.append(1/estimate_NN.hybrid_MAE_GR(NN=random_initial_NN,
                                                              vectors = x_train, 
                                                              labels = y_train, 
                                                              n_vectors = 40, 
                                                              n_labels = len(set(y_train))))

    

new_NNs = procreation.generate(strings = random_NNs_initial, evaluations =initial_NNs_evaluated,
                     training_x = x_train, n_cycles = 15000, training_y = y_train, n_vectors = 80,
                     n_children = 50, loss_func = "hybrid")
evaluated_by_test_set_new_NNs = []
for chosen_NN in new_NNs:
    evaluated_by_test_set_new_NNs.append(estimate_NN.guess_rate(NN=chosen_NN,
                                                                vectors = x_test,
                                                                labels = y_test,
                                                                n_vectors = len(x_test),
                                                                n_labels = len(set(y_test))))

print(evaluated_by_test_set_new_NNs)