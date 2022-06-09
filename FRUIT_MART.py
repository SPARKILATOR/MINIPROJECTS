import time
price = {'apple':80,'banana':50,'pomegranate':120,'kiwi':100}
inventory = {'apple':80,'banana':50,'pomegranate':120,'kiwi':100}
print("---------------- WELCOME TO YASH MART ---------------------\n")
time.sleep(5)
final = {}
item_list = {}
bill = 0
print("FRUIT RATE :")
print("---------------------------\n")
print("APPLE - Rs. 80/Kg")
print("BANANA - Rs. 50/Kg")
print("POMEGRANATE/ANAR - Rs. 80/Kg")
print("KIWI - Rs. 80/Kg\n")
time.sleep(1)
#num_items = int(input("How many items :  "))
for _ in range(0,100):
    a = input("ENTER FRUIT NAME (WHICH IS PRESENT IN RATE LIST): ")
    a = a.lower()
    if a not in price:
        print("NOT AVAILABLE. SORRY ")
        continue
    b = float(input("ENTER QUANTITY (IN KGs): "))
    item_list[a] = b
    c = input("PRESS E TO end the bucket : ")
    inventory[a] = inventory[a] - b
    for i,j in price.items():
        if i == a:
            final[i] = j*b
    if c == "E":
        print("LIST ADDED SUCCESSFULLY.....")
        break
print("-----------------------------------\n")
print("FINAL BUCKET LIST :: %r" %(item_list))
time.sleep(3)
print("---------------------------------------\n")
print("PLEASE WAIT WHILE WE PROCESS YOUR BILL ...\n")
time.sleep(5)
print("FINAL CHECKOUT \n")
for i,j in final.items():
    bill = bill + j
    print("%r     -     Rs. %r" %(i,j))
print("---------------------------------------\n")
print("PLEASE PAY THE TOTAL AMOUNT : Rs. %r " %(bill))
print("---------------------------------------\n")
print("THANKS FOR COMING. VISIT AGAIN")
print("INVENTORY REMAINING (ONLY FOR STAFF USE) :: %r " %(inventory))
            
