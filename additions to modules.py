deviation_weight = sum ([abs (w1-w2) for w1, w2 in zip (nn_first,nn_candidate)])
#нужно разделить эти функции!!!
#отдельно отбор и отдельно скрещивание
def __breed_cross_sect (self):
        self.__new_children = []
        for breeds in range(self.__n_children//2):
            [parent_a,parent_b] = random.choices(self.__children, weights = self.__evaluation, k = 2)
            deliminator = random.choice (range (len (child_1)))
            child_1 = parent_a [:deliminator]+parent_b [deliminator:]
            child_2 = parent_b [:deliminator]+parent_a [deliminator:]

            self.__new_children.append (child_1)
            self.__new_children.append (child_2)
        return

def __breed_deviant (self):
        self.__new_children = []
        for breeds in range(self.__n_children//2):
            parent_a = random.choices(self.__children, weights = self.__evaluation, k = 1)
            deviant_weights = []
            for mb_parent in self.__children:
                deviant_weight = sum ([(w1-w2)**2 for w1, w2 in zip (parent_a,mb_parent)])
                deviant_weights.append(deviant_weight)
            parent_b = random.choices(self.__children, weights = deviant_weights, k = 1)
            child_1 = [random.choice (weights) for weights in zip (parent_a,parent_b)]
            child_2 = [random.choice (weights) for weights in zip (parent_a,parent_b)]
            self.__new_children.append (child_1)
            self.__new_children.append (child_2)
        return

def __breed_proportional_addition (self):
        self.__new_children = []
        for breeds in range(self.__n_children//2):
            [parent_a,parent_b] = random.choices(self.__children, weights = self.__evaluation, k = 2)
            multiplier = random.random ()
            child_1 = parent_a [:deliminator]+parent_b [deliminator:]
            child_2 = parent_b [:deliminator]+parent_a [deliminator:]

            self.__new_children.append (child_1)
            self.__new_children.append (child_2)
        return
