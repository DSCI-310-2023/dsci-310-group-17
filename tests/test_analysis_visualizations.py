import sys
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sys.path.append('src')
from analysis_visualizations import visualize_classification

def test_data():
    """
    Produces a mock dataset to be used for testing
    Parameters
    ----------
    None
    Returns
    ----------
    pd.DataFrame: mock data frame with a small subset of data
    """
    return pd.DataFrame({
        'age':[41,23,46,70],
        'TSH':[1.3, 4.1, 0.98, 0.16],
        'TT4':[125,102,109,175],
        'T4U':[1.14,0.91,0.87,1.3],
        'FTI':[109,120,70,141]
    })

def empty_plot():
    """
    Produces an empty scatterplot
    Parameters
    ----------
    None
    Returns
    ----------
    fig: An empty scatterplot with specified axis labels
    """
    fig = plt.figure()
    plt.scatter(pd.DataFrame(), pd.DataFrame(), c=np.empty(0), s=50, cmap='viridis')
    plt.xlabel("TSH concentration")
    plt.ylabel("TT4 concentration")
    # Add a color bar to the plot
    cb = plt.colorbar()
    cb.set_label('Color Label')
    return fig

def test_visualize_classification_keyerror():
    """
    Tests that the correct columns exist in the dataframe when visualize_classification is used
    Parameters
    ----------
    None
    Returns
    ----------
    None if no error, prints "Column TSH and/or TT4 do not exist" if KeyError is present
    """
    try:
        result = visualize_classification(pd.DataFrame(), np.random.randint(low=0, high = 2, size = (4,)))
    except KeyError:
        print("Column TSH and/or TT4 do not exist")

def test_visualize_classification_axeslabels():
    """
    Tests that the plot axis labels are correct when visualize_classification is used
    Parameters
    ----------
    None
    Returns
    ----------
    True if axis labels are correct, AssertionError if axis labels are incorrect
    """
    result = visualize_classification(test_data(), np.random.randint(low=0, high = 2, size = (4,)))
    assert(result.get_axes()[0].get_xlabel() == 'TSH concentration')
    assert(result.get_axes()[0].get_ylabel() == 'TT4 concentration')

def test_visualize_classification_empty():
    """
    Tests that utilizing visualize_classification with an empty dataset returns an empty plot
    Parameters
    ----------
    None
    Returns
    ----------
    True if an empty plot is created, AssertionError otherwise
    """
    empty_df = pd.DataFrame(columns=['age', 'TSH', 'TT4', 'T4U', 'FTI'])
    result = visualize_classification(empty_df, np.empty(0))
    assert(result.show() == empty_plot().show())

