class Atm(object):
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number

    def cash_with_drawl(self):
        print("With draw the cash here...!")

    def balance_enquiry(self):
        print("Enquire here for your balance amount")

reema = Atm("7863457853698705", "2268")
print(reema.card_number)

keyuri = Atm("2765386496510482","9986")
print(keyuri.pin_number)
print(keyuri.card_number)
