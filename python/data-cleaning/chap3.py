import pandas as pd
import os

def get_file_dir(path):
    paths = (path if path != None else __file__).split(os.sep)
    _ = paths.pop()
    d = os.path.join(*paths)
    return f"/{d}"


def direct_filtering_func(df):
    id_col = df['id']

    id_index_1 = id_col[1]

    print(id_index_1)

    # Creating dataframe from df
    new_df = df[['artist', 'title']]

    print(new_df['artist'])

    # Accessing row range based
    # df[1:2] -> Returns the df with end index exclusif
    row = df[1:2]

    print(row)

    # Every row that match a given condition
    d_df = df[df['year'] > 1980]
    
    print(d_df)
    pass

def indexing_using_loc(df):

    # ROW=index|start:end|:|[i,j]
    # COL=index|start:end|:|[i,j]
    # df.loc[ROW, COL]
    print(df.loc[1, :])

    print(df.loc[[1,5], 'id':'artistId'])

def indexing_using_iloc(df):
    
    # iloc is like loc, but use the integer prosition instead of string characters
    # Note: Column index start at index 0
    df.iloc[1, :]
    pass


def filtering_using_str_contains(df):

    # Works on Series type
    # pandas.core.series.Series

    # serie.str.contains(<Pattern>, case=<Boolean>, regex=<Boolean>, na=<Boolean>_Should_Skip_Not_A_Number_Values)
    df.loc[df['medium'].str.contains('Graphics', case=False), ['artist', 'medium']]

    # Works only on string series/columns
    df.loc[df['year'].astype(str).str.contains('1826'), :]
    pass


if __name__ == '__main__':
    print(__file__)
    directory = get_file_dir(__file__)

    # pd.read_csv('path', encoding='latin-1|...', usecols=[<Columns>], header=<RowNumberOfHeaders>)
    # usecols=[] specify the list of columns to load from the file to read from
    df = pd.read_csv(os.path.join(directory, 'exercises', 'artwork_sample.csv'))

    # Setting the df index to a column of the df
    df.set_index('id', inplace=True)

    # Direct filtering
    direct_filtering_func(df)

    indexing_using_loc(df)

    indexing_using_iloc(df)