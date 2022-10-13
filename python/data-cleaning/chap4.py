import pandas as pd
import os
from numpy import nan

def get_file_dir(path):
    paths = (path if path != None else __file__).split(os.sep)
    _ = paths.pop()
    d = os.path.join(*paths)
    return f"/{d}"


def stripping_white_space_func(df):

    # Find rows with tile having whitespace at the end
    # rstrip() | lstrip() | strip()
    result = df['title'].str.contains('\n$', regex=True)

    print(result)

    # Remove the whitespace at the end of the strings
    df['title'].str.strip(inplace=True)
    # or
    df['title'] = df['title,'].str.strip()

    print(df)
    pass

def dropping_row_of_data(df):

    # Drop rows in the dataset when any/all columns have NaN as value
    # df.dropna(how='all|any', tresh=TRESH_VALUE, subset=[<Columns>])
    # use subset to match only specific columns
    df.dropna()
    pass

def identifying_dropping_duplicates(df):
    # df.dropna(subset=[<Columns>], keep=first|last|False)
    # use subset to match only specific columns
    # keep: to keep the first, last or no column
    df.drop_duplicates()

    # Finding duplicated columns
    df.loc[df.duplicated(subset=['artist', 'title'], keep=False)]
    pass

def replacing_bad_data_func(df):

    # Check if the column dateText of all rows contains
    # This function takes a scalar or array-like object and indicates
    # whether values are missing (``NaN`` in numeric arrays, ``None`` or ``NaN``
    # in object arrays, ``NaT`` in datetimelike).
    _ = pd.isna(df.loc[:, 'dateText'])

    # Set/Replace dateText column values to NaN if they match date not known
    df.replace({ 'dateText': {"date not known" : nan}}, inplace=True)
    # Or
    df.loc[df['dateText'] == 'date not known', ['dateText']] = nan

    # Another example
    df.loc[df['year'].notnull() & df['year'].astype(str).contains('[^0-9]', regex=True), ['year']] = nan
    pass

def filling_missing_data_func(df):

    # Fill nan value column with the defined value
    # df.fillna(0) -> Replace all nan in all column with 0
    # df.fillna(value={<Column>: <Value>, <Colum2>: <Value2>}) -> Target specific columns
    df.fillna(value={'depth': 0}, inplace=True)
    pass


if __name__ == '__main__':
    print(__file__)
    directory = get_file_dir(__file__)

    # pd.read_csv('path', encoding='latin-1|...', usecols=[<Columns>], header=<RowNumberOfHeaders>)
    # usecols=[] specify the list of columns to load from the file to read from
    df = pd.read_csv(os.path.join(directory, 'exercises', 'artwork_data.csv'), low_memory=False)

    # Stripping white space data
    stripping_white_space_func(df)

    # Replacing missing or bad data
    replacing_bad_data_func(df)

    # Droping na column row
    dropping_row_of_data(df)
