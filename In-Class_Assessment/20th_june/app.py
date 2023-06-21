# Write a class that takes a dictionary and has 3 functions one that grades them 2 that gets the summation

class Grade:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary

    def counter(self):
        return len(self.dictionary)

    def grades(self):

        new_dict = {}

        for i in self.dictionary:
            if self.dictionary[i] >= 70:
                new_dict[i] = 'A'
            elif self.dictionary[i] >= 60:
                new_dict[i] = 'B'
            elif self.dictionary[i] >= 50:
                new_dict[i] = 'C'
            elif self.dictionary[i] >= 40:
                new_dict[i] = 'D'
            else:
                new_dict[i] = 'E'

        return new_dict

    def average(self):
        for i in self.dictionary.values:
            sumn += i
            sumn += self.dictionary[i]
            # average = self.dictionary[i] / len(self.dictionary)
        return sumn


xoxo = Grade({"john": 64, "mary": 98})
print(xoxo.average())
