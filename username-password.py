 ## create a dictionary to store the credentials
credstore = {                
  "ck" : "mic145", 
  "alexa" : "siri",
  "echo" : "dot"
  }
## initializong variables

username = "" ## initialize the username
password = ""  ## initialize the password
n = 0 ## counter initializition 
max_attempt = 6

while n < max_attempt: 
    n +=1
    username = input('Enter your username: ') # prompt the user to enter his credentials 
    password = input('Enter your password: ')

    if username in credstore and credstore[username] == password:
            print("\n your credentials are correct you have access to you account") # the condition have been validated                                                              
            break 
    elif username not in credstore or password[username] != password:
            
            if n != max_attempt:
                  print('\nPlease Try Again your credential are not correct')  # The user will be ask to try again for a max of 5 times, until he get his credentials right
       
            else:
                  print("\n I am sorry your account has been locked due to multiples login attempt please contact your administartor or try again after 24 hours") # After 5 unsuccessfull logon attempt the user account will be locked for security reason.
                  break
    else: 
             break