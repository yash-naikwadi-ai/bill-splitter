pay=float(input("Enter your total bill amount:"))
if pay>0:
    splitno=int(input("Enter no customer together:"))
    if splitno>0:
        
        amt=pay/splitno
        print("Each customer has",amt,"$ to pay.")
        print("-------------------------------------------")
        print("_FINAL_ORIGINAL_BILL_=",pay,"$")
        print("_NO_OF_PAYERS_IN_SINGLE_BILL=",splitno)
        print("_FINAL_PER_PERSON_BILL_=",amt,"$")
        print("THANKS")
        print("-------------------------------------------")
    else :
        print("_INVALID_NUMBER_OF_CUSTOMERS_")
else:
    print("_INVALID_BILL_AMOUNT_")
