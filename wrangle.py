#imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
import seaborn as sns
from sklearn.model_selection import train_test_split
from scipy import stats
from sklearn.preprocessing import MultiLabelBinarizer

warnings.filterwarnings("ignore")


'''
*------------------*
|                  |
|     ACQUIRE      |
|                  |
*------------------*
'''

def get_aac():
    """
    get_aac will :
    - read in Austin_Animal_Center_Intakes.csv & Austin_Animal_Center_Outcomes.csv
    return: right merged pandas dataframe
    """
    
    aac_intake = pd.read_csv('Austin_Animal_Center_Intakes.csv')
    
    aac_outcome = pd.read_csv('Austin_Animal_Center_Outcomes.csv')
    
    #df = pd.merge(aac_intake, aac_outcome, how='right')
    
    return pd.merge(aac_intake, aac_outcome, how='right')




    
'''
*------------------*
|                  |
|     PREPARE      |
|                  |
*------------------*
'''

def clean_aac(df):
    """
    clean_aac takes in right merged df
    - removes unnecessary columns
    - renames columns
    - encode: ages, sex, animal_type, adopted
    - change dtypes of certain columns
    - create new columns: is_pitbull, is_black
    - removes duplicate animal_ids
    - set animal_id as index
    """
    
    df = df.rename(columns={"Name": "name", "DateTime": "date", "MonthYear": "monthyear", "Animal ID": "animal_id", 
                       "Found Location": "found_loc", "Intake Type": "intake_type", "Intake Condition": "intake_cond", 
                       "Animal Type": "animal_type", "Sex upon Intake": "intake_sex", "Age upon Intake": "intake_age", 
                       "Breed": "breed", "Color": "color", "Date of Birth": "dob", "Outcome Type": "outcome_type", 
                       "Outcome Subtype": "outcome_subtype", "Sex upon Outcome": "outcome_sex", "Age upon Outcome": "outcome_age"})

    # remove time from `datetime` col  and convert dtype to date
    df['date'] = pd.to_datetime(df['date']).dt.date
    
    dropcols = ['name', 'monthyear', 'found_loc', 'intake_type', 'intake_cond', 'intake_sex', 'intake_age', 'outcome_subtype']
    df = df.drop(columns= dropcols)
    
    # drop negative age observations
    df = df[(df.outcome_age != '-1 years') & (df.outcome_age != '-2 years') & (df.outcome_age != '-3 years')]
    
    # drop blank outcome_type observations
    df = df[(df.outcome_type).isin(df.outcome_type.dropna())]
    
    # Drop blank outcome_age
    df = df[(df.outcome_age).isin(df.outcome_age.dropna())]

    # Drop blank outcome_sex
    df = df[(df.outcome_sex).isin(df.outcome_sex.dropna())]
    
    # filter df to only cats and dogs
    df = df[(df.animal_type != 'Other') & (df.animal_type != 'Bird') & (df.animal_type != 'Livestock')]
    
    # filter df to remove pets returned to owners
    df = df[(df.outcome_type != 'Return to Owner') & (df.outcome_type != 'Rto-Adopt')]
    
    # convert all 'puppies' to '0 years'
    df['outcome_age'] = np.where(df['outcome_age'].str.contains('day|days|weeks|week|month|months'), "0 years", df.outcome_age)
    
    # convert 'year' to 'years'
    df.replace('1 year', '1 years', inplace = True )
    
    # convert outcome_age to integer
    df['outcome_age'] = df.outcome_age.str.replace('years', '').astype(int)
    
    #encode ages
    df['elderly'] = np.where(df.outcome_age > 5, 1, 0 )
    df['full_grown'] = np.where((df.outcome_age < 6) & (df.outcome_age > 1), 1, 0 )
    df['youngins'] = np.where(df.outcome_age < 2, 1, 0 )
    
    # encode sex
    df['neutered_male'] = np.where(df.outcome_sex ==  "Neutered Male", 1, 0 )
    df['intact_male'] = np.where(df.outcome_sex ==  "Intact Male", 1, 0 )
    df['neutered'] = np.where((df.outcome_sex ==  "Neutered Male") | (df.outcome_sex ==  "Spayed Female"), 1, 0 )
    df['is_male'] = np.where((df.outcome_sex ==  "Neutered Male") | (df.outcome_sex ==  "Intact Male"), 1, 0 )
    
    # encode animal_type
    dummy_df = pd.get_dummies(df.animal_type, prefix="is", drop_first=True)
    # append dummy column
    df = pd.concat([df, dummy_df], axis =1)
  
    
    # new columns
    df['is_pitbull'] = np.where(df['breed'].str.contains('Pit|American Staffordshire|Staffordshire'), 1, 0)
    
    df['is_black'] = np.where(df.color == "Black", 1, 0)
    
        
    # encode outcome_type
    df['adopted'] = np.where(df.outcome_type == "Adoption", 1, 0)
    
    # drop duplicates
    df = df.sort_values('date').drop_duplicates('animal_id', keep='last')
    
    # drop encoded/unncessary columns
    cols = ['animal_type', 'outcome_type', 'outcome_sex']
    df = df.drop(columns= cols)
    
    # List of cols to convert to 'str'
    colms = ['date', 'breed', 'color', 
            'dob']
    # loop through cols list in conversion
    for colm in colms:
        df[colm] = df[colm].astype('str')
    
    df = df.set_index("animal_id")
    
    return df





def clean_aac001(df):
    """
    clean_aac takes in right merged df
    - removes unnecessary columns
    - renames columns
    - encode: ages, sex, animal_type, adopted
    - change dtypes of certain columns
    - create new columns: is_pitbull, is_black
    """
    
    df = df.rename(columns={"Name": "name", "DateTime": "date", "MonthYear": "monthyear", "Animal ID": "animal_id", 
                       "Found Location": "found_loc", "Intake Type": "intake_type", "Intake Condition": "intake_cond", 
                       "Animal Type": "animal_type", "Sex upon Intake": "intake_sex", "Age upon Intake": "intake_age", 
                       "Breed": "breed", "Color": "color", "Date of Birth": "dob", "Outcome Type": "outcome_type", 
                       "Outcome Subtype": "outcome_subtype", "Sex upon Outcome": "outcome_sex", "Age upon Outcome": "outcome_age"})

    # remove time from `datetime` col  and convert dtype to date
    df['date'] = pd.to_datetime(df['date']).dt.date
    
    dropcols = ['name', 'monthyear', 'found_loc', 'intake_type', 'intake_cond', 'intake_sex', 'intake_age', 'outcome_subtype']
    df = df.drop(columns= dropcols)
    
    # drop negative age observations
    df = df[(df.outcome_age != '-1 years') & (df.outcome_age != '-2 years') & (df.outcome_age != '-3 years')]
    
    # drop blank outcome_type observations
    df = df[(df.outcome_type).isin(df.outcome_type.dropna())]
    
    # Drop blank outcome_age
    df = df[(df.outcome_age).isin(df.outcome_age.dropna())]

    # Drop blank outcome_sex
    df = df[(df.outcome_sex).isin(df.outcome_sex.dropna())]
    
    # filter df to only cats and dogs
    df = df[(df.animal_type != 'Other') & (df.animal_type != 'Bird') & (df.animal_type != 'Livestock')]
    
    # filter df to remove pets returned to owners
    df = df[(df.outcome_type != 'Return to Owner') & (df.outcome_type != 'Rto-Adopt')]
    
    # convert all 'puppies' to '0 years'
    df['outcome_age'] = np.where(df['outcome_age'].str.contains('day|days|weeks|week|month|months'), "0 years", df.outcome_age)
    
    # convert 'year' to 'years'
    df.replace('1 year', '1 years', inplace = True )
    
    # convert outcome_age to integer
    df['outcome_age'] = df.outcome_age.str.replace('years', '').astype(int)
    
    #encode ages
    df['elderly'] = np.where(df.outcome_age > 5, 1, 0 )
    df['full_grown'] = np.where((df.outcome_age < 6) & (df.outcome_age > 1), 1, 0 )
    df['youngins'] = np.where(df.outcome_age < 2, 1, 0 )
    
    # encode sex
    df['neutered_male'] = np.where(df.outcome_sex ==  "Neutered Male", 1, 0 )
    df['intact_male'] = np.where(df.outcome_sex ==  "Intact Male", 1, 0 )
    df['neutered'] = np.where((df.outcome_sex ==  "Neutered Male") | (df.outcome_sex ==  "Spayed Female"), 1, 0 )
    df['is_male'] = np.where((df.outcome_sex ==  "Neutered Male") | (df.outcome_sex ==  "Intact Male"), 1, 0 )
    
    # encode animal_type
    dummy_df = pd.get_dummies(df.animal_type, prefix="is", drop_first=True)
    # append dummy column
    df = pd.concat([df, dummy_df], axis =1)
  
    
    # new columns
    df['is_pitbull'] = np.where(df['breed'].str.contains('Pit|American Staffordshire|Staffordshire'), 1, 0)
    
    df['is_black'] = np.where(df.color == "Black", 1, 0)
    
        
    # encode outcome_type
    df['adopted'] = np.where(df.outcome_type == "Adoption", 1, 0)
    
    # drop duplicates
    df = df.sort_values('date').drop_duplicates('animal_id', keep='last')
    
    # drop encoded/unncessary columns
    cols = ['animal_type', 'outcome_type', 'outcome_sex']
    df = df.drop(columns= cols)
    
    # List of cols to convert to 'str'
    colms = ['date', 'breed', 'color', 
            'dob']
    # loop through cols list in conversion
    for colm in colms:
        df[colm] = df[colm].astype('str')
        
    df = df.reset_index(drop=True)
    
    return df




def encode_df(df):
    """
    
    """
    
    df = df.copy()
    
    df = df.reset_index(drop=True)
    
    # Creating list of multi-labels: BREED
    breed_list = df.breed.apply(lambda x: list(x.split("/")))
    
    # Converting it into dataframe and working on it seperately: BREED
    breed_df =pd.DataFrame({"breed":breed_list})
    
    # instantiating MultiLabelBinarizer: BREED
    mlb = MultiLabelBinarizer()
    breed_encoded = pd.DataFrame(mlb.fit_transform(breed_df["breed"]),columns=mlb.classes_)
    
    
    # Creating list of multi-labels: COLOR
    color_list = df.color.apply(lambda x: list(x.split("/")))
    
    # Converting it into dataframe and working on it seperately: COLOR
    color_df =pd.DataFrame({"color":color_list})
    
    # instantiating MultiLabelBinarizer: COLOR
    mlb = MultiLabelBinarizer()
    color_encoded = pd.DataFrame(mlb.fit_transform(color_df["color"]),columns=mlb.classes_)
    
    
    return pd.concat([df, breed_encoded, color_encoded], axis =1)




def split_df(df, target, seed):
    '''
    split_df will take one argument(df) and 
    then split our data into 20/80, 
    then split the 80% into 30/70
    
    performs a train, validate, test split
    
    splits each of the 3 samples into a dataframe with independent variables
    and a series with the dependent, or target variable. 
    
    The function returns 6 dataframes and 3 series:
    train, validate, test split, X_train (df) & y_train (series), X_validate & y_validate, X_test & y_test. 
    '''
    # Train, Validate, and test
    train_and_validate, test = train_test_split(df, test_size=0.2, random_state=seed)
    train, validate = train_test_split(train_and_validate, test_size=0.3, random_state=seed)
    
    # Split with X and y
    X_train = train.drop(columns=[target])
    y_train = train[target]
    
    X_validate = validate.drop(columns=[target])
    y_validate = validate[target]
    
    X_test = test.drop(columns=[target])
    y_test = test[target]
    
    return train, validate, test, X_train, y_train, X_validate, y_validate, X_test, y_test 





def get_object_cols(df):
    '''
    This function takes in a dataframe and identifies the columns that are object types
    and returns a list of those column names. 
    '''
    # create a mask of columns whether they are object type or not
    mask = np.array((df.dtypes == "object") | (df.dtypes == "category"))

        
    # get a list of the column names that are objects (from the mask)
    object_cols = df.iloc[:, mask].columns.tolist()
    
    return object_cols





def get_numeric_X_cols(train, object_cols):
    '''
    takes in a dataframe and list of object column names
    and returns a list of all other columns names, the non-objects. 
    '''
    numeric_cols = [col for col in train.columns.values if col not in object_cols]
    
    return numeric_cols   