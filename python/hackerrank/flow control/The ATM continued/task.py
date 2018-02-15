class atm:
    def __init__(self,balance):
        f = open("balance.txt","w")
        ##User code
        self.balance = balance
        ##User Code End
        f.write(str(self.balance))
        f.close()
        
    def withdraw(self,amount):
        ##User Code
        withraw_prompt = "You have selected to withdraw money from the account"
        ##User Code End
        f = open("withdraw.txt","w")
        f.write(withraw_prompt+"\n")
        
        ##User code
        print(withraw_prompt)
        self.amount = amount
        reply = "You have $"+str(self.balance-self.amount)+".00 left"
        print(reply)
        
        ##User Code End

        f.write(reply)
        f.close()
    
    def deposit(self,amount):
        f = open("deposit.txt","w")
        self.amount = amount
        user_prompt = "You have selected to deposit money to the account"
        deposit_ans = "Your new balance is $"+str(self.balance+self.amount)+".00"
        print(user_prompt)
        print(deposit_ans)
        f.write(user_prompt+"\n")
        f.write(deposit_ans)
        f.close()
        
    def setBalance(self,balance):
        self.balance = balance

    def cancel(self):
        f = open("cancel.txt","w")
        cancel_reply = "Returning to account selection."
        self.cancel = self
        print(cancel_reply)
        f.write(cancel_reply)
    def default():
        print("You have selected an Invalid option")

    def finished(self,choice):
        f = open("finished.txt","a")
        self.choice = choice
        if self.choice == "derp":
            invalid_option = "You have selected an Invalid option"
            f.write(invalid_option+"\n")
            print(invalid_option)
            f.close()
        else:
            if self.choice == "Yes":
                return_main_menu = "Returning to main menu"
                f.write(return_main_menu+"\n")
                print(return_main_menu)
                f.close()
            else:
                have_nice_day = "Have a nice day!"
                f.write(have_nice_day+"\n")
                print(have_nice_day)
                f.close()

   