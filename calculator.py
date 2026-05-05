history = []

while True:
    user_input = input("Start Calculating: ")

    if user_input == "exit":
        break

    elif user_input == "history":
        print(history)

    else:
        history.append(user_input)

        new = user_input.split()
        num1 = int(new[0])
        operator = new[1]
        num2 = int(new[2])

        result = None

        if operator == "+":
            result = num1 + num2
            

        elif operator == "-":
            result = num1 - num2
            

        elif operator == "*":
            result = num1 * num2
            

        elif operator == "/":
            if num2 == 0:
                print("Cannot divide by Zero")
            else:
                result = num1 / num2
        if result is not None:
            print(f'{num1} {operator} {num2} = {result}')

