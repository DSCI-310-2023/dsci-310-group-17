import sys

sys.path.append('src')
from analysis_visualizations import visualize_classification

def test_visualize_classification():
    # Create Sample DataFrame
    df = pd.DataFrame({'age': [1,2,3,4,5,6,7,8,9,10],
                       'binaryClass': ['P', 'P', 'P',
                                       'P', 'N', 'N',
                                       np.nan, np.nan, np.nan, np.nan]})
    # Assert that the function runs without error
    assert(visualize_classification(df) == None)
    assert(visualize_classification(df, 'binaryClass') == None)
    assert(visualize_classification(df, 'binaryClass', 'binaryClass') == None)