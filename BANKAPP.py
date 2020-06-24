import sys
import time
class Banker:
    '''
       The Silly Bank of Irkia (SBI) is an  multinational, public sector banking and financial services statutory body. It is a government corporation
       statutory body headquartered in Jamty. SBI is ranked as 236th in the Fortune Global 500 list of the world's biggest corporations of 2019.
       It is the large bank with a 23% market share in assets, besides a share of one-fourth of the total loan and deposits market.
       The bank descends from the Bank of Calcutta, founded in 1806, via the Imperial Bank of India, making it the oldest commercial bank in the
       Indian subcontinent. The  merged into the other two "presidency banks" , the Bank of Cal and the Bank of Bom, to form the Imperial Bank,
       which in turn became the Silly Bank of Irkia in 1955. The Government took control of the Imperial Bank in 1955, with Reserve Bank (central bank)
       taking a 60% stake, renaming it the Silly Bank of Irkia.
    '''
    bankname="SILLY BANK OF IRKIA (SBI)"
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance

    def deposit(self,amt):
        self.balance = self.balance + amt
        print "AMOUNT DEPOSITED SUCCESSFULLY"
        print "ACCOUNT BALANCE ::: ",self.balance

    def withdraw(self,amt):
        if amt>self.balance:
            print "INSUFFCIENT FUNDS ...."
            print "EXITING FROM THE HERE REDIRECTING TO THE OPTIONS PAGE...."
            stay()
        else:
            print "WITHDRAWED SUCCESSFULLY"
            self.balance = self.balance - amt
            print "ACCOUNT BALANCE ::: ",self.balance

    def info(self,accno,ifsc,mobile):
        self.accno=accno
        self.ifsc=ifsc
        self.mobile=mobile
        print "ACCOUNT NO. == ",self.accno
        print "IFSC code   == ",self.ifsc
        print "Mobile No.  == ",self.mobile

print "--------------WELCOME TO  THE {} ---------------".format(Banker.bankname)
print "-----------------------------------------------------------------------------------------------"
name = raw_input("ENTER UR NAME ::: ")
l=name.split(" ")
time.sleep(1)
print "Hi {} hope u are doing good... ".format(l[0])
print "-----------------------------------------------------------------------------------------------------------------"
print "So at the START we want some account related information so please tell, it will be CONFIDENTIAL...."
print "---------------------------------------------------------------------------------------------------------------------------------"
time.sleep(1)
b = Banker(name)
while True:
    accno = raw_input("ENTER ur 11 digit ACCOUNT NUMBER::")
    if len(accno) == 11:
       print "OK ACCEPTED."
       break
    else:
       print "it shd be of 11 chracters"
while True:
    ifsc = raw_input("ENTER ur 5 digit IFSC NUMBER::")
    if len(ifsc) == 5:
       print "OK ACCEPTED."
       break
    else:
       print "it shd be of 5 chracters"
while True:
    mobile = raw_input("ENTER ur 10 digit mobile NUMBER::")
    if len(mobile) == 10:
       print "OK ACCEPTED."
       break
    else:
       print "it shd be of 5 chracters"
count=0
def stay():
    print "WANT TO CONTINUE IN THE APP :: PRESS \'N\' for NO else PRESS ENTER key "
    n = raw_input("CHOSE OPTION (Y or N) ::")
    if n == 'N' or n == 'n':
        time.sleep(1)
        print "THANKS FOR USING OUR SERVICES...."
        sys.exit()
print "------------------WELCOME TO THE WORLD OF MODERNISED BANKING-----------------------"
print "PLEASE WAIT WHILE WE ARE LOADING THE STUFFS FOR U .........................."
while True:
    time.sleep(2)
    print "--------------------------------------------------"
    print "Choose the options given below to use this APP:::"
    print "----------------------------------------------------------------------------------------------------------------------------------"
    print "ENTER \'d\' for DEPOSIT\nENTER \'w\' for WITHDRAW\nENTER \'e\' for EXIT\nENTER \'b\' for BALANCE CHECK\nENTER \'i\' info about the account details\nENTER \'a\' for BANK HISTORY"
    option=raw_input("CHOOSE UR OPTION ::: ")
    if option == 'd' or option == 'D':
        amt = float(raw_input("HOW MUCH AMOUNT U WANT TO DEPOSIT :: Rs."))
        time.sleep(2)
        b.deposit(amt)
        print "------------------------------------------------------------------------------------------------------------------------------"
        stay() 
    elif  option == 'w' or option == 'W':
        amt = float(raw_input("HOW MUCH AMOUNT U WANT TO WITHDRAW :: Rs."))
        time.sleep(1)
        b.withdraw(amt)
        print "-------------------------------------------------------------------------------------------------------------------------------"
        stay()
    elif  option == 'e' or option == 'E':
        amt = raw_input(" ---------------------------THANKS FOR BANKING WITH US------------------------ ")
        time.sleep(1)
        sys.exit()
    elif option == 'b' or option == 'B':
        time.sleep(1)
        print "UR ACCOUNT BALANCE IS :: ",b.balance
        if b.balance < 1000:
            print "PLEASE MAINTAIN A MINIMUM OF Rs. 1000 IN THE ACCOUNT"
        print "-----------------------------------------------------------------------------------------------------------------------------------"
    elif option == 'i' or option == 'I':
        time.sleep(1)
        print "ACCOUNT DETAILS::::::::::"
        print "-------------------------------------"
        b.info(accno,ifsc,mobile)
        print "-----------------------------------------------------------------------------------------------------------------------------------"
    elif option == 'a' or option == 'A':
        time.sleep(1)
        print "ABOUT::::::::::"
        print "-------------------------------------"
        print Banker.__doc__
    else:
        print "---------------------ENTER CORRECTLY, OPTION CHOSEN IS INCORRECT---------------------------"
        count+=1
        print "{} Attempts remaining".format(4-count)
    if count > 3:
        print "*****SORRY FOR THE INCONVENIENCE*****"
        print "REACHED MAX ATTEMPTS.... EXITING"
        sys.exit()

