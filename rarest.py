# a function that returns the number of times a number occurs
def nth_most_signature(list_of_integers, n):
    # the function takes in two aruments

    for x in set(list_of_integers):
        if list_of_integers.count(x) == n:
            # the count function counts the number of times an item occured

            return x


random_numbers = [5, 4, 5, 4, 5, 4, 4, 5, 3, 3, 3, 2, 2, 1, 5]
# calling the function
print(nth_most_signature(random_numbers, 3))

