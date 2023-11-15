prompt = "How old are you?"
prompt += "\nEnter 'age' when you are finished. "

while True:
    age = input(prompt)
    if age == 'age':
        break
    age = int(age)

    if age < 3:
        print("  You get in free")
    elif age < 12:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")
        