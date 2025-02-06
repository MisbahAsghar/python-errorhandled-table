def generate_table():
    try:
        user_input= int(input("Enter a number:"))
        for i in range(1,11):
              print(f"{user_input} * {i}  = {user_input * i}")
    except ValueError:
        print("Enter a valid Number")    

generate_table()    