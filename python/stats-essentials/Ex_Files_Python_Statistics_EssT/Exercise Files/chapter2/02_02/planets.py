import pandas as pd
import os

def get_file_dir(path):
    paths = (path if path != None else __file__).split(os.sep)
    _ = paths.pop()
    d = os.path.join(*paths)
    return f"/{d}"

if __name__ == '__main__':
    directory = get_file_dir(__file__)

    # pd.read_csv('path', encoding='latin-1|...')
    df = pd.read_csv(os.path.join(directory, 'Planets-Cleaned.csv'))

    # Accessing columns in a data frame using Array indexes
    print(df['Mass'])

    # Accessing columns using OOP
    print(df.Mass)

    # Modify the index column name
    # Most of df method requires inplace to modify the df instead of creating a copy
    df.set_index('Planet', inplace=True)

    # Accessing the indexes
    print(df.index)

    # Checking the number of rows in the df
    print(df.info)

    # Get a dataframe colum
    print('Loaded Venus colums data: ')
    print(df.loc['VENUS'])
    
    # Number of rows in the df is the len of the df
    length = len(df)

    print(length)

    # List the columns in the data frame
    print(df.columns)

    # Get a column of a row in the df
    print(df.loc['MERCURY'].FirstVisited)

    # String to datetime object
    # Assigning value to a matching column
    df['FirstVisited'] = pd.to_datetime(df['FirstVisited'])

    print(df)

    # Now the datetime column can be access as python datetime
    print(df.loc['MERCURY']['FirstVisited'].year)