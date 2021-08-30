import smtplib #->simple mail transfer protocol lib
from email.message import EmailMessage

def post_email(reciever: str, 
               subject: str,
               content: str):
    email_sent = False
    try:
        history = EmailMessage()
        history['Subject'] = subject
        history['From'] = 'Dopethon Financers'
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
