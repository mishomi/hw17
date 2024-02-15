class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"პიროვნება: {self.name}, დეპოზიტი: {self.deposit}, სესხი: {self.loan}"

class House:
    def __init__(self, ID, price, owner, status="გასაყიდი"):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = status

    def sell_house(self, buyer, loan_amount=0):
        if buyer.deposit >= self.price - loan_amount:
            buyer.deposit -= self.price - loan_amount
            self.owner.deposit += self.price
            self.owner = buyer
            buyer.loan+=loan_amount
            if loan_amount:
                self.status = "გაყიდული სესხით"
            else:
                self.status = "გაყიდული"
            print(f"სახლი {self.ID} შეისყიდა {buyer.name}-მა {self.price} დარად, სესხად კი {loan_amount} აიღო.")
        else:
            print("მყიდველს არ აქვს საკმარისი თანხა სახლის საყიდლად.")

person1 = Person("Owner1", 100000, 0)
person2 = Person("Buyer1", 100000, 0)

house1 = House("ABC123", 50000, person1)

print(person1)
print(person2)

house1.sell_house(person2, loan_amount=20000)

print(person1)
print(person2)
