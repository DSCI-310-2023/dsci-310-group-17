import matplotlib.pyplot as plt


def visualize_classification(data, preds):
    """
    Produces a scatteplot with the classified data points for the  given dataset

    Parameters
    ----------
    data: (pd.DataFrame) -> the dataset the predictions are taken from
    preds: (pd.DataFrame) -> the classification predictions that have been produced

    Returns
    ----------
    fig: Scatterplot object visualizing the classifications of the data points
    """
    fig = plt.figure()
    plt.scatter(data["TSH"], data["TT4"], c=preds, s=50, cmap='viridis')
    plt.xlabel("TSH concentration")
    plt.ylabel("TT4 concentration")
    return fig
