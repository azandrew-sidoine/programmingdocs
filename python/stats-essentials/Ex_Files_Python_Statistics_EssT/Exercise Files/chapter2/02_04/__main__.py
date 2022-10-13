import os
import pandas as pd
import matplotlib.pyplot as plt

def get_file_dir(path):
    paths = (path if path != None else __file__).split(os.sep)
    _ = paths.pop()
    d = os.path.join(*paths)
    return f"/{d}"


if __name__ == '__main__':

    df = pd.read_csv(os.path.join(get_file_dir(__file__), 'billboard.csv'))

    # Get the First less than 10 rows of the data frame
    h = df.head
    print(h)

    # Iterating over rows

    for index, row in df.iterrows():
        plt.plot(range(1, 77), row['x1st.week':'x76th.week'], color='C0', alpha=0.1)

    plt.show()

    # Select only some columns of the dataframe
    dfshort = df[['artist.inverted', 'track', 'time', 'date.entered', 'x1st.week', 'x2nd.week', 'x3rd.week']]

    print(dfshort.head())

    # Reassign the selected column
    dfshort.columns = ['artist', 'track', 'time', 'date_entered', 'wk1', 'wk2', 'wk3']

    print('\n----- SHORT DATA FRAME ------\n')
    print(dfshort.head())

    # Melt the dataframe columns
    # df.melt(<Identifier_Variables_Repeated_For_Several_Rows>, <Observation_Columns>, <Observabtion_Type_Column_Name>, <Observabtion_Value_Column_Name>)
    dfmelt = dfshort.melt(['artist', 'track', 'time', 'date_entered'], ['wk1', 'wk2', 'wk3'], 'week', 'rank')

    # Querying a column
    # Query use natural processing language syntax
    result = dfmelt.query('track == "Liar"')
    print('\n----- QUERY RESULT ------\n')
    print(result)

    # Coverting column using apply
    # The Lambda simply get the 3rd characted of the week column entries and convert it to string
    dfmelt['week'] = dfmelt['week'].apply(lambda x : int(x[2]))

    dfmelt['date_entered'] = dfmelt['date_entered'].apply(lambda x : pd.to_datetime(x))

    print('\n----- MELTED DATA FRAME ------\n')
    print(dfmelt)

    # Performing arithmetic between two dates
    dfmelt['date'] = dfmelt['date_entered'] + pd.Timedelta('7 days') * (dfmelt['week'] - 1)

    print(dfmelt.head())

    # Dropping a column
    dfmelt.drop(['date_entered'], axis=1)

    # Sorting values of a column
    dfinal = dfmelt[['artist', 'track', 'time', 'date', 'week', 'rank']].sort_values(['artist', 'track'])

    print('\n----- FINAL DATA FRAME ------\n')
    print(dfinal.head())

    # Dropping duplicates on a column
    tracks = dfinal[['artist', 'track', 'time']].drop_duplicates()

    print(tracks.head())

    # Set index of the tracks id
    tracks.index.name = 'id'
    tracks = tracks.reset_index()

    print('\n----- TRACKS DATA FRAME ------\n')
    tracks.head()

    # Joining/Merging data frames

    dfinal = pd.merge(tracks, dfinal, on=['track', 'artist', 'time'])

    print('\n----- FINAL MERGED DATA FRAME ------\n')
    print(dfinal.head())

    # Creating a tidy dataframe 
    # It's a data frame that gets read of unnecessary data
    tidy = dfinal.drop(['artist', 'track', 'time'], axis=1)

    print('\n----- TIDY DATA FRAME ------\n')
    print(tidy.head())

    # Ranks for minimal idx
    print(tidy.loc[tidy[tidy.week == 1]['rank'].idxmin()])

    # Converting a panda column to string
    # df['column'] = df['column'].str
    
    
    # maping panda columns to a new value
    # df['column'] = df['column'].map({'value': 'new-value', 'val2' : 'new-val-2', ...})

    # Drop non number on columns
    # df = df.dropna(subset['column'])


    # Writting data frame to csv
    # df.to_csv('path/to/files')