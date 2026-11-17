
print("hello WOrld")
intpi = input("input num")
if intpi.isdigit():
    intpi = int(intpi)
    if intpi<100 :
        num=int(intpi)
        print(f"romal normal is {num}")
    else: 
        print("put a number less than 100")
else:
    print("put num not englis")