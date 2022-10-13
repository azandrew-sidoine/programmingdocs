# Python Statistics Essential Training


## Data cleaning

> df.loc[start:end:step] - Select a range of rows in a dataset

```py
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

    # Minimum of a data frame
    df.min() # It returns the min per column

    # Maximum of the data frame
    df.max()

    # Mean
    df.mean()

    # Variance
    df.var(ddof=0)

    # Quantile
    df.quantile([.25, .75, .5])

    # Median
    df.quantile([.5])
    df.median()

    # Sum column values
    df['column'].sum()

    # Grouping columns by
    df[df.year == 2015].groupBy('column')['column'].sum()

    # Plotting scatter matrix
    pd.plotting.scatter_matrix(df, figsize=(Tuple))

    # Value count of categorical columns. It kind of group duplicates by number of occurences
    df['column'].value_counts(normalize=True|False)

    # df.unstack() - Call on df grouped by a given colum
    groupedDf.unstack()

```

## Data plotting


- Plotting with panda data frames

> df.plot.scatter(<x_colum>, <y_column>, colormap=matplotlib.cm.get_cmap('Color'), <DataPointAreaMeasurement>=Number, <colors>="String|Map", <linewidths>=Number, <edgecolors>=Color, figsize=(Tuple))

- Distributions

> scipy.stats.percentileofscore(df[<Column>], <MaxValue>) - Percentage of the rows that has the column value less that the MaxValue

- Histograms

> df.plot(kind='box') - Return / Create a box plot

> df.boxplot() - Return / Create a box plot

> df.plot(kind='hist', histtype='step', bins=<Number>, density=<Boolean>) - Plot a histograms

> plt.axvline(df.mean(), c=<Color>, linestyle=<String>) - Draw a vertical line on a matplotlib plot

> plt.plot(kind='density') - Plot the density plot

Note: linestyle -> ':', '--', None.
We can plot means, quantiles(medians, etc..),

> df.plot.line(x=<XColumn>, y=X=<Y_Column>, axis=1)

> plt.axis(xmin=<MinimumValueOfXCoordinate>, xmax=<MaximumValueOfXCoordinate>, ymin=<MinimumValueOfYCoordinate>, ymax=<MaximumValueOfYCoordinate>) Setting axis ranges

> plt.subplot(<Number_Of_Row>, <Number_of_Row>, <Index_of_Page>); df.plot(kind='bar', stack=<Boolean>) - Subplotting in panda

- Categorical variables

> pd.Categorical(df, ordered=True, categories=[...<ListOfCategories>]) -> Return a column with categories converted to numerical values

## Statistical inferrence

Process for finding understanding in the data in order to draw conclusion from data.

- Interval de confiance

Soit µ=`Moyenne de la Population total`, ∂=`Ecart type de la population total`

Soit, x_hat=`Population des Moyennes d'echantillonage` µ_x_hat=`Moyenne de la Distributiin d'echantillonnage des x_hat`, ∂_x_hat≈√x `Ecart type de la Distributiin d'echantillonnage des x_hat`

> Confidence Interval : It's found from the data so that .95 probability of the time, it will include the True values.