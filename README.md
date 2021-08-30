Title: 
    Dopethon Finances

Programming Language: 
    Python v3.9.7

Database: 
    Mysql (Community Version)

GitHub Repository: 
    https://github.com/macromrit/Mysql_bankingsystem_class12_project

Develper's Community:
    ->S.Surya
    ->M.Adethya
    ->C.R.M.S.Amrit Subramanian

Purpose: 
    Class 12 Cs Project

Description:
    A Bank alike Software.. Which infact is capable of transferring, receiving, depositing and withdrawing funds. To add-on with.. This beauty got the ability to mail users about fund-transactions transpiring via the user's account. That isn't all... Super-User access is the killer-bite of the whole segment, which basically approves an admin validated user to access crude data and display confidential info's of an user as per the super-user's wish.

Medium of transactions:
    -> '$' a.k.a USD [United States Dollar]

Libraries and modules used:
    matplotlib -> install it via pip.
    datetime -> to display the time [pre-installed].
    time -> to let program sleep for a sec or two [pre-installed].
    mysql -> install it via pip. used to integrate python with mysql db.
    smtplib -> used to handle email via python [pre-installed] [fullform: simple-mail-transfer-protocol-library].
    random -> to generate unique id [pre-installed].
    email -> to make the email server linkage primitive [pre-installed].


Set of Mysql commands to be executed before running the program:
    ->  Command I:
        CREATE DATABASE banking_system;

    ->  Command II:
        USE banking_system;

    ->  Command III:
        CREATE TABLE IF not exists account_holders(
        name varchar(120), 
        gender char(1),
        age int, 
        nationality varchar(100), 
        unique_id char(10), 
        phone_no varchar(20),
        email varchar(80),
        date_created varchar(252),
        balance FLOAT, 
        password varchar(108),
        primary key(unique_id));
    
    ->  Command IV:
        CREATE TABLE IF NOT EXISTS history(
        user_id char(10), 
        mode varchar(100), 
        amount float, 
        rec_user_id char(10));
       

Files:
    ->main.py:
        The grand-dad of all files.. this is the peculiar and ultimate destination where the files existing would colloborate togther to make the whole system of process work like charm.

    ->crude_fun.py:
        A typical module portraying file.. Got all the fundamental functions to pretty the output and intimate user about what's going on.

    ->database.py:
        Horizon where most of the data-related functions reside.. Its a typical module-portraying file.. way similiar to the prior. It consists of stuffs related to transactions i.e: bunchies like withdrawal, deposital and thingys that sort, come under this genre.

    ->email_bot.py:
        Gotta employ somebody to dust off chores.. And that's where email_bot comes under action. This kuddo send's email to the users by establishing smtp server in the most efficient way out there. Might consume some time. But worth the span.

    ->super_user.py:
        The ultimate bucket list which comprises a mapping eventually making that mapping store super-user name and their passkey to get the super-user access.

    ->unique_code_gen.py:
        Generating stuffs are pretty simple.. But human effort kills worthy span. unique_code_gen makes it sweet by manufacturing an unique id for a user which inturn is contrasted with the id's available from the database. Atlast if stuffs work right an unique id is generated.


functions created:
    ->crude_fun.py:
        -> cust_inp : to receive input from the user in the best way possible.
        -> ref_all  : to reflect data reciept depending on the transactions made.
        -> void_sep : to leave blank lines while running the program.
        -> func_sep : to seperate functionalites done by the user while running the program.
    
    ->database.py:
        -> create_user      : to create a user in the bank account.
        -> authenticate_user: to let a user log-in and make transactions.
        -> withdraw_funds   : to withdraw funds from the user's account.    [Log-in required]
        -> deposit_funds    : to deposit funds to the user's account.       [Log-in required]
        -> transfer_funds   : to transfer funds from one user to another.   [Log-in required]
        -> delete_user      : to delete user from the bank db.              [Log-in required]
        -> display_balance  : to display user's account info.               [Log-in required]
        -> super_user_access: to give the user super-user approval.         [super-user-Log-in required]
    
    ->email_bot.py:
        -> post_email: to mail users about the transactions thay make.
    
    ->unique_code_gen:
        -> unique_code_gen: to generate unique user id for new users.
    
    ->super_user.py:
        -> super_user: a map containing a bucket list of super users username and passkey to let them log-in.


Contact Us @:
    -> C.R.M.S.Amrit Subramanian:
        -> Ph.no    : 90037 24367
        -> Email    : amritsubramanian.c@gmail.com
        -> Instagram: amritsubramanian.c
        -> GitHub   : macromrit
    
    -> S.Surya: 
        -> Ph.no    : 80159 60773
        -> Email    : surya090404@gmail.com
        -> GitHub   : surya0904shankar
    
    -> M.Adethya:
        -> Ph.no    : 63807 57829
        -> Email    : surya090404@gmail.com
        -> GitHub   : Ade-Mur

