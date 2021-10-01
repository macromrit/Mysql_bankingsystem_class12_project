import random
import mysql.connector as mysq
from mysql.connector.errors import DatabaseError

try:
    main_conn = mysq.connect(host='localhost',
                            username='root',
                            passwd='amma@@1953',
                            database='banking_system')
    connected = True

except DatabaseError:
    connected = False

if connected:
    auth_cursor = main_conn.cursor()
    try:
        auth_cursor.execute('SELECT unique_id FROM account_holders')
        id_infos = [x[0] for x in auth_cursor.fetchall()]
    except:
        print('issue2: data renderance error')
    auth_cursor.close()
    main_conn.close()

    def unique_code_gen():
        """
        usr_code composition: 
            total_len = 10    
            upper_alpha = 3chrs
            lower_alpha = 3chrs
            digits = 2chrs
            special_chrs = 2chrs
            :-> 3:3:2:2 -> 10chrs
        """
        while True:
        
            upper_alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            lower_alpha = list('abcdefghijklmnopqrstuvwxyz')
            digits = list('0123456789')
            special_chrs = list('#&@')
            
            crude_code = list()
            
            for _ in range(3): crude_code.append(random.choice(upper_alpha))
            
            for _ in range(3): crude_code.append(random.choice(lower_alpha))
            
            for _ in range(2): crude_code.append(random.choice(digits))
            
            for _ in range(2): crude_code.append(random.choice(special_chrs))
            
            random.shuffle(crude_code)
            
            
            auth_code = ''
            
            for chrs in crude_code: auth_code+=chrs
            
            if auth_code in id_infos: pass
            else: break
        
        return auth_code
    
    def unique_otc_email_auth():
        psudo_code = ''
        for i in range(4):
            psudo_code+=str(random.randint(1,9))
        return psudo_code
    #------------------------------------------------------------>
        
        
    if __name__ == '__main__':
        print(unique_code_gen())
        print(unique_otc_email_auth())

else:
    print('issue1: mysql connectivity error')
