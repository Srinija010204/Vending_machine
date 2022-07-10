initial_balance =200 #balance in the vending machine
present_earning = 0
code = {1: 'waterbottle', 2: 'dairymilk', 3: 'cooldrink', 4: 'pepsi', 5: 'icecream'}
item = {'waterbottle': [50, 100], 'dairymilk': [40, 80], 'cooldrink': [60, 150], 'pepsi': [10, 55],
            'icecream': [80, 200]}

print("____MENU____(with code)")
print("\n")
    
for x,y in code.items():
    print(x,y)



def products(item_code):
    global code, item
    item[code[item_code]] # item.get(code.get(item_code))
    print(f"There are {item[code[item_code]][1]} items and it costs {item[code[item_code]][0]} Rs per item.")
    return None

def user_requirement():

    global initial_balance, code, item, present_earning

    b=int(input("enter product_code: "))
    products(b)
    c=int(input("enter number_of_pieces: "))
    d=int(input("enter amount: "))
    if (initial_balance < d-c*item[code[b]][0]) or (d < c * item[code[b]][0]):
        print(f"sorry please provide amount {item[code[b]][0]*c}  ")
        return None

    else:
        x = d - c * item[code[b]][0]
        initial_balance -= x
        present_earning += c*item[code[b]][0]
        initial_balance += present_earning
        print(f"collect the item and the change of rupees {x}")
        item[code[b]][1] = item[code[b]][1] -c
        return None

while True:
    x=input("do you want to stop the program? (y/n): ")
    if x=="y":
        print(f"the earnings for today is rs {present_earning} and the balance in the machine is {initial_balance-present_earning}")
        break
    user_requirement()


