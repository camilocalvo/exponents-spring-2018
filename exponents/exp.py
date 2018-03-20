## Get our base and exponent. ##
def get_input():
    temp_base = input("What number are you raising? (q to quit) ")
    if temp_base == "q":
        quit()
    try:
        base = int(temp_base)
    except:
        print("Invalid base")
        return False
    powr = input("2nd, 3rd, or 4th power? ")
    if powr != "2" and  powr != "3" and powr != "4":
        print("Invalid exponent")
        return False
    return (base,powr)

tup = False
## Run the program loop. ##
while True:
    while tup == False:
        tup = get_input()
        if tup != False:
            base = tup[0]
            powr = tup[1]

    if powr == "2":
        print(str(base * base))
    elif powr == "3":
        print(str(base * base * base))
    elif powr == "4":
        print(str(base * base * base * base))
    tup = False
