while True:
    try:
        print(sum(list(map(int, input()))))
        break
    except ValueError:
        print('miałes wprowadzić liczbę!')
        break
