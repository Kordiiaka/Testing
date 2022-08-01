def solution(number):
    suma = 0
    for x in range(number):
        if x%3 == 0 or x%5 == 0:
            suma += x
    return suma

print(solution(-1))


