while True:
    try:
        print(sum(list(map(int, input()))))
    except ValueError:
        print('Miałes wprowadzić cyfrę!')
        break
