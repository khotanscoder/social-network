from datetime import datetime
import csv
import time

class Post:

    def __init__(self, user_id, post_id, body, comments=[]):
        """
        :param  post_id: index of post
        :param body: body of post
        :param comments_number: quantity of post's comments
        """
        self.user_id = user_id
        self.post_id = post_id
        self.body = body
        self.comments = comments
        self.created_on = datetime.now()

    def write_post_on_csv(self):
        post_file_path = "posts.csv"
        dict_of_post = {
            "user_id" : self.user_id,
            "post_id" : self.post_id,
            "post" : self.body,
            "comments" : self.comments,
            "created_on" : self.created_on
       }
        with open(post_file_path, 'a+') as posts:
            reader = csv.reader(posts)
            fieldnames = 'user_id,post_id,post,comments,created_on'.split(',')
            csv_writer = csv.DictWriter(posts, fieldnames=fieldnames,)
            csv_writer.writerow(dict_of_post)

            print('Your post is created.')
            time.sleep(3)

    @staticmethod
    def show_posts():
        post_file_path = "posts.csv"

        with open(post_file_path, 'r') as posts:
            reader = csv.reader(posts)

            counter = 0
            for index, p in enumerate(reader):
                if not(len(p) == 0 or index == 0):
                    counter += 1
                    print(f"Post {counter}:")
                    print(p[2])
                    print('-' * 10)
                    time.sleep(5)
                    
    
