def deposit():
    while True:
        amount=input("Enter you deposit: ")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Amount must be grater than 0")
        else:
            print("Enter a amount.")
            
    return amount
        
deposit()

