prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' topping:"

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        break