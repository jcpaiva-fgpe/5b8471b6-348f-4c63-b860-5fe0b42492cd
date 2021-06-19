while True:
    try:
        print(sum(list(map(int, input()))))
    except ValueError:
        print('Miałes wisać liczbę całkowitą!')
        break
