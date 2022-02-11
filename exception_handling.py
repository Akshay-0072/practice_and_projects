try:
    i = int(input("enter a number "))
    w = i*4
except Exception as e:
    print("please enter a valid number!", e)
else:
    print(w)
    exit()
finally:
    print("thams")

