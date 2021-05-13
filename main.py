# import termcolored
import subprocess as sp
import uuid

from user import User
from Post import Post
from profile import Profile


if __name__ == '__main__': 
       
    sp.run('clear')
    print("_________Welcome to Khotan's Club_________")
    print(' ')
    print('1: Login')
    print('2: Register')
    print('3: Exit.')

    login_or_register = input('Please enter 1 to login, 2 to sign up, 3 to exit: ')

    if login_or_register == '1':
        username = input('Please enter username: ')
        password = input('Please enter password: ')

        is_logged_in, user_id = User.login(username, password)

        if is_logged_in == False:
            print("The given username or password is incorrect!")
        elif is_logged_in == True:

            while True:
                sp.run('clear')
                print(f"++++++++++++{username} logged in successfully++++++++++++")
                print(' ')
                print(' ')
                print('1: Posts')
                print('2: Friends')
                print('3: Profile')
                print('4: Post Something')
                print('5: Exit')
                print('6: List All Users')
                print('7: Sent A Request')
                print('8: write comment')
                print(' ')

                main_menu_option = input('Please choose one of the above options: ')

                if main_menu_option == '1':
                    sp.run('clear')
                    print('The posts are: ')
                    print('=' * 20)
                    Post.show_posts(just_show=True)

                # elif main_menu_option == '2' :
                #     User.show_friends()

                elif main_menu_option == '3':
                    print('1: See your own profile')
                    print('2: See others profile')

                    main_menu_option = input('Please choose one of the above options: ')

                    if main_menu_option == '1':
                        username = username
                        Profile.show_profile(username)

                        print('')
                        print('1: Edit your profile')
                        print('2: Exit')

                        main_menu_option = input('Please choose one of the above options: ')
                        if main_menu_option == '1':
                            Profile.edit_profile()

                        elif main_menu_option == '2':
                            break

                    elif main_menu_option == '2':
                        username = input('Please enter the username to which you want to visit the profile : ')
                        Profile.show_others_profile(username)

                        
                elif main_menu_option == '4':
                    post_string = input('Please enter your post content:   || ')
                    post_id = uuid.uuid4()
                    post_obj = Post(user_id,post_id, post_string)
                    post_obj.write_post_on_csv()
                
                elif main_menu_option == '5':
                    break
                
                elif main_menu_option == '6':
                    User.show_users()

                elif main_menu_option == '7':
                    User.send_request()
                elif main_menu_option == '8':
                    Post.write_comment()


    elif login_or_register == '2':
        username = input('Please enter username:')
        password = input('Please enter password:')
        password2 = input('Please enter password again: ')
        user_id = uuid.uuid4()

        if not(password == password2):
            print('The passwords are not the same.')
            exit()

        user = User(username, password)
        user.register()

    elif login_or_register == '3':
        exit()
    else:
        print('Error.')
