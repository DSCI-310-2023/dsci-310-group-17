import matplotlib.pyplot as plt
import seaborn as sns


def plot_correlations(data):
    """
    Takes in the cleaned dataset, selects only numerical features, and then calculates 
    the correlations between them and plots them as a heatmap

    Parameters
    ----------
    data: (pd.DataFrame) -> the dataset in which correlations are to be produced from

    Returns
    ----------
    fig: Heatmap visualizing the correlations of numeric features
    """
    print("Figure 1: Correlations of numeric features")
    numeric = data[['age', 'TSH', 'TT4', 'T4U', 'FTI']]
    cor = numeric.corr()
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.set(font_scale=1)
    sns.heatmap(cor, annot=True, ax=ax, cmap=plt.cm.Blues)
    return fig
