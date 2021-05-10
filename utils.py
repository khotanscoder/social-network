def update_csv(file_path, value_to_update, updated_value):
        import pandas as pd

        df = pd.read_csv(file_path)

        # df[df['username'] == username]

        df_updated = df.replace(to_replace =value_to_update, value = updated_value)
        
        import os
        os.remove(file_path)
        df_updated.to_csv(file_path, index=False)