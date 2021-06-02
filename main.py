import subprocess as sp
import uuid

from pandas.core.construction import create_series_with_explicit_dtype

from User import User
from Post import Post
from logger import log

if __name__ == '__main__':

    sp.run('clear')
    print("_________Welcome to Khotan's Club_________")
    print(' ')
    print('1: Login')
    print('2: Register')
    print('3: Exit.')

    login_or_register = input(
        'Please enter 1 to login, 2 to sign up, 3 to exit: ')

    if login_or_register == '1':
        username = input('Please enter username: ')
        password = input('Please enter password: ')

        is_logged_in, user = User.login(username, password)

        if is_logged_in == False:
            print("The given username or password is incorrect!")           

        elif is_logged_in == True:
            log("logged_in", user)
            while True:
                sp.run('clear')
                print(
                    f"++++++++++++{username} logged in successfully++++++++++++")
                print(' ')
                print(' ')
                print('1: Posts')
                print('2: Friends')
                print('3: Profile')
                print('4: Post Something')
                print('5: List All Users')
                print('6: write comment')
                print('7: Follow someone')
                print('x: Exit')
                print(' ')

                main_menu_option = input(
                    'Please choose one of the above options: ')

                if main_menu_option == '1':
                    log("posts", user)
                    sp.run('clear')
                    print('The posts are: ')
                    print('=' * 20)
                    Post.show_posts(just_show=True)

                elif main_menu_option == '2':
                    log("friends", user)
                    for followee_username in user.get_user_followings():
                        print(followee_username)
                    input('Please enter  to go back to the main menu. ')

                elif main_menu_option == '3':
                    log("profile", user)
                    sp.run('clear')
                    print('1: Show your profile')
                    print('2: Edit your profile')
                    print("3: Show others' profile")
                    print(' ')
                    edit_or_show = input(
                        'Please enter one of the options above: ')

                    if edit_or_show == '1':
                        log("show_profile", user)
                        User.show_profile(username)

                    elif edit_or_show == '2':
                        log("edit_profile", user)
                        tmp_phone_number = input("plese insert new phone_number, enter for skip: ")
                        tmp_email = input("plese insert new email, enter for skip: ")
                        tmp_bio = input("plese insert new bio, enter for skip: ")
                        
                        updated_phone_number = tmp_phone_number if tmp_phone_number != "" else user.phone_number
                        updated_email = tmp_email if tmp_email != "" else user.email
                        updated_bio = tmp_bio if tmp_bio != "" else user.bio

                        user.update_profile_info(phone_number=updated_phone_number, email=updated_email, bio=updated_bio)
                        

                    elif edit_or_show == '3':
                        log("show_all_profiles", user)
                        User.show_others_profile(username)
                    
                    input('Please enter  to go back to the main menu. ')

                elif main_menu_option == '4':
                    log("post something", user)
                    post_string = input(
                        'Please enter your post content:   || ')
                    post_id = uuid.uuid4()
                    post_obj = Post(user_id, post_id, post_string)
                    post_obj.write_post_on_csv()

                elif main_menu_option == '5':
                    log("list all users", user)
                    User.show_users()
                    input('Please enter  to go back to the main menu. ')

                elif main_menu_option == '6':
                    log("write comment", user)
                    Post.write_comment()

                elif main_menu_option == '7':
                    log("follow someone", user)
                    User.show_users()
                    to_follow_user = input(
                        "Please enter name of the user you want to follow: ")
                    user.follow_user(to_follow_user)
                    input('Please enter  to go back to the main menu. ')

                elif main_menu_option == 'x':

                    break

    elif login_or_register == '2':
        username = input('Please enter username:')
        password = input('Please enter password:')
        password2 = input('Please enter password again: ')

        if not(password == password2):
            print('The passwords are not the same.')
            exit()

        user = User(username=username, password=password)
        user.register()
        log("registered", user)

    elif login_or_register == '3':
        exit()
    else:
        print('Error.')
