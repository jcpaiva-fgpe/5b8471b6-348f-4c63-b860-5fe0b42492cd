while True:
    try: 
        n = list(map(int, input('Wprowadź ciąg liczb całkowitych:​\n').split(',')))    
    except ValueError: 
        break

    print('liczby to:', *sorted(set(n), reverse=True))
    