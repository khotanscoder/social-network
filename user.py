import subprocess as sp
import csv
from csv import DictReader, DictWriter
import hashlib
import uuid

from profile import Profile


class User():
    user_csv_path = "accounts.csv"
    user_csv_columns = ["user_id", "username",
                        "password", "phone_number", "email", "bio"]
    following_csv_path = "following.csv"

    def __init__(self, username, password=None, user_id=None, phone_number=None, email=None, bio=None):
        """
        :param username: username
        :param password: password
        :param friends: the list of friends
        :param
        """
        self.user_id = user_id
        self.username = username
        self.password = password
        self.phone_number = phone_number
        self.email = email
        self.bio = bio

    def update_profile_info(self, phone_number=None, email=None, bio=None):
        self.phone_number = phone_number
        self.email = email
        self.bio = bio

        self.update()

    def update(self):
        self._update_row({
            "user_id": self.user_id,
            "username": self.username,
            "password": self.password,
            "phone_number": self.phone_number,
            "email": self.email,
            "bio": self.bio
        })

    @classmethod
    def _update_row(cls, user_obj):
        user_id = user_obj["user_id"] if "user_id" in user_obj else None
        username = user_obj["username"] if "username" in user_obj else None
        cls._remove_row(user_id=user_id, username=username)
        cls._add_row(user_obj)

    @classmethod
    def _add_row(cls, user_obj):
        user_row = {}
        for col in cls.user_csv_columns:
            user_row[col] = user_obj[col] if col in user_obj else ""

        with open(cls.user_csv_path, 'a+') as users_csv:
            csv_writer = csv.DictWriter(
                users_csv, fieldnames=cls.user_csv_columns)
            csv_writer.writerow(user_row)

    @classmethod
    def _remove_row(cls, user_id=None, username=None):
        lines = []
        with open(cls.user_csv_path, 'r') as users_file:
            users = csv.reader(users_file)
            for user in users:
                if user[0] == user_id or user[1] == username:
                    continue
                lines.append(user)

        with open(cls.user_csv_path, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

    def register(self):
        """
            This function register an account and create a uniqe profile for user
            and save user's informations in "accounts.csv" file;
        """
        if self.username == "username":
            print("Username is not valid")
            return

        if self._find_user(username=self.username) is not None:
            print('duplicated username')
            return

        # hashing the password
        hash_password = hashlib.sha256(
            self.password.encode("utf8")).hexdigest()

        user_id = uuid.uuid4()
        self._add_row({
            'user_id': user_id,
            'username': self.username,
            'password': hash_password
        })
        self.user_id = user_id
        self.password = hash_password

    @classmethod
    def _find_user(cls, user_id=None, username=None):
        with open(cls.user_csv_path, 'r') as users_file:
            users = csv.reader(users_file)
            for user in users:
                if len(user) > 0:
                    if user[0] == user_id or user[1] == username:
                        return User(
                            user_id=user[0],
                            username=user[1],
                            # it exposes password to higher level function which may cause some security issues
                            password=user[2],
                            phone_number=user[3],
                            email=user[4],
                            bio=user[5],
                        )
        return None

    def get_user_followings(self):
        followings = {}
        with open(self.following_csv_path, 'r') as followings_file:
            followings_list = csv.reader(followings_file)
            for following in followings_list:
                if following[0] == self.user_id:
                    followee = self._find_user(username=following[1])
                    followings[followee.username] = followee

        return followings

    @classmethod
    def get_all_users(cls):
        users = {}
        with open(cls.user_csv_path, 'r') as users_file:
            users_list = csv.reader(users_file)
            for user in users_list:
                user_obj = cls._find_user(username=user[1])
                if user_obj is None or user_obj.username == "username":
                    continue
                users[user_obj.username] = user_obj
        return users

    def _follow_user(self, followee):
        with open(self.following_csv_path, 'a+') as csv_file:
            csv_writer = csv.DictWriter(
                csv_file, fieldnames=["follower_id", "followee_id"])
            csv_writer.writerow({
                "follower_id": self.user_id,
                "followee_id": followee.user_id,
            })

    @ classmethod
    def login(cls, username, password):
        user = cls._find_user(username=username)
        hash_password = hashlib.sha256(password.encode("utf8")).hexdigest()
        if user is not None and user.password == hash_password:
            return True, user

        return False, None

    @ classmethod
    def show_users(cls):
        """
            This function enumerate the users of khotan's club;
        """
        sp.run('clear')
        print(' ')
        print('********The list of all users********')

        all_users = cls.get_all_users()
        for username in all_users.keys():
            print(f"* {username}")

    def follow_user(self, to_follow_username):
        followee = self._find_user(username=to_follow_username)
        if followee is None:
            print("the entered username is not found!")
            return

        if followee.username == self.username:
            print("You can not follow yourself")
            return

        user_followings = self.get_user_followings()
        if followee.username in user_followings:
            print(f"You've already followed this account: {followee.username}")
            return

        self._follow_user(followee)
        print(f"User {followee.username} followed succesfuly!")

    @classmethod
    def show_profile(cls, username):
        user = cls._find_user(username=username)
        print(f"Your username: {username}")

        if len(user.phone_number) == 0:
            print(f"Your phone number: NOT-SET")
        else:
            print(f"Your phone number: {user.phone_number}")

        if len(user.email) == 0:
            print(f"Your email: NOT-SET")
        else:
            print(f"Your email: {user.email}")

        if len(user.bio) == 0:
            print(f"Your bio: NOT-SET")
        else:
            print(f"Your bio: {user.bio}")

    @classmethod
    def show_others_profile(cls, username):
        all_users = cls.get_all_users()
        for username in all_users.keys():
            print(f"* {username}")
        username = input(
            'enter the username whome you want to visit his/her profile from above list : ')
        cls.show_profile(username)
