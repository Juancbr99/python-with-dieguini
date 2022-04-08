try:
    #Este código puede fallar
    age = input("Enter your age (numbers only): ")
    print("Your age is", int(age))
except:
    #Si mi código falla, se ejecuta este código:
    print("You are an asshole!")