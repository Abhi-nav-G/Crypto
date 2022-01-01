class Transfer:
    def __init__(self,name):
        self.name = name
        if self.name != "main_db":
            self.coin = 10000
        else:
            self.coin = 10000
    def send(self, p2):
        amount = int(input("Enter the amount of coin you have to send: "))
        p2.coin += amount
        self.coin -= amount
   
    

ashwin = Transfer('ashwin')
achu = Transfer('achu') 
while True:
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