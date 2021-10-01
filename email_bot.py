import smtplib #->simple mail transfer protocol lib
from email.message import EmailMessage
from unique_code_gen import unique_otc_email_auth

from matplotlib.pyplot import title
import yagmail

def post_email(reciever: str, 
               subject: str,
               content: str):
    email_sent = False
    try:
        history = EmailMessage()
        history['Subject'] = subject
        history['From'] = 'Dopethon Finances'
        history['To'] = reciever
        history.set_content(content)
        
#Connecting to server
#------------------------------------------------------------------------------------------------------------------------->
        maccy_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        maccy_server.login('amritsubramanian.c@gmail.com', 'amma@@1953')#connection established
        maccy_server.send_message(history)
        maccy_server.quit()
        email_sent = True
    except:
        pass
    return email_sent

def acc_post_email(reciever_email: str, 
                   usdid: str): 
    right_from = 'amritsubramanian.c@gmail.com'
    act_receiver = reciever_email
    titly = 'Dopethon Finances - Your Transactional History with our bank'
    filename = F'user_transactions/{usdid}.csv'
    
    mrit = yagmail.SMTP(right_from, 'amma@@1953')
    mrit.send(
        to=act_receiver,
        subject=titly,
        contents='Your transactional history upto now has been written to the csv file pinged down:',
        attachments=filename
    )
    
def email_verification(receiver_email)->str: 
    email_sent = False
    try:
        history = EmailMessage()
        history['Subject'] = 'This is your one time verification code'
        history['From'] = 'Dopethon Finances'
        history['To'] = receiver_email
        otc = unique_otc_email_auth()
        history.set_content(F'Your otp -> {otc}')
        
#Connecting to server
#------------------------------------------------------------------------------------------------------------------------->
        maccy_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        maccy_server.login('amritsubramanian.c@gmail.com', 'amma@@1953')#connection established
        maccy_server.send_message(history)
        maccy_server.quit()
        email_sent = True
    except:
        pass
    return email_sent, otc

if __name__ == '__main__': pass
