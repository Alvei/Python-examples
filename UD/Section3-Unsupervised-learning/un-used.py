def create_attributes_per_flag(df):
    """ Create a column with a list of all the attribute flags. Then create a dictionary of the flags
        and a corresponding list of column names.
        INPUT:  df of data
        OUTPUT: dictionary of attributes where the key is the flag => list of attributes to
    """
    print(f"\t Converting col 4 to a dict with key:flag and value:list of attributes where flag is found")
    df['Flags'] = df.iloc[:,3].apply(lambda x: x[1:-1].split(',')) # Convert the str to list of str

    flags  = ['-1','0', '9', 'X', 'XX']
    dict_attr = {}
    for flag in flags:
        mask = df.Flags.apply(lambda x: flag in x)  # Check to see if the flag is the in converted list in last column
        df1  = df[mask]                             # Create a DF with only the rows where the flag is found
        attr = df1.attribute.tolist()               # Create list of attributes and save in dictionary
        dict_attr[flag] = attr
        print(f"\tflag:{flag}\t-> {len(attr)} attributes")

    return dict_attr

def create_attr_to_clean(df, col_to_clean, dict_flag):
    """ Identify the attributes (columns) that require cleaning.
        INPUT:  DataFrame, dictionary of flags, dict_flag
        OUTPUT: dictionary of flags
    """
    new_col_to_clean = {}
    for key, value in dict_flag.items():
        df_tmp = df.loc[:, col_to_clean[key]]        # Identify the columns where there is flag
        mask_sum = (df_tmp == value).sum()                # Create a true/false DF if the the flag is found then sum
        res = mask_sum[mask_sum > 0]                      # Keep only the attributes where a change is to be made
        print(f"\tflag:{key}\t=> {len(res)} of {df_tmp.shape[1]} columns")
        new_col_to_clean[key] = res.index.tolist()
    return new_col_to_clean

flags  = ['-1','0', '9', 'X', 'XX']
dict_attr = {}
for flag in flags:
    mask = df.Flags.apply(lambda x: flag in x)  # Check to see if the flag is the in converted list in last column
    df1  = df[mask]                             # Create a DF with only the rows where the flag is found
    attr = df1.attribute.tolist()               # Create list of attributes and save in dictionary
    dict_attr[flag] = attr
    print(f"\tflag:{flag}\t-> {len(attr)} attributes")

# pre-processing check number of missing data
pre = azdias.isna().sum()
print(f" No. of attributes with missing data: {pre[pre>0].count()} out of {max_col}")
id_max = pre.idxmax()
print(f" {id_max} attribute has max missing data of any attribute with {100*pre[pre>0].max()/max_row:.2f}%")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5), sharey=True, sharex=True)
ax1.hist(pre, bins=10,  color='#86bf91')
ax1.set_ylabel('Number of attributes')
ax1.set_title('Histogram - bin = 10')

ax2.hist(pre, bins=25, color='#86bf91')
ax1.set_xlabel('Number of missing data for attributes')
ax2.set_xlabel('Number of missing data for attributes')
ax2.set_title('Histogram - bin = 25');


criterion= 200000             # Threshold
exceed = pre[pre>criterion]*100/max_row
print(f"No. attributes that exceed the threshold {criterion:,} of missing data: {len(exceed)}")

dict_flag = {'-1':-1, '0':0, '9':9, 'X':'X', 'XX':'XX'}  # Needed dict because map str->int and str->str
attr_per_flag = create_attributes_per_flag(feat_info)    # Create a dictionary of attr to clean with the flag
col_to_clean  = create_attr_to_clean(azdias, attr_per_flag, dict_flag)

# Loop over all the known flags that could be in column 4. The key is the str flag and the value is the int or str
for key, value in dict_flag.items():
    for col in col_to_clean[key]: # For each of the flag, run through the columns and replace the flag with NaN
       # print(f"Flag: {key} Replacing flag with NaN: {col}")
       azdias[col].replace(value, np.nan, inplace=True)

#attr_per_flag
col_to_clean


def clean_data(azdias, feat_info):
    """
    Perform feature trimming, re-encoding, and engineering for demographics
    data

    INPUT: Demographics DataFrame
    OUTPUT: Trimmed and cleaned demographics DataFrame
    """

    max_row, max_col = azdias.shape

    print("1. Convert missing value codes into NaNs...")
    # Find attributes where missing values
    dict_flag     = {'-1':-1, '0':0, '9':9, 'X':'X', 'XX':'XX'}  # Needed dict because map str->int and str->str
    attr_per_flag = create_attributes_per_flag(feat_info)        # Create a dictionary of attr to clean with the flag
    col_to_clean  = create_attr_to_clean(azdias, attr_per_flag, dict_flag)

    for key, value in dict_flag.items():
        for col in col_to_clean[key]: # For each of the flag, run through the columns and replace the flag with NaN
            azdias[col].replace(value, np.nan, inplace=True)

    print("2. Removing cols with alot of missing data...")
    post = azdias.isna().sum()
    #print(f" No. of attributes with missing data {post[post>0].count()} out of {max_col}")
    criterion = 200000
    col_to_investigate = post[post>criterion].index.tolist()
    azdias_new  = azdias.drop(col_to_investigate, axis=1)
    print(f"\tCol drop criterion > {criterion:,}")
    print(f"\tDrop {len(col_to_investigate)} attributes: {col_to_investigate}")
    print(f"\tShape of DF:{azdias.shape} ")
    max_col_new = azdias_new.shape[1]

    print("3. Removing rows with alot of missing data...")
    row_missing_data = azdias_new.isna().sum(axis=1)/max_col_new   # represent as %
    criterion = .2
    list_of_rows = row_missing_data[row_missing_data>criterion].index.tolist()
    print(f"\tRow drop criterion > {criterion*100:.2f}%")
    print(f"\tDrop {len(list_of_rows):,} or {len(list_of_rows)*100/max_row:.2f}% of rows")
    azdias_new_low = azdias_new.drop(list_of_rows)
    print(f"\tShape of DF:{azdias_new_low.shape} ")
    azdias_new2 = azdias_new_low.copy()

    ### select, re-encode, and engineer column values.

    # Assess categorical variables: which are binary, which are multi-level, and which one needs to be re-encoded?
    categorical = feat_info[feat_info['type'] == 'categorical']['attribute'].tolist()  # get a list of categorical attributes
    mixed       = feat_info[feat_info['type'] == 'mixed']['attribute'].tolist()        # get a list of mixed attributes
    mixed.remove("KBA05_BAUMAX")                                                       # Already removed
    categorical = list(set(categorical) & set(azdias_new_low.columns))   # Necessary to eliminate the attributes already eliminated

    print("4. Convert binary attribute to number...")
    quick_dict = {'W': 1, 'O':2}
    azdias_new2['OST_WEST_KZ'] = azdias_new2['OST_WEST_KZ'].replace(quick_dict)

    categorical_bin = []
    for col in categorical:
        tmp = azdias_new2[col].unique()
        #print(f"{col}:\t\t{tmp}")
        if len(tmp) == 2:
            categorical_bin.append(col)

    categorical_to_drop = categorical

    print("5. Remove the binary attributes")
    for col in categorical_bin:
        categorical_to_drop.remove(col)

    print(f"\tDrop {len(categorical_to_drop)} categorical attributes" )

    azdias_new2.drop(categorical_to_drop, axis=1, inplace=True)
    print(f"\tShape of DF: {azdias_new2.shape}")

    PRAEGENDE_dict = { 1: [40, 1],  2: [40, 2], 3: [50, 1],  4: [50, 2],
                       5: [60, 1],  6: [60, 2], 7: [60, 2],  8: [70, 1], 9: [70, 2],
                      10: [80, 1], 11: [80, 2], 12: [80, 1], 13: [80, 2],
                      14: [90, 1], 15: [90, 2], np.nan: [90, 1]
                     }

    # Create a DF with the lists in each cell
    print("6. Cleaning two mixed attributes...")
    b = azdias_new2["PRAEGENDE_JUGENDJAHRE"].map(PRAEGENDE_dict).to_frame()
    azdias_new2[['decade','movement']]= pd.DataFrame(b.PRAEGENDE_JUGENDJAHRE.tolist(), index= b.index) # Create the two columns


    azdias_new2["CAMEO_INTL_2015"].replace(np.nan, 52, inplace=True)

    mixed.remove("CAMEO_INTL_2015")  # Do not remove this column

    azdias_new2.drop(mixed, axis=1, inplace=True)
    print(f"\tDroping {len(mixed)} mixed attributes: {mixed}")
    print(f"\tShape of DF: {azdias_new2.shape}")

    # Data type of the attribute is string. Need to convert to integer first.
    # Then note that by dividing by 10 and reconverting to integer we can do the mapping
    azdias_new2["CAMEO_INTL_2015"] = azdias_new2["CAMEO_INTL_2015"].astype('int').div(10).astype('int')

    ### Return the cleaned dataframe.
    print("*** DONE! ***")
    return azdias_new2



# Apply feature scaling to the general population demographics data.
scaler = StandardScaler()
person_features = ['AGER_TYP', 'ALTERSKATEGORIE_GROB', 'ANREDE_KZ', 'CJT_GESAMTTYP',
                   'FINANZ_MINIMALIST', 'FINANZ_SPARER', 'FINANZ_VORSORGER', 'FINANZ_ANLEGER',
                   'FINANZ_UNAUFFAELLIGER', 'FINANZ_HAUSBAUER', 'FINANZTYP', 'GEBURTSJAHR',
                   'GFK_URLAUBERTYP', 'GREEN_AVANTGARDE', 'HEALTH_TYP', 'LP_LEBENSPHASE_FEIN',
                   'LP_LEBENSPHASE_GROB', 'LP_FAMILIE_FEIN', 'LP_FAMILIE_GROB', 'LP_STATUS_FEIN',
                   'LP_STATUS_GROB', 'NATIONALITAET_KZ', 'PRAEGENDE_JUGENDJAHRE', 'RETOURTYP_BK_S',
                   'SEMIO_SOZ', 'SEMIO_FAM', 'SEMIO_REL', 'SEMIO_MAT', 'SEMIO_VERT', 'SEMIO_LUST',
                   'SEMIO_ERL', 'SEMIO_KULT', 'SEMIO_RAT', 'SEMIO_KRIT', 'SEMIO_DOM', 'SEMIO_KAEM',
                   'SEMIO_PFLICHT', 'SEMIO_TRADV', 'SHOPPER_TYP', 'SOHO_KZ', 'TITEL_KZ', 'VERS_TYP', 'ZABEOTYP']
features = df.columns.tolist()

# Use set math to find the list of remaining features that are person-level
remaining_person_features = list(set(features) & set(person_features))
df_scaled = df.copy()
df_scaled[remaining_person_features] = scaler.fit_transform(df[remaining_person_features])