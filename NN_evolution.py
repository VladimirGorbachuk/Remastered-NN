# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:48:37 2019

@author: Vovan-i-Venera
"""
from NN_calculations import NN_performace_estimation
import random
from functools import partial

class Genetic_cross_breeding(NN_performace_estimation):
    """
    def __init___(self,source_NN,
                  
                                strings=None,evaluations =None,
	                            n_children = 50, n_mutants = 5,
	                            n_elite =5, n_cycles = 50, mutagenity = 0.1
	                            training_x = None, training_y = None, estimation_func = None):
        self.__children = strings
        self.__evaluation = evaluation
        self.__n_children = n_children
        self.__n_mutants = n_mutants
        self.__n_cycles = n_cycles
        self.__n_elite = elite
        self.__elite = self.__gather_elite()
        self.__mutagenity = mutagenity
        self.__estimate = estimation_func
    такой был инит... но он вообще говоря тут не нужен. Нам нужны только общие "настройки"
    типа числа слоёв , количества нейронов в каждом слое
    а эти показатели спокойно можно принять во встроенном методе generate
    """
    def __gather_elite(self):
        evaluated_children = zip (self.__evaluation, self.__children)
        self.elite = sorted (evaluated_children)[-self.__n_elite:]
    def __breed (self):
        self.__new_children = []
        for breeds in range(self.__n_children//2):
            [parent_a,parent_b] = random.choices(self.__children, weights = self.__evaluation, k = 2)
            child_1 = [random.choice (weights) for weights in zip (parent_a,parent_b)]
            child_2 = [random.choice (weights) for weights in zip (parent_a,parent_b)]
            self.__new_children.append (child_1)
            self.__new_children.append (child_2)
        return
    def __mutate (self):
        for mutations in range(self.__n_mutants):
            mutant = random.choice (self.__new_children)
            mutated = []
            for weight in mutant:
                [weight_2] = random.choices ([weight, random.random ()], weights = [1,self.__mutagenity])
                mutated.append (weight_2)
            self.__new_children.append (mutated)
    def __tournament_selection (self):
        for new_child in self.__new_children:
            contestant_number = random.choice(range(len(self.__children)))
            contestant = self.__children[contestant_number]
            new_child_estimation = 1/self.__estimate (NN=new_child) #АЛЯРМ
            if new_child_estimation > self.__estimate(NN=contestant):
                self.__children [contestant_number] = new_child
                self.__evaluation [contestant_number] = new_child_estimation
    def generate (self,strings=None,evaluations =None, n_children = 100, n_mutants = 5,
	              n_elite =5, n_cycles = 1000, mutagenity = 0.1, n_vectors = 10,
	              training_x = None, training_y = None, output = True, loss_func = "MAE"):
        
        """
        оч сомневаюсь что следующий блок с присвоением self. вообще нужен
        а ещё сомневаюсь в необходимости self.__gather_elite()
        """
        self.__children = strings
        self.__evaluation = evaluations
        self.__n_children = n_children
        self.__n_mutants = n_mutants
        self.__n_cycles = n_cycles
        self.__n_elite = n_elite
        self.__elite = self.__gather_elite()
        self.__mutagenity = mutagenity
        self.__children = strings
        if loss_func == "MAE":
            self.__estimate = partial(self.mean_abs_error, vectors = training_x, labels = training_y,
                                              n_vectors = n_vectors, n_labels = len(set(training_y)))
        elif loss_func == "hybrid":
            self.__estimate = partial(self.hybrid_MAE_GR, vectors = training_x, labels = training_y,
                                              n_vectors = n_vectors, n_labels = len(set(training_y)))

        for _evolution_cycle in range(self.__n_cycles):
            self.__gather_elite()
            self.__breed()
            self.__mutate()
            self.__tournament_selection()
            if output == True:
                print("current average performance:", sum(self.__evaluation) / len(self.__evaluation))
        return self.__children