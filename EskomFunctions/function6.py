### START FUNCTION
""" This function takes pandas dataframe as input, split the sentence into a list of separate words and returns a modified dataframe"""
def word_splitter(df):
    # your code here
    # initializing char to increment through the data frame with
    char = 0
    
    # each char (word) encountered has the .lower and .split methods applied to it 
    # in the data frame as in increments
    df['Split Tweets'] = [char.lower().split() for char in df['Tweets']]
    
    # the returned result should be displayed 
    # in the following columns and rows using the .head function
    df[['Tweets','Date', 'Split Tweets']].head()
    
    #return result
    return (df)

### END FUNCTION
