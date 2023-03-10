import sys

sys.path.append('src')
from eda import plot_correlations

def test_plot_correlations():
    # Create Sample DataFrame
    df = pd.DataFrame({'age': [1,2,3,4,5,6,7,8,9,10],
                       'binaryClass': ['P', 'P', 'P',
                                       'P', 'N', 'N',
                                       np.nan, np.nan, np.nan, np.nan]})
    # Assert that the function runs without error
    assert(plot_correlations(df) == None)
    assert(plot_correlations(df, 'binaryClass') == None)
    assert(plot_correlations(df, 'binaryClass', 'binaryClass') == None)