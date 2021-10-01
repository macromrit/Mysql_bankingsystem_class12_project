#------------------------------------------------------------->
# from enum import unique
from logging import exception
import time
import mysql.connector as mq
from mysql.connector.errors import DatabaseError
from matplotlib import pyplot as pt
#crude_fun
from crude_fun import func_sep, ref_all, void_sep
import datetime
from crude_fun import cust_inp
from super_user import super_users
import csv
#------------------------------------------------------------->
try:
    main_connection = mq.connect(host='localhost',
                                username='root',
                                passwd='amma@@1953',
                                database='banking_system')
    connected = True
    
except DatabaseError:
    connected = False
    
if connected:
    
    def create_user(name: str,
                    gender: str,
                    age: int,
                    nationality: str,
                    unique_id: str,
                    phone_no: str,
                    email: str,
                    date_created: str,
                    balance: float,
                    password: str,
                    pincode: str
                    )->bool:
        
        create_cursor = main_connection.cursor()
        created = False
        
        try:
            create_cursor.execute(
'''INSERT INTO account_holders VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
(name, gender, age, nationality, unique_id, phone_no, email, date_created, balance, password, pincode)
        )
            main_connection.commit()
            created=True
        
        except:
            #in case of error.. rolling back to norm
            main_connection.rollback()

        create_cursor.close()
        return created

#Login
#-------------------------------------------------------------------------------------------------------->    
    def authenticate_user(name: str, 
                          user_id: str, 
                          password: str)->bool and str:
        check_cursor = main_connection.cursor()
        try:
            check_cursor.execute(F"SELECT name, unique_id, password, email, pincode FROM account_holders where name like '{name}'")
            info = [x for x in check_cursor.fetchall()]
        except:
            print('issue2: data renderance error')
        # check_cursor.close()
        
        authenticated = False
        if info:
            if name==info[0][0] and user_id==info[0][1] and password==info[0][2]: authenticated = True
            else:pass
        
        else: pass
        
        if authenticated: return (authenticated, name, user_id, info[0][3], info[0][4])
        else: return authenticated, None, None, None, None
        
#delete       
#-------------------------------------------------------------------------------------------------------->    
    def delete_user(user_id: str)->bool:
        delete_cursor = main_connection.cursor()
        deleted = False
        try:
            delete_cursor.execute(F"DELETE FROM account_holders where unique_id='{user_id}'")
            main_connection.commit()
            deleted = True
        except:
            #in case of error.. rolling back to norm
            main_connection.rollback()
        delete_cursor.close()

        return deleted

#update pin
#-------------------------------------------------------------------------------------------------------->    
    def update_pin(user_id: str,
                new_pin: str)->bool:
        update_pin_cursor = main_connection.cursor()
        updated = False
        try:
            update_pin_cursor.execute('UPDATE account_holders set pincode=%s where unique_id=%s',
                                    (new_pin, user_id))
            main_connection.commit()
            updated = True
        except:
            main_connection.rollback()
            print('Error')
        update_pin_cursor.close()
        
        return updated


#withdrawal
#-------------------------------------------------------------------------------------------------------->    
    def withdraw_funds(user_name: str,
                       user_id: str,
                       amount: float)->bool:
        with_cursor = main_connection.cursor()
        try:
            # with_cursor.execute("SELECT balance FROM account_holders WHERE unique_id = %s", (user_id))
            with_cursor.execute(F"SELECT balance FROM account_holders WHERE unique_id = '{user_id}'")
            balance = [x[0] for x in with_cursor.fetchall()]
        except:
            print('issue2: data renderance error')
        
        withdrawal = False
        if balance[0]>=amount>0 and 0<amount<=60000:
            upd_balance = balance[0]-amount
            try:
                with_cursor.execute("UPDATE account_holders SET balance = %s WHERE unique_id = %s", (upd_balance, user_id))
                with_cursor.execute("INSERT INTO history(user_id, mode, amount, time, sudo_balance) values(%s, %s, %s, %s, %s)", (user_id, 'w', amount, str(datetime.datetime.now()), upd_balance))
                main_connection.commit()
                withdrawal = True
            except:
                #in case of error.. rolling back to norm
                print('exception raised line 115')
                main_connection.rollback()
        else:pass
        
        with_cursor.close()
        
        if withdrawal:
            return withdrawal,  ref_all('w', user_name, user_id, amount, upd_balance, str(datetime.datetime.now()))
        else:
            return withdrawal, None
        

#deposition        
#-------------------------------------------------------------------------------------------------------->    
    def deposit_funds(user_name: str,
                       user_id: str,
                       amount: float)->bool:
        depo_cursor = main_connection.cursor()
        try:
            depo_cursor.execute(F"SELECT balance FROM account_holders WHERE unique_id = '{user_id}'")
            # depo_cursor.execute("SELECT balance FROM account_holders WHERE unique_id = %s", (user_id))
            balance = [x[0] for x in depo_cursor.fetchall()]
        except:
            print('issue2: data renderance error')
        
        deposited = False
                
        if 1000000>=amount>0:
            try:
                upd_balance = balance[0]+amount
                depo_cursor.execute("UPDATE account_holders SET balance = %s WHERE unique_id=%s", (upd_balance, user_id))

                depo_cursor.execute("INSERT INTO history(user_id, mode, amount, time, sudo_balance) VALUES(%s, %s, %s, %s, %s)", (user_id, 'd', amount, str(datetime.datetime.now()), upd_balance))
                main_connection.commit()
                deposited=True
            except:
                #rolling back incase of error
                main_connection.rollback()
            depo_cursor.close()
        else: pass
        
        if deposited: return deposited, ref_all('d', user_name, user_id, amount, upd_balance, str(datetime.datetime.now()))
        else: return deposited, None
    

#transfer    
#-------------------------------------------------------------------------------------------------------->
    def transfer_funds(user_name: str,
                       user_id: str,
                       amount: float,
                       recievers_name: str,
                       recievers_id: str):
        
        transfer_cursor = main_connection.cursor()
        try:
            transfer_cursor.execute(F'SELECT balance FROM account_holders WHERE unique_id = \'{user_id}\'')
            sender_balance = [x for x in transfer_cursor.fetchall()]
            transfer_cursor.execute(F'SELECT balance FROM account_holders WHERE unique_id = \'{recievers_id}\'')
            reciever_balance = [x for x in transfer_cursor.fetchall()]
        except:
            print('Phase Error-I')
        transferred = False
        if 0<amount<sender_balance[0][0]:
            
            try:
                #deducting cash from sender
                updating_cursor = main_connection.cursor()
                upd_senders_balance = sender_balance[0][0] - amount
                updating_cursor.execute(F'UPDATE account_holders SET balance = {upd_senders_balance} WHERE unique_id = \'{user_id}\'')
                updating_cursor.execute("INSERT INTO history VALUES(%s, %s, %s, %s, %s, %s)", (user_id, 'ts', amount, recievers_id, datetime.datetime.now(), upd_senders_balance))
                #depositing cash to the receiver
                upd_recievers_balance = reciever_balance[0][0] + amount
                updating_cursor.execute(F'UPDATE account_holders SET balance = {upd_recievers_balance} WHERE unique_id = \'{recievers_id}\'')
                updating_cursor.execute("INSERT INTO history VALUES(%s, %s, %s, %s, %s, %s)", (recievers_id, 'tr', amount, None, datetime.datetime.now(), upd_recievers_balance))
                main_connection.commit()
                transferred = True
            except:
                print('Connectivity Error')
                main_connection.rollback()
            
            if transferred: return transferred, ref_all('t', user_name, user_id, amount, recievers_name, recievers_id, amount, str(datetime.datetime.now())), upd_senders_balance, upd_recievers_balance
            else: return transferred, None, None, None
        
        else: 
            return transferred, None, None, None
        
#balance enquiry    
#-------------------------------------------------------------------------------------------------------->
    def display_balance(user_id: str):
        dis_cursor = main_connection.cursor()
        try:
            dis_cursor.execute(F"SELECT name, unique_id, balance, date_created from account_holders where unique_id = '{user_id}'")
            vals = [x for x in dis_cursor.fetchall()]
        except:
            print('issue2: data renderance error')
        dis_cursor.close()
        
        return True, ref_all('b', vals[0][0], vals[0][1], vals[0][2], vals[0][3])
    
#transaction history   
#-------------------------------------------------------------------------------------------------------->

    def csv_transactions(filename: str,
                         user_id: str)->bool:
        process = False
        try:
            history_cursor = main_connection.cursor()
            history_cursor.execute('SELECT * FROM history WHERE user_id = %s', (user_id,))
            with open(F'user_transactions/{filename}.csv', 'w', newline='') as writting: 
                actual = csv.writer(writting, delimiter=',')
                actual.writerow(['Your-Id', 'Debited', 'Credited', 'Balance-History', 'Transaction-Time'])
                for i in list(history_cursor):
                    if i[1] in ('ts', 'w'): actual.writerow([i[0], '$'+str(i[2]) , '-----', '$'+str(i[5]), i[4]])
                    else: actual.writerow([i[0], '-----', '$'+str(i[2]), '$'+str(i[5]), i[4]])
                    
            history_cursor.close()
            process=True
        except: pass
        return process

    
#super user
#-------------------------------------------------------------------------------------------------------->    
    def super_user_access():
        username = cust_inp('Enter superuser\'s name: ', 's')
        check_cursor = main_connection.cursor()
        check_cursor.execute('SELECT unique_id FROM account_holders')
        main_checker = [x[0] for x in check_cursor]
        check_cursor.execute('SELECT unique_id, balance, name FROM account_holders')
        hypo_checker = [x for x in check_cursor]
        
        if username in super_users.keys():
            passcode = cust_inp('Enter password: ', 's')
            if super_users[username] == passcode:
                
                while True:
                
                    splitter = cust_inp('See user\'s info | graph comparing user\'s balance | to logout (u/g/l): ', 's')
                    if splitter == 'g':
                        check_list_y = list()
                        check_list_x = list()
                        for _ in range(1, cust_inp('How many users balance should be displayed in graph: ', 'i')+1):
                            while True:
                                val = cust_inp(F'Enter user {_}\'s code: ', 's')
                                if len(val)==10 and val in main_checker:
                                    for i in hypo_checker:
                            
                                        if i[0]==val:
                                            check_list_y.append(i[1])
                                            check_list_x.append(i[2])
                                            break
                                        else: pass
                                    break
                                                
                                else: print('No... imvalid id Try again')
                            
                        #removing the right pane
                        fig, ax = pt.subplots()
                        right_side = ax.spines["right"]
                        right_side.set_visible(False)
                        ##################################
                        
                        pt.barh(check_list_x, check_list_y, color='red')
                        pt.title('user vs user via balance')
                        for index, value in enumerate(check_list_y):
                            pt.text(value, index,
                            str(value))
                        pt.xlabel('Balance', fontweight='bold')
                        pt.ylabel('Name', fontweight='bold')
                        pt.grid(True)
                        pt.show()
                    
                    elif splitter=='u':
                        valo = cust_inp('Enter user\'s code: ', 's')
                        new_cur = main_connection.cursor()
                        new_cur.execute(F"SELECT * FROM account_holders WHERE unique_id = '{valo}'")                    
                        vals = [x for x in new_cur.fetchall()]
                        if len(valo)==10 and valo in main_checker:

                            print(F"""
--------------------------------
User Details
--------------------------------                              
Username     :{vals[0][0]}                          
Gender       :{vals[0][1]}
Age          :{vals[0][2]}
Nationality  :{vals[0][3]}
Unique Id    :{vals[0][4]}
Phone Number :{vals[0][5]}
E-mail       :{vals[0][6]} 
Date Created :{vals[0][7]}
Balance      :${vals[0][8]}
Password     :{vals[0][9]}
Pin-Code     :{vals[0][10]}
--------------------------------

                            """)
                        else: print('Ooopss..No such user found!')
                    
                    elif splitter=='l':
                        print('Logging-Out Superuser')
                        time.sleep(1)
                        break
                                    
                    else: 
                        print('Invalid Input... Try again')
                        void_sep()
                    
            else: print('Oooops! invalid password')

        else: print('Ooops! No such user found')
    
    
#le end    
#-------------------------------------------------------------------------------------------------------->
    if __name__=='__main__': pass

else: print('issue1: mysql connectivity error') 
