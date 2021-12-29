class Transfer:
    def __init__(self,name):
        self.name = name
        if self.name != "main_db":
            self.coin = 10
        else:
            self.coin = 100
    def send(self, p2):
        amount = int(input("Enter the amount of coin you have to send: "))
        p2.coin += amount
        self.coin -= amount
    def buy(self, p2):
        cbuy = int(input("Enter how many coins you have to buy: "))
        p2.coin+= cbuy
        self.coin -= cbuy
    
main_db = Transfer("main_db")
ashwin = Transfer('ashwin')
achu = Transfer('achu') 
while True:
    question = input("Do you want to buy coin(y/n): ")
    if question == "y":
        user = eval(input("Enter username: "))
        main_db.buy(user)



    if question == "n":
        quest = input("do you want to send money(y/n): ")
        if quest == "y":
            quest = input("whom do you want to send money: ")
            if quest == "achu":
                ashwin.send(achu)
            elif quest == "ashwin":
                achu.send(ashwin)
            else:
                print("no other user created")
        elif quest == "n":
            print('bye-bye')



    print("Balance of achu: ",achu.coin)
    print("Balance of ashwin: ", ashwin.coin)

    yn = input("Do you want to send again")
    if yn == "n":
        break