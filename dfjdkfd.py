class Iphone14:
    hardware = 'battery'

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calculate(self):
        print(self.num1 + self.num2)
        # print(num1 + num2)
    # def intro(self):
    #     print(
    #         f'Hello im iphone14 n i have a {self.color} and i have a {self.hardware} n cost {self.price}')


dapo = Iphone14(5, 2)
# dapo.intro()
dapo.calculate()


def intro():
    print('hello world')


intro()
