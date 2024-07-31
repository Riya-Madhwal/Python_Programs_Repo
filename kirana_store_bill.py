import time
sum = 0
l1 = []
l2 = []

while(True):
 item_name = input("enter the  valid item name or press q to quit!")
 item_price = input("enter the valid item price or press q to quit!")

 if item_name != 'q' and item_price != 'q':
    l1.append(item_name)
    l2.append(item_price)
    sum = sum + int(item_price)

 elif item_name == 'q' and item_price == 'q':
  print("x--------------Welcome to SRIRAM STORES---------------x")
  print("-------------------generating bill--------------------")
  time.sleep(3)
  for (i, j) in zip(l1, l2):
    print(i, j)
  break

 else:
  print("do you really want to quit?, if yes please enter 'q' in both")


print(f"your total bill ------{sum}")

print("Thanks for shopping with us! Please visit again")