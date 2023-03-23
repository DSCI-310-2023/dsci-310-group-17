import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from analysis_visualizations import visualize_classification
from eda import plot_correlations
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.linear_model import LogisticRegression
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.pipeline import make_pipeline

from pandas.plotting import table

def main(input_path, output_folder):
    hyper_clean = pd.read_csv(input_path)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)



    #plot data description
    ax = plt.subplot(111, frame_on = False)
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    table(ax, hyper_clean.describe(), rowLabels=['']*hyper_clean.describe().shape[0], loc='center')
    plt.savefig(output_folder + "/data_described.png", bbox_inches="tight")
    hyper_clean.describe().to_csv(output_folder + "/data_described.csv")

    plot_correlations(hyper_clean).savefig(output_folder + "/correlation_of_numeric_features.png", bbox_inches='tight')



    #model training & analysis
    # Splitting data
    X = hyper_clean.drop(columns="binaryClass")
    y = hyper_clean['binaryClass']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    # Preprocessing data
    onehot = ['sex', 'on thyroxine', 'query on thyroxine', 'on antithyroid medication',
            'sick', 'pregnant', 'thyroid surgery', 'I131 treatment', 'query hypothyroid',
            'query hyperthyroid', 'lithium', 'goitre', 'tumor', 'psych', 'hypopituitary']
    numeric = ['age', 'TSH', 'TT4', 'T4U', 'FTI']
    ct = make_column_transformer(
        (StandardScaler(), numeric),
        (OneHotEncoder(handle_unknown='ignore'), onehot)
    )
    transformed_X_train = ct.fit_transform(X_train)
    transformed_X_test = ct.transform(X_test)

    # Creating LogisticRegression Classifier
    pipe_log = make_pipeline(ct, LogisticRegression(max_iter=1000, C=1))
    cv = cross_validate(pipe_log, X_train, y_train, error_score='raise', return_train_score=True)


    lr = LogisticRegression(max_iter=1000, C=1)
    X_train_trans = ct.fit_transform(X_train)
    X_test_trans = ct.transform(X_test)
    lr.fit(X_train_trans, y_train)
    train_preds = lr.predict(X_train_trans)

    visualize_classification(X_train, train_preds).savefig(output_folder + "/TSH_vs_TT4_concentration_training_set", bbox_inches='tight')

    #test set
    test_preds = lr.predict(X_test_trans)
    visualize_classification(X_test, test_preds).savefig(output_folder + "/TSH_vs_TT4_concentration_test_set", bbox_inches='tight')


    #plot confusion matrix
    ax = plt.subplot(111, frame_on = False)
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    table(ax, pd.DataFrame(confusion_matrix(y_test, test_preds)), rowLabels=['']*pd.DataFrame(confusion_matrix(y_test, test_preds)).shape[0], loc='center')
    plt.savefig(output_folder + "/confusion_matrix.png", bbox_inches="tight")
    pd.DataFrame(confusion_matrix(y_test, test_preds)).to_csv(output_folder + "/confusion_matrix.csv")  

if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="Creates ans saves figures from clean data")
    parse.add_argument("file_path", help = "Path to clean data file")
    parse.add_argument("output_path", help = "Filename to save ")
    
    arg = parse.parse_args()
    main(arg.file_path, arg.output_path)




