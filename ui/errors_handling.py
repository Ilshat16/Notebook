def numeric_input_exceptions(text):
    error = True
    while error:
        print(text, end=": ")
        try:
            number = int(input())
            error = False
        except ValueError:
            print("Ошибка ввода!")
    return number
