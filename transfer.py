class Transfer:
    def __init__(self,name):
        self.name = name
        self.coin = 10
    def send(self, p2):
        amount = int(input("Enter the amount of coin you have to send: "))
        p2.coin += amount
        self.coin -= amount

achu = Transfer('achu')
ashwin = Transfer('ashwin')

achu.send(ashwin)
print("Balance of achu: ",achu.coin)
print("Balance of ashwin: ", ashwin.coin)

