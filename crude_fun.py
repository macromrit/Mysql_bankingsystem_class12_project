#phase1 - func cust_inp
def cust_inp(content: str='', 
             d_type: str='s')->str or float or int:
    """customized input aisle

    Args:
        content (str, optional): the content that should be reflected to the user. Defaults to ''.
        d_type (str, optional): determining the data type of the value to be returned. Defaults to 's'.

    Returns:
        str or int or float: the values that should be appended to the db
    """
    
    if d_type=='s':#its a str
        while True:
            try:
                main_val = str(input(content)).strip()
                #####
                break
            except: print('Oops :( something went wrong.. Try again!!')
    
    elif d_type=='f':#its a float
        while True:
            try:
                main_val = float(input(content))
                #####
                break
            except: print('Oops :( something went wrong.. Try again!!')
                
    elif d_type=='i':
        while True:
            try:
                main_val = int(input(content))
                #####
                break
            except: print('Oops :( something went wrong.. Try again!!')
    
    else: main_val = -1
    
    return main_val
              
#------------------------------------------------------------------------------------------------------------------------->                
#phase2 - func ref_all                
def ref_all(mode: str='w', 
            *vals) -> str:
    """To return a reciept

    Args:
        mode (str, optional): to detect the mode of process done by the user. Defaults to 'w'.
        vals: necessary details of the user to be reflected

    Returns:
        str: Reciept
    """
    
    if mode=='w':#if the mode is to withdraw funds
        reciept = F'''
-------------------------------------        
Withdawal Reciept        
-------------------------------------        
User's Name:        {vals[0]}
User's bank id:     {vals[1]}
Amount withdrawn:   ${vals[2]}
Withdrawal Time:    {vals[4]}
User's balance:     ${vals[3]}
-------------------------------------
        '''
    elif mode=='d':#if the mode is to deposit funds
        reciept = F'''
-------------------------------------        
Deposital Reciept        
-------------------------------------        
User's Name:        {vals[0]}
User's bank id:     {vals[1]}
Amount deposited:   ${vals[2]}
Deposital Time:     {vals[4]}
User's balance:     ${vals[3]}
-------------------------------------
        '''
        
    elif mode=='t':#if the mode is to transfer funds
        reciept = F'''
--------------------------------------
Tranfer Reciept         
--------------------------------------        
Sender's Name:      {vals[0]}
Sender's bank id:   {vals[1]}
Amount transferred: ${vals[2]}
<><><><><><><><><><><><><><><><><><><>
Transferred Time:   {vals[6]}
<><><><><><><><><><><><><><><><><><><>
reciever's Name:    {vals[3]}
reciever's bank id: {vals[4]}
Amount recieved:    ${vals[5]}
--------------------------------------
        '''
    
    elif mode=='b':#if the mode is to display balance and account details
        reciept = F'''
-------------------------------------        
Account details
-------------------------------------
User's Name:            {vals[0]}
User's bank id:         {vals[1]}
User's balance:         ${vals[2]}
Account was created on: {vals[3]}
-------------------------------------
        '''
    
    else: 
        reciept = -1
    
    return reciept

#------------------------------------------------------------------------------------------------------------------------->
#phase3-> func to print empty lines for prettyfying the output
def void_sep(iter: int=1):
    for _ in range(iter):
        print()


#------------------------------------------------------------------------------------------------------------------------->
def func_sep():
    print('+'*80)
    print('+'*80)

#------------------------------------------------------------------------------------------------------------------------->
if __name__ == '__main__': pass
