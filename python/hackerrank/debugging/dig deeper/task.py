def Wallet(bills, numberOfBills):
    total = 0
    for x in range(0, len(numberOfBills)):
        total = total + (bills[x] * numberOfBills[x])
    return(total)