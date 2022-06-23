def main():
    num_user = int(input("Введите номер вашего числа: "))
    fib(n=num_user)




def fib(n):
    fib1 = 0
    fib2 = 1

    #sum = fib_one + fib_two

    fib_index = 3

    list_fib = [fib1, fib2]

    for char in range(250):

        fib1, fib2 = fib2, fib1 + fib2

        list_fib.append(fib2)

    print(f"Ваше число: {list_fib[n]}")

main()


