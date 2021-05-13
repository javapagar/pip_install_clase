## DATA CLEANING

There are the explanation of the following functions that we can apply to cleaning our DF.

### num_columns(df):

	Create a list with the names of the numeric columns of a dataframe.
    This function is used on rem_outliers and knn_missings.

    Params:
        - df = dataframe.


### rem_col_nan(df, per_na=.3, rem_print=False):

    If a column has more than 30 % NaN, will be removed.
    Percentage NaN could be changed on the params.

    Params:
        - df = dataframe.
        - per_na = percentage limit of Nan to remove the column, by default 0.30.
        - rem_print = print the list with removed columns.


### rem_outliers(df, z_num=3, shape_print=False):

	The rows with a value more than 3 z-score, will be removed.
    The z-score indicates if the number is an outlier.
    Z-Score could be changed on the input.

    Params:
        - df = dataframe
        - z_num = limit of z-score to consider an outlier, by default 3.
        - shape_print: print the number of rows removed.


### knn_missings(df, n_ngb=3):

    First calls the function to select the numeric columns of the dataframe
    and transform the NaN through a KNN with 3 neighbors (optional).
    The return change the values on the original dataframe.

    Params:
        df = dataframe.
        n_ngb = number of neighbors of KNN, by default 3.


### nlp_encoder(df, cols, encoder):

	This function compiles the most used encoders to have them all easily at hand,
    uses Sklearn and Pandas tools for its operation and currently has 4 functions
    which are called using their respective encoder.

    1º encoder = labelencoder:
        To use this encoder you must enter the column name that you want to be converted
        into multiple columns, it can be multiclass.

    2º encoder = binary:
        To use this encoder you must enter the column name that you want to be converted
        into 2 columns.
        This column must contain only 2 values, since the contained values are converted only into 0 and 1.

    3º encoder = onehotencoder:
        To use this encoder you must enter the column names that you want to be converted
        as many columns as there are variables.
        The function remove the original columns and add the new "variables columns" at the end.


    4º encoder = dummies:
        Similar to One hot encoder, you must enter the column names that you want to be converted as many columns as there are variables.
        The function remove the original columns and add the new "variables columns" at the end.

    Params:
    - df = dataframe.
    - cols = pass a list of columns to transform:
    - encoder = select as a string the desired encode to tranform:
        - labelencoder
        - binary
        - onehotencoder
        - dummies


