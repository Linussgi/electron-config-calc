orbitals = ( 
    (2, "1s"),
    (2, "2s"),
    (6, "2p"),
    (2, "3s"),
    (6, "3p"),
    (2, "4s"),
    (10, "3d")
)

print("Calculator supports up to 30 electrons")

while True:
    try:
        electron_num = int(input("\nEnter number of electrons: "))
        if electron_num <= 0 or electron_num > 30:
            print("Invalid input")
            continue
    except ValueError:
        print("Invalid input")
        continue

    print(f"Electronic configuration with {electron_num} electron(s):")

    if electron_num == 24 or electron_num == 29:
        for index in range(0, 4):
            print(orbitals[index][1] + str(orbitals[index][0]))
        print("3d" + str(electron_num - 19))
        print("4s1")
        continue
    else:
        for orbital in orbitals:
            if electron_num > orbital[0]:
                print(orbital[1] + str(orbital[0]))
                electron_num -= orbital[0]
            else:
                print(orbital[1] + str(electron_num))
                break
        continue
