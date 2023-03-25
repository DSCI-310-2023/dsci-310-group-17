import pytest
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas.api.types import CategoricalDtype

sys.path.append('src')
from clean_data import relabel_bclass, col_dtype_reformat

def test_relabel_bclass_returns():
    """
    Tests that relabel_bclass returns a pd.DataFrame
    Parameters
    ----------
    None
    Returns
    ----------
    True if relabel_bclass produces a pd.DataFrame , AssertionError otherwise
    """
    pre_df = pd.DataFrame({'age': [1,2,3,4,5,6,7,8,9,10],
                           'binaryClass': ['negative.|3733', 'negative.|1442', 'n',
                                           'nABC123', 'hyperthyroid.|108', 'h',
                                           'T3 toxic.|1304', 'T', 'goitre.|2416', 'g']})
    ref_df = pd.DataFrame({'age': [1,2,3,4,5,6,7,8,9,10],
                           'binaryClass': ['P', 'P', 'P',
                                           'P', 'N', 'N',
                                           np.nan, np.nan, np.nan, np.nan]})
    assert isinstance(relabel_bclass(pre_df), pd.DataFrame)

def test_relabel_bclass_relabels():
    """
    Tests that relabel_bclass correctly relabels entries in the binaryClass column
    Parameters
    ----------
    None
    Returns
    ----------
    True if relabel_bclass correctly relabels the binaryClass column, AssertionError otherwise
    """
    pre_df = pd.DataFrame({'age': [1,2,3,4,5,6,7,8,9,10],
                           'binaryClass': ['negative.|3733', 'negative.|1442', 'n',
                                           'nABC123', 'hyperthyroid.|108', 'h',
                                           'T3 toxic.|1304', 'T', 'goitre.|2416', 'g']})
    ref_df = pd.DataFrame({'age': [1,2,3,4,5,6,7,8,9,10],
                           'binaryClass':  ['P', 'P', 'P',
                                           'P', 'N', 'N',
                                           np.nan, np.nan, np.nan, np.nan]})
    result = relabel_bclass(pre_df)
    pd.testing.assert_frame_equal(result, ref_df)

def test_data_col_dtype_reformat():
    """
    Creates a mock dataframe to use for future tests regarding col_dtype_reformat
    Parameters
    ----------
    None
    Returns
    ----------
    pd.DataFrame: A mock dataframe with a subset of the data used
    """
    return pd.DataFrame({'age': ['41','23','46','70'],
                        'sex': ['F','F','M','F'],
                        'TSH':['1.3','4.1','0.98','0.16'],
                        'hypopituitary': ['f','f','f','f']})

def test_col_dtype_reformat_returns():
    """
    Tests that col_dtype_reformat returns a pd.DataFrame
    Parameters
    ----------
    None
    Returns
    ----------
    True if col_dtype_reformat produces a pd.DataFrame , AssertionError otherwise
    """
    num = ['age','TSH']
    cat = []
    result = col_dtype_reformat(num, cat, test_data_col_dtype_reformat())
    assert isinstance(result, pd.DataFrame)

def test_col_dtype_reformat_datatypes():
    """
    Tests that col_dtype_reformat correctly reformats the datatypes
    Parameters
    ----------
    None
    Returns
    ----------
    True if col_dtype_reformat correctly alters the datatypes, AssertionError otherwise
    """
    num = ['age','TSH']
    cat = []
    result = col_dtype_reformat(num, cat, test_data_col_dtype_reformat())
    actual_types = result.dtypes
    expected_types = pd.Series({'age': 'float64',
                                'sex': 'object',
                                'TSH': 'float64',
                                'hypopituitary': 'object'})
    assert actual_types.equals(expected_types)