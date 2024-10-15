import time
import random

# Lineair zoeken met index
def linear_search(array, target):
    for index, element in enumerate(array):
        if element == target:
            return index  # Return de index waar het getal is gevonden
    return -1  # -1 betekent dat het getal niet is gevonden

# Binair zoeken met index
def binary_search(array, target, low, high):
    if low > high:
        return -1  # -1 betekent dat het getal niet is gevonden
    mid = (low + high) // 2
    if array[mid] == target:
        return mid  # Return de index waar het getal is gevonden
    elif array[mid] > target:
        return binary_search(array, target, low, mid - 1)
    else:
        return binary_search(array, target, mid + 1, high)

# Input van array en target
def get_input():
    array = input("Voer de array in (gescheiden door komma's): ").split(',')
    array = [int(x) for x in array]
    target = int(input("Voer het getal in dat je wilt zoeken: "))
    return array, target

# Runtime meten met extra argumenten voor binair zoeken
def time_function(func, array, target, *args):
    start_time = time.time()
    index = func(array, target, *args)  # Extra argumenten doorgeven aan de zoekfunctie
    end_time = time.time()
    return index, end_time - start_time

# Hoofdprogramma
if __name__ == "__main__":
    # Genereer array of neem invoer van gebruiker
    array, target = get_input()

    # Sorteer array voor binair zoeken
    array.sort()

    print(f"Gesorteerde array: {array}")

    # Lineair zoeken
    index, runtime = time_function(linear_search, array, target)
    if index != -1:
        print(f"Lineair zoeken: gevonden op index {index} in {runtime:.6f} seconden.")
    else:
        print(f"Lineair zoeken: niet gevonden in {runtime:.6f} seconden.")

    # Binair zoeken
    index, runtime = time_function(binary_search, array, target, 0, len(array) - 1)
    if index != -1:
        print(f"Binair zoeken: gevonden op index {index} in {runtime:.6f} seconden.")
    else:
        print(f"Binair zoeken: niet gevonden in {runtime:.6f} seconden.")
