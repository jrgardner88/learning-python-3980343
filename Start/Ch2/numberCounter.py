def count_numbers(which, numbers):
    counter = 0
    if (which == "even"):
        for d in numbers:
            if (d % 2 == 0):
                counter = counter + 1
            else:
                continue
        return counter
    elif (which == "odd"):
        for d in numbers:
            if (d % 2 != 0):
                counter = counter + 1
            else:
                continue
        return counter
    return -1

numbers = [7, 17, 2, 13, 19, 20, 0, 5, 11, 1280, 105]
print(count_numbers("even", numbers))