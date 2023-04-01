numbers = []

numbers_size = 100_000
#So we don't count zero as one of the elements
numbers_size += 1

for i in range(numbers_size):
    numbers.append(i)

#print(numbers)

wanted_number = 89000

def divider():
    print("----------------------------------------")

def linear_search():
    divider()
    tries = 0
    print("Linear Search : ")

    for i in range(len(numbers)):
        tries += 1

        if numbers[i] == wanted_number :
            print(f"The wanted number {wanted_number}, was found")
            print(f'Tries required {tries}')
            break

    print()
    divider()

linear_search()