class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def showDetails(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print(f"User Bank Balance: Rs.{self.balance}")


class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def depositAmount(self, amount):
        self.amount = amount
        self.balance += self.amount
        print(f"Account Balance has been Updated: Rs.{self.balance}")

    def withdrawAmount(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print(f"Insufficient Balance | Account Balance: Rs.{self.balance}")
        else:
            self.balance -= self.amount
            print("Withdrawal Successfully!")
            print(f"Account Balance has been Updated: Rs.{self.balance}")

    def viewBalance(self):
        print(f"User Bank Balance: Rs.{self.balance}")

    def bankReceipt(self):
        self.line = "-"*48
        with open("Receipt.txt", "w") as f:
            f.write(self.line + "\n" + "\t\tBanking System" + "\n" + self.line + "\n")
            f.write("User Name   | " + str(self.name) + "\n")
            f.write("User Age    | " + str(self.age) + "\n")
            f.write("User Gender | " + str(self.gender) + "\n" + self.line + "\n")
            f.write("User Bank Balance: Rs." + str(self.balance))
            f.write("\n" + self.line)


if __name__ == "__main__":
    line = "-"*50
    print(line, "\n", "\t\tBanking System")
    print(line)

    name = input("Enter User Name: ")
    age = input("Enter User Age: ")
    gender = input("Enter User Gender: ")

    bank = Bank(name, age, gender)

    print(line)
    print("Choose an Option:")
    print("1. Deposit Amount")
    print("2. Withdraw Amount")
    print("3. View User Balance")
    print("4. Show User Details")
    print("5. Quit")

    while True:
        try:
            print(line)
            num = int(input("Enter Option Number: "))
            print(line)
            if num == 1:
                amount = int(input("Enter Deposit Amount: "))
                bank.depositAmount(amount)
            elif num == 2:
                amount = int(input("Enter Withdrawal Amount: "))
                bank.withdrawAmount(amount)
            elif num == 3:
                bank.viewBalance()
            elif num == 4:
                bank.showDetails()
            elif num == 5:
                bank.bankReceipt()
                print("Thank You!", "\n", line)
                break
            else:
                print("Invalid Input!")
        except:
            # if user try to write options in words or anything else, then this exception is executed.
            print(line,"\nERROR! Enter a Valid Input.")
