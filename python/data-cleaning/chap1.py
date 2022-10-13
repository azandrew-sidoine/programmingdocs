import pandas as pd
import os

def get_file_dir(path):
    paths = (path if path != None else __file__).split(os.sep)
    _ = paths.pop()
    d = os.path.join(*paths)
    return f"/{d}"


# Data Agregation
def agg_func(df):

    min_y = df['year'].min() # Minimum value of the column

    max_y = df['year'].max() # Maximum

    mean_y = df['year'].mean() # Mean / Moyenne

    std_y = df['year'].std() # Standard deviation / Ecart type

    print('Min: {}, Max: {}, Mean: {}, Std: {} '.format(min_y, max_y, mean_y, std_y))

    df.agg(['min', 'max', 'std']) # Call aggreagtion function for every colum of the df


def normalize_func(df):
    # Normalization must be run only on numeric data of the data frame
    # Adjust the value in a column  and change their scale

    # Stardazation
    norm = (df['height'] - df['height'].mean()) / df['height'].std()
    print(norm)
    df['standardized_height'] = norm

    # Normalize to value between 0 - 1
    df['normal_height'] = (df['height'] - df['height'].min()) / ( df['height'].max() - df['height'].min())

    print(df)

def transform_func(df):
    # Transform is like a functionnal pattern method defined on data frame
    # to apply data transformation like map() on column data
    df['height'].transform(lambda x: x / 10)

    print(df.head())

    # Group the data by a column and apply transform to remove duplicates
    print(df.groupby('artist').transform('nunique'))

    # Assigning transformation to a column
    df['height_mean_grouped_by_artist'] = df.groupby('artist')['height'].transform('mean')

    print(df)
    pass

def filter_func(df):

    # Filter a data frame to load only some columns
    # Note: like param take a case sensitive column name matching
    # 
    #df.filter(items=[Col1, Col2, .... Coln], like=<Str>, regex=<RegularExpression>, axis=0|1)
    filtered_df = df.filter(items=['id', 'artist'])

    print(filtered_df)

    artist_colum_df = df.filter(like='artist')

    print(artist_colum_df)
    pass



if __name__ == '__main__':
    print(__file__)
    directory = get_file_dir(__file__)

    # pd.read_csv('path', encoding='latin-1|...')
    df = pd.read_csv(os.path.join(directory, 'exercises', 'artwork_sample.csv'))

    # Print the head of the data frame
    print(df.head)

    # Return the type of each column in the data frame
    print(df.dtypes)

    df['acquisitionYear'] = df['acquisitionYear'].astype(float)

    print(df['acquisitionYear'].head())

    # Coverting a column to a numeric/floating point type with error coercion
    pd.to_numeric(df['height'], errors='coerce')

    # Running aggreagation
    agg_func(df)

    # Data normalization
    normalize_func(df)

    # Data transformation
    transform_func(df)

    # Data filtering
    filter_func(df)