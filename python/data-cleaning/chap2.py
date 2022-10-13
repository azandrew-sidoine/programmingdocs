import pandas as pd
import os

def get_file_dir(path):
    paths = (path if path != None else __file__).split(os.sep)
    _ = paths.pop()
    d = os.path.join(*paths)
    return f"/{d}"
    

def dropping_columns(df):

    # Dropping row by specifying index
    # Dropping works on rows by default
    n_df = df.drop(0) # Drop the first row

    n_df = df.drop(label=[0,1,2]) # Drop a list of the rows

    n_df = df.drop('id', axis=1) # Drop the column id axis=1 specify the operation to be performed on columns

    n_df = df.drop(columns=['id']) # Dropping a list of columns at once

    # Note: All pandas / most pandas methods are immutable
    # In order to modify the data frame, use inplace=True
    df.drop(columns=['id'], inplace=True)

    print(n_df)
    pass

def change_col_case_func(df):

    df.columns.str.lower() # Convert all column names to lower case

    # Using list comprehension
    df.columns = [c.lower() for c in df.columns]

    print(df.columns)

    # Using map
    df.columns = map[lambda c: c.lower(), df.columns]

    # Note we can perform more robust case operations

def renaming_columns(df):

    # Renaming columns using the columns key
    df.rename(columns={"old_column_name": "new_column_name"})

    # Renaming column using the axis keyword
    df.rename({"old_column_name": "new_column_name"}, axis=1, inplace=True)

    # Using lambda function
    df.columns = df.rename(columns=lambda c: c.lower(), inplace=True)

    pass
if __name__ == '__main__':
    print(__file__)
    directory = get_file_dir(__file__)

    # pd.read_csv('path', encoding='latin-1|...', usecols=[<Columns>], header=<RowNumberOfHeaders>)
    # usecols=[] specify the list of columns to load from the file to read from
    df = pd.read_csv(os.path.join(directory, 'exercises', 'artwork_sample.csv'), )

    # Dropping data frame columns
    dropping_columns(df)

    # Changing data frame column case
    change_col_case_func(df)

    # Renaming data frame columns
    renaming_columns(df)