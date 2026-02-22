from banken_3 import Bankkonto

konto = Bankkonto()

while True:
    print("\n1. Sätta in pengar")
    print("2. Ta ut pengar")
    print("3. Beräkna ränta")
    print("4. Visa saldo")
    print("5. Betala räkning")
    print("6. Avsluta")

    choice = input("Välj: ")

    if choice == "1":
        amount = float(input("Belopp: "))
        if konto.deposit(amount):
            print("Insättning genomförd.")
        else:
            print("Ogiltigt belopp.")

    elif choice == "2":
        amount = float(input("Belopp: "))

        if konto.withdraw(amount):
            print("Uttag genomfört.")
            print("Nytt saldo:", konto.balance())
        else:
            print("Otillräckligt saldo eller ogiltigt belopp.")

    elif choice == "3":
        konto.apply_interest()
        print("Ränta på 10% har lagts till.")
        print("Nytt saldo:", konto.balance())

    elif choice == "4":
        print("Saldo:", konto.balance())

    elif choice == "5":
        amount = float(input("Belopp: "))

        if konto.pay_bill(amount):
            print("Räkningen är betald.")
            print("Nytt saldo:", konto.balance())
        else:
            print("Det finns inte tillräckligt med pengar.")

    elif choice == "6":
        break
