from veckouppgift6.banken_3 import Bankkonto

# Hjälpfunktion: skapar ett konto med 100 kr
def create_account_with_balance():
    account = Bankkonto()
    account.deposit(100)
    return account

# AK1 Skapa ett konto där saldo är 0kr
def test_start_saldo():
    account = Bankkonto()
    assert account.balance() == 0

# AK2 Insättning av belopp
def test_deposit():
    account = Bankkonto()
    assert account.deposit(100) == 100

# AK3 Insättning med minusbelopp
def test_deposit_negative():
    account = Bankkonto()
    assert account.deposit(-100) == 0

# AK4 Uttag från konto där pengar finns
def test_withdraw():
    account = create_account_with_balance()
    assert account.withdraw(20) == True

# AK5 Uttag från konto där saldo inte finns
def test_withdraw_too_much():
    account = create_account_with_balance()
    assert account.withdraw(200) == False

# AK6 Lägger på ränta 10%
def test_interest():
    account = create_account_with_balance()
    assert account.apply_interest() == 110


# AK7 Betalar en räkning där pengar finns på konto
def test_pay_bill_success():
    account = create_account_with_balance()
    assert account.pay_bill(40) == True


# AK8 Betalar en räkning där pengar inte finns på konto
# def test_pay_bill_fail():
# #    account = create_account_with_balance()
#     account = Bankkonto()
#     assert account.pay_bill(200) == 0

def test_pay_bill_fail():
    account = create_account_with_balance()
    assert account.pay_bill(200) == False


def run_all_tests():
    test_start_saldo()
    test_deposit()
    test_deposit_negative()
    test_withdraw()
    test_withdraw_too_much()
    test_interest()
    test_pay_bill_success()
    test_pay_bill_fail()

    print("Alla tester gick igenom!")

if __name__ == "__main__":
    run_all_tests()