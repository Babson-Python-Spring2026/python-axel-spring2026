def get_numbers():
    raw = input("Enter numbers: ")
    pieces = raw.split()
    numbers = []
    for piece in pieces:
        numbers.append(int(piece))
    return numbers

#because int converts a string into an integer we must add int before input
def get_target():
    return int(input("Enter target: "))


def build_signs(i, n):
    signs = []
    for position in range(n):
        bit = i % 2
        if bit == 0:
            signs.append(-1)
        else:
            signs.append(1)
        i = i // 2
    return signs


def compute_sum(numbers, signs):
    products = []
    for k in range(len(numbers)):
        products.append(numbers[k] * signs[k])
    return sum(products)


def build_expression(numbers, signs, target):
    result = ""
    for k in range(len(numbers)):
        if k == 0:
            if signs[k] == 1:
                result = result + str(numbers[k])
            else:
                result = result + "-" + str(numbers[k])
        else:
            if signs[k] == 1:
                result = result + " + " + str(numbers[k])
            else:
                result = result + " - " + str(numbers[k])
    result = result + " = " + str(target)
    return result

#this code will either return the correct answer or will print "no solution found"

#Total combinations is 2 ** n because each answer gets 1/2 choices either + or - and the numbers are n 
def find_solution(numbers, target):
    n = len(numbers)
    total_combinations = 2 ** n
    for i in range(total_combinations):
        signs = build_signs(i, n)
        if compute_sum(numbers, signs) == target:
            return build_expression(numbers, signs, target)
    return "No solution possible"


def main():
    numbers = get_numbers()
    target = get_target()
    answer = find_solution(numbers, target)
    print(answer)


main()