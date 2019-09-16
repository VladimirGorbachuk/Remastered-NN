
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
    

iris = load_iris() # это будет потом отдельным файлом



class Solve_dataset (NN_evolution):
    def __init__(self, dataset = None, n_neurons = [], activation_func = "relu", quantity_children = 50):
        self.__dataset = dataset
        self._n_neurons = n_neurons
        self._activation_func = "relu"
        self.__quantity_children = quantity_children
    def __NN_config (self,n_neurons = [], x_train = None, y_train = None, activation_func = "relu"):
        NN = self.Neural_Network(n_neurons = n_neurons, input_sample = self.__x_train[0],n_out = len(set(self.__y_train)), activation_func = activation_func)
        self.__NN_configuration = NN
        return
    def __one_D_dataset_preproc (self):
        x = self.__dataset['data']
        y = self.__dataset  ['target']
        x_scaled = StandardScaler().fit_transform(x)
        x_train, x_test, y_train, y_test = train_test_split(
        x_scaled, y, test_size=0.5, random_state=2)
        self.__x_train = x_train
        self.__y_train = y_train
        self.__x_test = x_test
        self.__y_test = y_test
        return
    def __build_initial_random_NNs (self):
        #for _NN_random in range (quantity):
        self.NN_configuration.build_random_NN ()#Ошибка?!
        self.__procreation = Genetic_cross_breeding(NN)
        self.__random_NNs_initial = []
        self.__initial_NNs_evaluated = []
        for number_of_initial_NNs in range(50):
            NN.build_random_NN()
            NN_for_writing = self.Neural_Read_n_Write(NN)
            self.__random_NNs_initial.append(NN_for_writing.write())
            estimate_NN = self.NN_performace_estimation(NN)
            self.__initial_NNs_evaluated.append(1/estimate_NN.hybrid_MAE_GR(NN=random_initial_NN,
                                                              vectors = x_train,
                                                              labels = y_train,
                                                              n_vectors = 40)
        return
    def evolve(self)#, strings = random_NNs_initial, evaluations =initial_NNs_evaluated,
                    #training_x = x_train, n_cycles = 15000, training_y = y_train, n_vectors = 80,
                    #n_children = 50, loss_func = "hybrid"):                                                                                                                                                                  n_labels = len(set(y_train))))
       new_NNs = self.procreation.generate(self) #strings = random_NNs_initial, evaluations =initial_NNs_evaluated,
                     #training_x = x_train, n_cycles = 15000, training_y = y_train, n_vectors = 80,
                     #n_children = 50, loss_func = "hybrid")
       self.__final_eval ()
       return
    def __final_eval(self):
        evaluated_by_test_set_new_NNs = []
        for chosen_NN in new_NNs:
            evaluated_by_test_set_new_NNs.append(estimate_NN.guess_rate(NN=chosen_NN,
                                                                vectors = x_test,
                                                                labels = y_test,
                                                                n_vectors = len(x_test))
                                                                                                             n_labels = len(set(y_test))))
        print(evaluated_by_test_set_new_NNs)
        return
