# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 13:07:14 2019

@author: Vovan-i-Venera
"""
from NN_initialize import Neural_Read_n_Write
import random

class Neural_answer(Neural_Read_n_Write):
    """
    берём нейросеть, при помощи встроенной функции calc_output расчитываем для неё результат
    """
    def __init__(self, source_NN):
        """
        получается что этот класс будет работать следующим образом - сначала надо
        применить класс к нейросети - так мы соберём все значения из нейросети.
        для базового функционала Пайтон это особой погоды не делает.
        Но для следующих версий моей нейросети, которые будут использовать
        numpy и tensorflow уже на этой стадии мы 
        сможем сделать все необходимые преобразования (до того как начнём скармливать вектора,
        для которых нужно получить ответ нейронной сети)
        Послсе того как мы сделаем
        Neural_answer(NN) где NN-нейросеть для которой будут 
        проводиться вычисления, и когда все преобразования будут выполнены (сейчас - никаких преобразований)
        отдельным встроенным методом calc_output - мы сможем получить значения.
        """
        self.__dict__.update(source_NN.__dict__)
        if self._activation_func_name == "relu":
            self.__activation_function = self.__relu
        
            
    
    def __matrix_mult_relu (self,input,layer_number = None):
        if self.with_bias and layer_number != self.layers:
            input = [1]+input
        output = []
        for neuron in self.weights[layer_number]:
            product = 0
            for number_of_scalar,scalar in enumerate (input):
                product += neuron.weights [number_of_scalar]*scalar
            output.append (product)
        return self.__activation_function(output)
    
    def __relu (self, output):
        output = [x if x>0 else 0 for x in output ]
        return output

    def calc_output (self,input):
        """
        рассчитываем числа, которые выдаёт нейросеть для данного input (одномерного вектора)
        если в виде одной строки нейросеть, то используем наследованную функцию self.read()
        """

        for layer_number in range (self.layers):
            input = self.__matrix_mult_relu (input,layer_number = layer_number)       
        return input
    
    def nn_answer (self, input):
        """
        используем встроенную функцию calc_output, чтобы выяснить какой ответ
        даёт нейросеть - индекс максимального значения - соответствует ответу нейросети
        если в виде одной строки нейросеть, то используем наследованную функцию self.read()
        """

        output = self.calc_output(input)
        answer = output.index(max(output))
        return answer
    
    
class NN_performace_estimation(Neural_answer):
    """
    как и наследуемый класс Neural_answer, этот класс принимает нейросеть,
    поэтому я не прописываю __init__ (он ровно такой же)
    вся разница между этими классами в том, что этот класс будет использовать
    методы calc_output и nn_answer родительского класса чтобы оценить
    насколько хорошо работает очередная нейросеть
    выдаёт MAE и долю верно отгаданных ответов.
    Среднее отклонение по модулю будем использовать
    """
    def mean_abs_error (self,  NN=None, one_line_NN = True, vectors = None, labels = None, n_vectors = 1, n_labels = None):
        """
        разные бывают наборы и под-наборы даных, поэтому 
        """
        if one_line_NN == True:
            self.read(NN)
        if not n_labels:
            self.n_labels = len(set(labels))
        else:
            self.n_labels = n_labels
        vectors= list(vectors)
        
        self.numbers_of_vectors_chosen = random.choices(range(len(vectors)), k = n_vectors)
        abs_error = 0
        for number in self.numbers_of_vectors_chosen:
            correct_one_hot_encoded_answer = [0 if n_answer != labels[number] else 1 for n_answer in range(self.n_labels) ]
            nn_answer = self.calc_output(vectors[number])
            abs_error += sum([abs(val2-val1) for val1, val2 in zip(nn_answer,correct_one_hot_encoded_answer)])/self.n_labels
        mean_abs_error = abs_error / n_vectors
        return mean_abs_error
    
    def mean_squared_error (self,  NN=None, one_line_NN = True, vectors = None, labels = None, n_vectors = 1, n_labels = None):
        """
        разные бывают наборы и под-наборы даных, поэтому 
        """
        if one_line_NN == True:
            self.read(NN)
        if not n_labels:
            self.n_labels = len(set(labels))
        else:
            self.n_labels = n_labels
        vectors= list(vectors)
        
        self.numbers_of_vectors_chosen = random.choices(range(len(vectors)), k = n_vectors)
        sq_error = 0
        for number in self.numbers_of_vectors_chosen:
            correct_one_hot_encoded_answer = [0 if n_answer != labels[number] else 1 for n_answer in range(self.n_labels) ]
            nn_answer = self.calc_output(vectors[number])
            sq_error += sum([(val2-val1)**2 for val1, val2 in zip(nn_answer,correct_one_hot_encoded_answer)])/self.n_labels
        mean_sq_error = sq_error / n_vectors
        return mean_sq_error
    
    def hybrid_MAE_GR (self,  NN=None, one_line_NN = True, vectors = None, labels = None, n_vectors = 1, n_labels = None):
        """
        разные бывают наборы и под-наборы даных, поэтому 
        """
        if one_line_NN == True:
            self.read(NN)
        if not n_labels:
            self.n_labels = len(set(labels))
        else:
            self.n_labels = n_labels
        vectors= list(vectors)
        
        self.numbers_of_vectors_chosen = random.choices(range(len(vectors)), k = n_vectors)
        abs_error = 0
        total_guesses = 0
        correct_guesses = 0
        for number in self.numbers_of_vectors_chosen:
            total_guesses += 1
            correct_one_hot_encoded_answer = [0 if n_answer != labels[number] else 1 for n_answer in range(self.n_labels) ]
            nn_answer = self.calc_output(vectors[number])
            abs_error += sum([abs(val2-val1) for val1, val2 in zip(nn_answer,correct_one_hot_encoded_answer)])/self.n_labels
            if nn_answer.index(max(nn_answer)) == labels[number]:
                correct_guesses += 1
        mean_abs_error = abs_error / n_vectors
        return mean_abs_error*total_guesses/(correct_guesses+1)   
    
    def guess_rate(self, NN=None, one_line_NN = True, vectors = None, labels = None, n_vectors = 10, n_labels = None):
        if one_line_NN == True:
            self.read(NN)
        if not n_labels:
            self.n_labels = len(set(labels))
        else:
            self.n_labels = n_labels
        self.numbers_of_vectors_chosen = random.sample(range(len(vectors)), k = n_vectors)
        #self.enumerated_vectors_chosen = random.sample(enumerate(vectors), k = n_vectors)
        correct_guesses = 0
        total_guesses = 0
        for number in self.numbers_of_vectors_chosen:
            if self.nn_answer(vectors[number]) == labels[number]:
                correct_guesses += 1
            total_guesses +=1
        return correct_guesses / total_guesses