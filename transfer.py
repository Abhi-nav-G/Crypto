class Transfer:
    def __init__(self,name):
        self.name = name
        self.coin = 10
    def send(self, p2):
        amount = int(input("Enter the amount of coin you have to send: "))
        p2.coin += amount
        self.coin -= amount
ashwin = Transfer('ashwin')
achu = Transfer('achu') 
quest = input("whom do you want to send money: ")
if quest == "achu":
   ashwin.send(achu)
elif quest == "ashwin":
    achu.send(ashwin)
else:
    print("no other user created")



print("Balance of achu: ",achu.coin)
print("Balance of ashwin: ", ashwin.coin)

