##import mysql.connector as f
##p=f.connect(host="localhost",user="root",passwd="root",database="banking system")
def transfer():
    import mysql.connector as f
    p=f.connect(host="localhost",user="root",passwd="root",database="banking system") 
    k=input("enter your name")
    q=input("enter your unique id")
    r=int(input("enter amount to be transferred"))
    m=input("enter unique id of receiver")
    z=input("enter receiver name") 
    b=p.cursor()
    try:
        b.execute(F"select balance from account_holders where unique id='{q}'")
        balance=[x[0] for x in b.fetchall()]
    except:
        print("data not found")
    if balance[0]>=r and r<=30000:
        upd_bal=balance[0]-r
        b.execute(F"update account_holders set balance ='{upd_bal}' where unique_id='{q}'")
        b.commit()
        b.execute("select * from account_holders where unique_id='{q}'")
    try:
       b.execute(F"select balance from account_holders where unique id='{m}'")
       balance=[x[0] for x in b.fetchall()] 
       uid=[x[2] for x in b.fetchall()]
    except:
        print("data not found")
    try:
      upd_balc=balance[0]+r   
      b.execute(F"update account_holders set balance ='{upd_balc}' where unique_id='{m}'")
      b.commit()
      b.execute("select * from account_holders where unique_id='{m}'")
      print("transfer complete")
