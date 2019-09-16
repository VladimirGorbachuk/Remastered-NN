
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
from sklearn.datasets import load_iris#сейчас лишнее
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler #OneHotEncoder пока не юзаем
    

iris = load_iris()

def one_D_dataset_preproc (dataset):
    x = dataset['data']
    y = dataset  ['target']
    x_scaled = StandardScaler().fit_transform(x)
    x_train, x_test, y_train, y_test = train_test_split(
        x_scaled, y, test_size=0.5, random_state=2)
    return x_train,x_test,y_train, y_test

def NN_config (n_neurons = [], x_train = None, y_train = None, activation_func = "relu"):
    NN = Neural_Network(n_neurons = n_neurons, input_sample = x_train[0],n_out = len(set(y_train)), activation_func = activation_func)
    return NN

def build_initial_random_NNs (NN, quantity = 50):
    for _NN_random in range (quantity):
        NN.build_random_NN ()
        
print(NN)
def first_gen_eval(NN):
    procreation = Genetic_cross_breeding(NN)
    random_NNs_initial = []
    initial_NNs_evaluated = []
    for _number_of_initial_NNs in range(50):
        NN.build_random_NN()
        NN_for_writing = Neural_Read_n_Write(NN)
        random_NNs_initial.append(NN_for_writing.write())
        estimate_NN = NN_performace_estimation(NN)
        initial_NNs_evaluated.append(1/estimate_NN.hybrid_MAE_GR(NN=random_initial_NN,
                                                              vectors = x_train, 
                                                              labels = y_train, 
                                                              n_vectors = 40)
    return

def evolve(strings = random_NNs_initial, evaluations =initial_NNs_evaluated,
                     training_x = x_train, n_cycles = 15000, training_y = y_train, n_vectors = 80,
                     n_children = 50, loss_func = "hybrid"):                                                                                                                                                                  n_labels = len(set(y_train))))
   new_NNs = procreation.generate(strings = random_NNs_initial, evaluations =initial_NNs_evaluated,
                     training_x = x_train, n_cycles = 15000, training_y = y_train, n_vectors = 80,
                     n_children = 50, loss_func = "hybrid")
   return new_NNs

def final_eval():
    evaluated_by_test_set_new_NNs = []
    for chosen_NN in new_NNs:
        evaluated_by_test_set_new_NNs.append(estimate_NN.guess_rate(NN=chosen_NN,
                                                                vectors = x_test,
                                                                labels = y_test,
                                                                n_vectors = len(x_test),
                                                                n_labels = len(set(y_test))))
print(evaluated_by_test_set_new_NNs)
