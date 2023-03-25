import argparse
import pandas as pd
import os
import matplotlib.pyplot as plt
from pandas.plotting import table
from eda import plot_correlations

def main(input_path, output_folder):
    """
    Creates EDA figure and table based on clean data
    Stores them at the given output folder

    Parameters
    ----------
    input_path: (string) -> path to clean data

    output_path: (string) -> stores figures and CSVs to this file
    
    Returns
    ----------
    None
    """
    df = pd.read_csv(input_path)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # save and plot data description to png
    ax = plt.subplot(111, frame_on = False)
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    table(ax, df.describe(), rowLabels=['']*df.describe().shape[0], loc='center')
    desc = df.describe()
    df.describe().to_csv(output_folder + "/data_described.csv")
    #save data description to csv/dataframe
    plot_correlations(df).savefig(output_folder + "/correlation_of_numeric_features.png", bbox_inches='tight')


if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="Creates ans saves figures from clean data")
    parse.add_argument("file_path", help = "Path to clean data file")
    parse.add_argument("output_path", help = "Filename to save ")
    arg = parse.parse_args()
    main(arg.file_path, arg.output_path)
