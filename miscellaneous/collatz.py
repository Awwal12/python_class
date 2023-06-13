try:
    vals = int(input("input num: "))

    def collatz(number):
        if number % 2 == 0:
            return number // 2
        else:
            return 3 * number + 1
    while (vals != 1):
        vals = collatz(vals)
        print(vals)

except ValueError:
    print("you've messesd up G")


print('Experimenting with Collatz funtion pls input a number below')
collatz(vals)
