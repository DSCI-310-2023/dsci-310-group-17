import pytest
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sys.path.append('./../src/')
from CleanData import relabel_bclass, col_dtype_reformat
from AnalysisVisualizations import visualize_classification
from EDA import plot_correlations


def test_relabel_bclass():
    # Create Sample DataFrame
    pre_df = pd.DataFrame({'age': [1,2,3,4,5,6,7,8,9,10],
                           'binaryClass': ['negative.|3733', 'negative.|1442', 'n',
                                           'nABC123', 'hyperthyroid.|108', 'h',
                                           'T3 toxic.|1304', 'T', 'goitre.|2416', 'g']})
    ref_df = pd.DataFrame({'age': [1,2,3,4,5,6,7,8,9,10],
                           'binaryClass': ['P', 'P', 'P',
                                           'P', 'N', 'N',
                                           np.nan, np.nan, np.nan, np.nan]})
    post_df = relabel_bclass(pre_df)
    # Assert that only expected values were found in column
    assert(post_df.binaryClass.unique().tolist() == ['P', 'N', np.nan])
    # Assert that changes were as expected
    assert(post_df.equals(ref_df))

def test_col_dtype_reformat():
    num_cols = ['num1', 'num2', 'num3', 'abc']
    cat_cols = ['cat1', 'cat2']

    pre_df = pd.DataFrame(columns = ['num1', 'num2', 'abc', 'cat1', 'cat2', 'num3'],
                          dtype=object)

    post_df = col_dtype_reformat(num_cols, cat_cols, pre_df)

    # Assert the columns are casted to the correct dtypes
    assert((post_df[num_cols].dtypes == np.float64).all())
    assert((post_df[cat_cols].dtypes == 'category').all())

#def test_visualize_classification():


#def test_plot_correlations
