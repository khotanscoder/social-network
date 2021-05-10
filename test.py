import pandas as pd



def update_csv(username):
        file_path = 'accounts.csv'

        df = pd.read_csv(file_path)

        # df[df['username'] == username]

        df_updated = df.replace(to_replace =username, value= '/'.join(['re', 'za']))
        
        # import os
        # os.remove(file_path)
        df_updated.to_csv(file_path, index=False)



username = 'zahra'

update_csv(username)

