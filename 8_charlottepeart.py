#Define account balance and attempts

acc_bal = 100
count = 3

try:

    #define 3 attempts
    for attempt in range(count):
        #define input and target pin
        input_pin = float(input("Please enter pin code:"))
        target_pin = 1111

        #if match occurs
        if input_pin == target_pin:
            #request withdrawal amount
            withdrawal_amount = float(input("Please type the amount you wish to withdraw:"))
            rem_acc_bal = acc_bal - withdrawal_amount
            #exit loop if too much is withdrawn
            if rem_acc_bal < 0:
                print("Not enough money in account")
                break
            else:
                #print reciept and success if enough money present
                print("You have {} pounds remaining".format(rem_acc_bal))
                raise Exception

        #If pin incorrect
        if input_pin != target_pin:
            #reduce the attempts remaining
            count = count - 1
            print("Incorrect pin. You have {} attempts remaining".format(count))
            #if number of attempts exceeded
            if count == 0:
                #exit for loop and transaction
                print("Too many attempts. You must contact your bank for approval.")
                pass

except:
    print("Transaction complete")

