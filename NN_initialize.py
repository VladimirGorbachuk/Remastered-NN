# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 21:57:45 2019

@author: Vovan-i-Veneraa
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 23:04:14 2019

@author: Vovan-i-Venera
"""

import random
from collections import namedtuple
Neuron = namedtuple ("Neuron", ["weights"])

class Neural_Network ():
    """
    класс для рандомизированной сборки нейросети (для первых нейросетей он необходим)
    в этом классе хранится распределение нейронов по слоям, весов по нейронам
    в подфункциях заложен дополнительный функционал - чтобы собирать нейросеть
    по весам из генератора. Это нужно чтобы  собрать нейросеть из весов записанных в строку
    """
    
    def __init__ (self, n_neurons = None, input_sample = None, n_out = None, with_bias =True, activation_func = "relu"):
            """
            на вход примем число слоев в нейросети
            и количества нейронов в каждом слое
            в виде списка 0 - первый слой, 1 - второй итд
            """
           
            self.neurons = n_neurons + [n_out]
            self.layers = len (self.neurons)
            self.input_length = len (input_sample)
            self.weights = None
            self.with_bias = with_bias
            self._activation_func_name = "relu"
    def __repr__(self):
       if self.weights:
           repres =""
           for number_of_layer,layer in enumerate (self.weights):
               repres += "layer number " + str (number_of_layer) + "\n"
               repres += str (layer)
               repres += "\n"
           return repres
       else:
           return ("Empty_NN")

    def __make_one_neuron (self,layer,weight_generator = None):
        """
        чтобы сделать нейрон нужно знать сколько
        значений в него придет чтобы раскидать
        количество коэффициентов (равно количеству
        входных данных + 1 коэффициент для биаса)
       
        """
        if layer >0:
            n_inputs = self.neurons [layer-1]+1
        else:
            n_inputs = self.input_length+1
        if not self.with_bias:
            n_inputs -= 1 #если без биасов то не будем делать лишних весов
        if not weight_generator:
            neuron = Neuron (weights = [random.uniform (-1,1) for signals_and_bias
                     in range (n_inputs)])
        else:
            neuron = Neuron (weights = [next (weight_generator) for signals_and_bias
                     in range (n_inputs)])

        return neuron
   
    def __make_one_layer (self,layer,weight_generator = None):
        """
        теперь будем использовать встроенную функцию
        для собирания отдельного нейрона для
        собирания отдельного слоя нейронной сети
        """
        neurons_in_layer = [self.__make_one_neuron(layer,weight_generator) for neuron in range(self.neurons [layer])]
        return neurons_in_layer
           
    def _build_random_or_defined_NN (self,weight_generator = None):
        """
        функция для послойной сборки теперь будет использовать
        встроенную функцию для сборки одного слоя
        """
        all_neurons_in_NN = [self.__make_one_layer (layer, weight_generator = weight_generator ) for layer in range (self.layers)]
        self.weights = all_neurons_in_NN
        return
    
    def build_random_NN (self):
        self._build_random_or_defined_NN (weight_generator = False)
        return
    

class Neural_Read_n_Write(Neural_Network):
        
    def __init__(self, source=None):
        if source is not None:
            self.__dict__.update(source.__dict__)

    def write(self):
        one_liner_NN = []
        for layer in self.weights:
            for neuron in layer:
                for weights in neuron:
                    for weight in weights:
                        one_liner_NN.append(weight)
        return one_liner_NN
    
    def read(self, one_liner):
        weight_generator = (weight for weight in one_liner)
        """
        тут ещё думаю... надо как можно гибче сделать 
        хочу чтобы при скрещивании и число слоёв и количество нейронов в слоях
        менялось (было бы прикольно, возможжно... но это надо проверить)
        """
        self._build_random_or_defined_NN  (weight_generator=weight_generator)
        return

