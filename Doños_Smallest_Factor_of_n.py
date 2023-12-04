while True:

    n = int(input("Enter an integer >=2: "))

    if n < 2:
        print("Invalid input. Enter a number greater than 2.")
        break
    else:

        for i in range(2, n + 1):
            if n % i == 0:
                print("The smallest factor of", n, "other than 1 is:", i)
                break