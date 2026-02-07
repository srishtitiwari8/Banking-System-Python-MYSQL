import datetime

# MySQL connection
import mysql.connector
conn= mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="payment"
)


option=int(input("ENTER YOUR CHOICE \n  PRESS 1 FOR WITHDRAW: \n AND \n  PRESS 2 FOR DEPOSIT:"))
amount=eval(input("EMTER YOUR CURRENT AMOUNT HERE.."))
customer_id=int(input("ENTER YOUR I'D HERE."))
customer_name=input("ENTER YOUR NAME:")

# FUNCTION FOR WITHDRAW THE AMOUNT
def withdraw():
       bank_withdraw = eval(input("enter amount to withdraw:"))
       if bank_withdraw <= amount :
           final_amount = amount - bank_withdraw
           print(final_amount)
           a=str(customer_id)
           file=open(f"{a}.txt","w")
           file.write(f"\n customer id: {customer_id}\n customer name:{customer_name}\n current amount:{amount} \n withdraw amount:{bank_withdraw} \n final amount is {final_amount} \n ")
           now=datetime.datetime.now()
           file.write(f"date and time:{now}")
       else:
             print("YOU DON'T HAVE SUFFICIENT BALANCE.") 


       
# FUNCTION FOR DEPOSIT THE AMOUNT  
def deposite():
    bank_deposit = eval(input("enter amount to deposite: "))
    final_amount = bank_deposit + amount
    print(f"your final amount is {final_amount}")
    a=str(customer_id)
    file=open(f"{a}.txt","w")
    file.write(f"\n customer id: {customer_id}\n customer name:{customer_name}\n current amount:{amount} \n  deposit amount:{bank_deposit} \n final amount is{final_amount} \n ")
    now=datetime.datetime.now()
    file.write(f"date and time:{now}")

    curr= conn.cursor()

    sql="INSERT INTO BANK (customer_id,customer_name,amount,bank_withdraw,bank_deposit,final_amount) VALUES (%s, %s, %s, %s, %s)"
    values=(customer_id,customer_name,amount,final_amount)


    curr.execute(sql,values)
    conn.commit()
    print("✅ Data successfully inserted into orders table!")

    curr.close()
    conn.close()

#FUNCTION CALL 
if option==1:
   withdraw()
elif option==2:
    deposite()
else:
    print("INVALID CHOICE \n TRY AGAIN.")     




