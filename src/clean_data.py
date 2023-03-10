import numpy as np


def relabel_bclass(hyper_df):
    """
    Dataset provided by UCI is backwards for hyperthyroid classification, "P" referse to negative diagnosis
        while "N" refers to positive diagnosis. This function relabels the binaryClass column correctly
        and assigns all extra values to np.nan.
        (http://archive.ics.uci.edu/ml/machine-learning-databases/thyroid-disease/)

    Parameters
    ----------
    hyper_df: pd.DataFrame()
    Pandas data frame containing raw hyperthyroid datasets

    Returns
    ----------
    output_df: pd.DataFrame()
        Modified pandas data frame containing relabeled values for the 'binaryClass' column
    """

    output_df = hyper_df.replace({'binaryClass': {r'n.*': 'P',
                                                  r'h.*': 'N',
                                                  r'T.*': np.nan,
                                                  r'g.*': np.nan,
                                                  r's.*': np.nan}}, regex=True)
    return(output_df)


def col_dtype_reformat(num_cols, cat_cols, hyper_df):
    """
     Reformats the data types of specified numerical and categorical columns to the corresponding 'float64'
        and 'category' dtypes for classification analysis. All rows with np.nan values will be dropped to
        ensure that data types are correctly casted
    Parameters
    ----------
    num_cols: list
        list of column names to be casted to 'float64'
    cat_cols: list
        list of column names to be casted to 'category'
    hyper_df: pd.DataFrame()
        Pandas data frame containing hyperthyroid datasets

    Returns
    ----------
    output_df: pd.DataFrame()
        Modified pandas data frame with relabeled column
    """
    # Ensures dropping of np.nan values to ensure correct casting
    output_df = hyper_df.dropna()

    output_df[num_cols] = output_df[num_cols].astype('float64')
    output_df[cat_cols] = output_df[cat_cols].astype('category')

    return(output_df)
