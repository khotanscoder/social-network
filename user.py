import subprocess as sp
import csv
from csv import DictReader, DictWriter
import time
import pandas as pd
import hashlib

from profile import Profile
import uuid



class User():
   
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.friends = []
        self.sent_requests = []
        self.received_requests = []
    
    def register(self):
        """
            This function register an account and create a uniqe profile for user 
            and save user's informations in "accounts.csv" file;
        """
        file_path = "accounts.csv"
        df_account = pd.read_csv(file_path)
        lst_username = list(df_account['username'])

        if not(self.username in lst_username):
            print('valid username')
            # user_profile = Profile(self.username)


        # hashing the password
        hash_password = hashlib.sha256(self.password.encode("utf8")).hexdigest()

        # row_account = [[obj_user.username,obj_user.password]]
        with open(file_path,'a+',newline='') as csv_account:
            fieldnames = "user_id,username,password,friends,sent_requests,received_requests".split(',')
            csv_writer = csv.DictWriter(csv_account, fieldnames=fieldnames)
            csv_writer.writerow({
                    'user_id' : uuid.uuid4(),
                    'username': self.username,
                    'password': hash_password,
                    'friends' : self.friends,
                    'received_requests' : self.received_requests,
                    'sent_requests' : self.sent_requests,
                })


    @staticmethod
    def login(username, password):
        
        hash_password = hashlib.sha256(password.encode("utf8")).hexdigest()
        with open('accounts.csv', 'r') as file_users:
            reader = csv.reader(file_users)

            for row in reader:
                if not(len(row) == 0):
                    if row[1] == username and row[2] == hash_password:
                        user_id = row[0]
                        return (True, user_id)
                else:
                    continue

        return False

    @staticmethod
    def show_users():
        
        """
            This function enumerate the users of khotan's club;
        """
        sp.run('clear')
        file_path = 'accounts.csv'

        print(' ')
        print('********The list of all users********')

        with open(file_path, 'r') as users:
            reader = csv.reader(users)

            counter = 0
            for index, u in enumerate(reader):
                counter += 1
                if not(len(u) == 0 or index == 0):
                    print(f"User {counter}->  {u[1]}")
            time.sleep(5)

    @staticmethod
    def show_friends():
        pass

    @staticmethod
    def show_requests():
        pass

    @staticmethod
    def send_request():
        sp.run('clear')
        to_whom_username = input('Please enter the username to which you want to send the request: ')
        pending_requests = []    
        file_path = 'accounts.csv'
        
        df = pd.read_csv(file_path)
        print(str(df['sent_requests'][df["username"] == to_whom_username]))
        print(type(df['sent_requests'][df["username"] == to_whom_username]))

        from utils import update_csv

# User.send_request()




    # @classmethod
    # def follow_users(self):
    #     pass

    # def get_post(self, post_id):
    #     """
    #         this function get sent post from user and write on profile.txt file 
    #     """
    #     pass

    # def remove_post(self, post_id):
    #     """
    #         This function delete post
    #     """
    #     pass

    # def edit_post(self, post_id):
    #     """
    #         This functhion edit bio of post
    #     """
    #     pass
        
