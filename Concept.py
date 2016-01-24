import random

class Concept:
    seed = None

    subjects = ["bird", "baby", "cat", "dog"]
    descriptors = ["sad", "smoking", "cheerful", "happy"]
    settings = ["office", "dinner table", "cafe", "park"]

    def __init__(self, seed=None):
        self.seed = seed

    def conceptualize(self):
        if self.seed is None:
            return "A {} {} at the {}".format(random.sample(self.descriptors, 1)[0], random.sample(self.subjects, 1)[0], random.sample(self.settings, 1)[0])
        else:
            return "A {} {} at the {}".format(self.seed[0], self.seed[1], self.seed[2])
