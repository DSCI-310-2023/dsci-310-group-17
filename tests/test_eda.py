import pytest
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sys.path.append('src')
from eda import plot_correlations

def test_data():
    return pd.DataFrame({
        'age':[41,23,46,70],
        'TSH':[1.3, 4.1, 0.98, 0.16],
        'TT4':[125,102,109,175],
        'T4U':[1.14,0.91,0.87,1.3],
        'FTI':[109,120,70,141]
    })

def empty_plot():
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.set(font_scale=1)
    sns.heatmap(pd.DataFram(), annot=True, ax=ax, cmap=plt.cm.Blues)
    return fig

def test_plot_correlations_keyerror():
    try:
        result = plot_correlations(pd.DataFrame())
    except KeyError:
        print("Data must have the following columns: ['age', 'TSH', 'TT4', 'T4U', 'FTI']")

def test_plot_correlations_empty():
    try:
        empty_df = pd.DataFrame(columns=['age', 'TSH', 'TT4', 'T4U', 'FTI'])
        result = plot_correlations(empty_df)
    except ValueError:
        print("Data frame provided has correct columns but no data. Correlation cannot be made")
