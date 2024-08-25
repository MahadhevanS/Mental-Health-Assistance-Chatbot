import csv
import os
"""
    Maitains users login informations, 
    User Authentication and 
    Regiteration of new Users.
"""
# Initialize UserLog
UserLog = {}

def load_data():
    """ Load existing user data from a file (if it exists)"""
    global UserLog
    if os.path.exists('ChatterBot\\user_log.csv'):
        with open('user_log.csv', 'r') as f:
            reader = csv.reader(f)
            UserLog = {i[0] : i[1] for i in reader}

def save_data():
    """ Save user data to a file"""
    with open('user_log.csv', 'w',newline='') as f:
        writer = csv.writer(f)
        for username,password in UserLog.items():
            writer.writerow([username,password])

def update_user(Username, password):
    """ Update UserLog with a new username and password"""
    global UserLog
    UserLog[Username] = password
    save_data()

def check_user(Username, password):
    """ Check if the username and password are correct"""
    global UserLog
    if Username in UserLog and UserLog[Username] == password:
        return True
    else:
        print('You are registered as a new user!')
        return False
