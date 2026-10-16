number = int(input("how many acc do you need: "))
balance = 1500
acc_details = []
for i in range(number):
    print(f"\n--- Account {i + 1} ---")
    name = str(input("name: "))
    pan_no = input("enter your pan number: ")
    accno = int(input("enter your account number: "))
    dob = input("enter your date of birth: ")
    email = input("email: ")
    address = str(input("enter your address(place): "))
    cont = str(input("enter your contry: "))
    new_balance = int(input("enter the new balance: "))
    current_bal = new_balance
    tupledata = (accno, name, pan_no, dob)
    listdata = [email, address, cont, current_bal]
    bank_details = (tupledata, listdata)
    acc_details.append(bank_details)
while True:
    print("\n====================")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show accounts")
    print("====================")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        acc_no = int(input("Enter account number to deposit into: "))
        for acc in acc_details:
            tupledata, listdata = acc
            if tupledata[0] == acc_no:
                amount = float(input("Enter amount to deposit: "))
                listdata[3] += amount
                print(f"Deposited successfully! Current balance: {listdata[3]}")
                break
    elif choice == 2:
        acc_no = int(input("Enter account number to withdraw from: "))
        for acc in acc_details:
            tupledata, listdata = acc
            if tupledata[0] == acc_no:
                amount = float(input("Enter amount to withdraw: "))
                if listdata[3] >= amount:
                    listdata[3] -= amount 
                    print(f"Withdrawn successfully! Current balance: {listdata[3]}")
                else:
                    print("Insufficient balance!")
                break
            
    elif choice == 3:
        print("\nThe bank details are:")
        for acc in acc_details:
            print(acc)
    else:
        print("Invalid choice! Please select between 1 and 3.")