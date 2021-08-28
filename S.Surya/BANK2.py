##import mysql.connector as f
##p=f.connect(host="localhost",user="root",passwd="root",database="banking system")
def transfer():
    import mysql.connector as f
    p=f.connect(host="localhost",user="root",passwd="root",database="banking system") 
    k=input("enter your name")
    q=input("enter your unique id")
    r=int(input("enter amount to be transferred"))
    b=p.cursor()
    try:
        b.execute(F"select balance from account_holders where unique id='{q}'")
        balance=[x[0] for x in b.fetchall()]
    except:
        print("data not found")
    if 
