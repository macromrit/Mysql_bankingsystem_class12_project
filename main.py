from numpy import void
from database import *
from crude_fun import cust_inp, func_sep, void_sep
from unique_code_gen import unique_code_gen
import datetime
from email_bot import post_email
import time

###########################################
import mysql.connector
connect = mysql.connector.connect(
    host='localhost',
    username='root',
    passwd='amma@@1953',
    database='banking_system'
)
###########################################

menu = """
------------------------
welcome to home:enter -> 
------------------------
1 -> To Log-in
2 -> To Sign-up 
3 -> To Terminate the Program
4 -> Get Super User Access
------------------------
"""

procedural_menu = """
---------------------------------------
hey.. this is your dashboard..enter->
---------------------------------------
1 -> To withdraw funds
2 -> To deposit funds
3 -> To Transfer funds
4 -> To Logout
5 -> To Delete Account
6 -> To Display Account Balance and info
---------------------------------------
"""

while True:
    print(menu)
    desiration = cust_inp('(what do ya wanna do)-> ', 's')
    void_sep(1)
    if desiration in list('1234'):
        
        if desiration=='1':#login
            print('Enter necessary details to Log-In')
            name = cust_inp('Enter username: ', 's')
            user_id = cust_inp('Enter bank id: ', 's')
            password = cust_inp('Enter password: ', 's')
            authenticated, real_name, real_id, real_email = authenticate_user(name, user_id, password)
            if authenticated:
                print('Logged-In Successfully')
                time.sleep(1)
                void_sep()
                while True:
                    print(procedural_menu)
                    preference = cust_inp('(what do ya wanna do)-> ', 's')
                    void_sep(1)
                    if preference in list('123456'):

#withdrawal--------------------------------------------------------------------------------------------------->                        
                        if preference == '1':#withdrawal
                            amount = cust_inp('Enter the amount to be withdrawn: ', 'f')
                            processing = withdraw_funds(real_name, real_id, amount)
                            
                            if processing[0]:
                                print('Withdrawal successful')  
                                print(processing[1])
                                post_email(real_email, 'Withdrawed Funds Successfully', processing[1])
                                time.sleep(0.5)
                                
                            else:
                                void_sep()
                                print("Ooopss.... Something went wrong..might be that you account had insufficient balance.. or exceeded the withdrawal limit -> 60grand")   
                            
                            func_sep()
                                                         
#deposital--------------------------------------------------------------------------------------------------->                        
                        elif preference == '2':#deposit
                            amount = cust_inp('Enter the amount to be deposited: ', 'f')
                            processing = deposit_funds(real_name, real_id, amount)
                            
                            if processing[0]:
                                print('deposited successfully')  
                                print(processing[1])
                                post_email(real_email, 'Deposited Funds Successfully', processing[1])
                                time.sleep(0.5)
                                
                            else:
                                print("Ooopss.... Something went wrong..might be that you have exceeded the deposition limit.. or gave an invalid input")   
                            func_sep()

#transfer--------------------------------------------------------------------------------------------------->                                  
                        elif preference == '3':#transfer
                            recievers_name = cust_inp('Enter receiver\'s username: ', 's')
                            recievers_id = cust_inp('Enter receiver\'s bank id: ', 's') 
                            checky_cursor = connect.cursor()
                            checky_cursor.execute(F"SELECT name, unique_id, email from account_holders where unique_id = '{recievers_id}'")
                            main_val = [x for x in checky_cursor.fetchall()]
                            
                            if main_val:
                                if (recievers_name, recievers_id) == main_val[0][0:2] and main_val:
                                    amount = cust_inp('Enter the amount to be transferred: ', 'f')
                                    x, reciept = transfer_funds(real_name, real_id, amount, recievers_name, recievers_id)
                                    if x: 
                                        print('Fund Transfer Successful')
                                        void_sep()
                                        print(reciept)
                                        #email
                                        post_email(real_email, 'Transferred Funds Successfully', reciept)
                                        post_email(main_val[0][2], 'Received Funds Successfully', reciept)
                                        time.sleep(0.5)
                                        
                                    else: print('Ooppss.. amount wasn\'t valid! Try again. Transcation unsuccessful!')
                                
                                else: print('Ooopss.. no such user was detectable.. Try again with valid info!!')
                            
                            else: print('Ooopss.. no such user was detectable.. Try again with valid info!!')
                            func_sep()
#logout--------------------------------------------------------------------------------------------------->                         
                        elif preference == '4':#logout
                            print('Logging-Out...')
                            time.sleep(1)
                            print('Logged Out Successfully')
                            func_sep()
                            break

#delete--------------------------------------------------------------------------------------------------->                              
                        elif preference == '5':#delete
                            assurity = cust_inp('Are ya sure ya wanna delete this account(y/n->any character): ', 's').casefold()
                            if assurity=='y':
                                delete_user(real_id)
                                print(F'{real_name}\'s account has been deleted successfully')
                                time.sleep(1)
                                
                            else:
                                print('Oh.. gr8 that ya have changed ya mind')
                            
                            func_sep()

#display-detail-------------------------------------------------------------------------------------------->                                    
                        elif preference == '6':#display
                            print(display_balance(real_id)[1])
                            time.sleep(1)
                            func_sep()
                        
                        else: pass
                        
                    else: print('Invalid input!!')
                        
                
            else:
                void_sep()
                print("user-id, username and password didn't match!! or no such user found!!")
                func_sep()
                
        elif desiration=='2':#signup
            while True:
                '''name: str,
                    gender: str,
                    age: int,
                    nationality: str,
                    unique_id: str,
                    phone_no: str,
                    email: str,
                    date_created: str,
                    balance: float,
                    password: str'''
                    
                print('''
--------------------------------                      
Fill up the required details: ->
--------------------------------
                      ''')
                #name
                while True:
                    name = cust_inp('Enter your name: ', 's')
                    if 80>len(name)>4: break
                    else: print('Ooopss.. Try again.. the input was incorrect!!')
                void_sep()   
                #gender
                while True:
                    gender = cust_inp('Enter your gender(m/f): ', 's')
                    if (len(gender)==1) and (gender in list('mf')): break
                    else: print('Ooopss.. Try again.. the input was incorrect!!')
                void_sep()   
                #age
                while True:
                        age = cust_inp('Enter your age: ', 'i')
                        if 150>age>18: break
                        else: print('Ooopss.. Invalid age.. Try again!')
                void_sep()   
                #nationality
                while True:
                    nationality = cust_inp('Enter your nationality: ', 's')
                    if 120>len(nationality)>2: break
                    else: print('Ooopss.. Invalid input.. Try again!')
                void_sep()   
                #uniqueid
                unique_id = unique_code_gen()
                
                #phone_no
                while True:
                    phone_no = cust_inp('enter your 10digit phone no.: ', 's')
                    isalldigit = list()
                    for i in phone_no: isalldigit.append(i.isdigit())
                    if False in isalldigit: print('Oops.. Try again no alpha characters allowed')
                    elif len(phone_no)!=10: print('Oops.. Try again it should have 10 numbers')
                    else: break 
                void_sep()   
                
                #email
                while True:
                    email = cust_inp('Enter your email: ', 's')
                    if ('@' in email) and (('.com' in email) or ('.in' in email)): break
                    else: print('Ooopss.. Enter invalid input!')
                void_sep()   
                
                #balance                
                balance = 0
                
                #password
                while True:
                    password = cust_inp('Set Password: ', 's')
                    passwordconf = cust_inp('Renter the Password: ', 's')
                    
                    if (password==passwordconf) and (len(password)>7): break
                    else: print('ensure your password has 8 characters or more!! or might be that passwords didn\'t match')                        
                void_sep()   
                
                #date_created
                date_created = str(datetime.datetime.now())
                
                print('balance initialized to 0.. deposit cash if wanted after logging in')
                void_sep()
                z = create_user(name, gender, age, nationality, unique_id, phone_no, email, date_created, balance, password)
                
                if z: 
                    print('Account Created successfully')
                    content =     F'''
###############################################                        
Account Created Successfully
----------------------------
Account info:
name                  : {name}
user id               : {unique_id}
email                 : {email}
date and time created : {date_created}
gender                : {gender}
age                   : {age}
###############################################                        
                        '''
                    print(content)
                    #emailng
                    post_email(email, 'Account Created in Dopethon Finance Successfully', content)
                    func_sep()
                    time.sleep(1)
                    break
                else: 
                    main = cust_inp('ya wanna try creating an account again)(y/n): ', 's').casefold()
                    if main=='y':pass
                    elif main=='n': break
        
        elif desiration=='3':#terminate
            print('Thanks for choosing us..Catch ya Soon!!!') 
            break

#Super user processal
#------------------------------------------------------------------------------------------------------------------------->        
        elif desiration=='4':#super user processal
            super_user_access()
            time.sleep(1)
            void_sep()
            func_sep()
        else:pass
        
    
    else:
        print('Invalid input.. Try again!')
