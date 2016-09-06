from guitar import Guitar

def main():

    guitars = []

    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    jason = Guitar("Made in JingZhou", 1988, 8650)

    print(gibson.get_age())
    print(jason.get_age())

    print(gibson.is_vintage())
    print(jason.is_vintage())

    guitars.append(gibson)
    guitars.append(jason)

    for i, guitar in enumerate(guitars):
        print("Guitar {}: {:>20} ({}), worth $ {:10,.2f} {}".format(i+1, guitar.name, guitar.year, guitar.cost, guitar.is_vintage()))

main()