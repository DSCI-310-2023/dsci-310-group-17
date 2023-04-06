import argparse
import pandas as pd
import matplotlib.pyplot as plt
import os
from analysis_visualizations import visualize_classification
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.linear_model import LogisticRegression
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.pipeline import make_pipeline
from pandas.plotting import table

def main(input_path, output_folder):
    """
    Creates figures and tabes based on clean data. 
    Stores them at the given output folder

    Parameters
    ----------
    input_path: (string) -> path to clean data

    output_folder: (string) -> path to output folder where figures and tables will be stored
    
    Returns
    ----------
    None
    """
    hyper_clean = pd.read_csv(input_path)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    
    # model training & analysis
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


    # save and plot confusion matrix to png
    cm = confusion_matrix(y_test, test_preds)
    disp = ConfusionMatrixDisplay(cm, display_labels=[True, False]).plot()
    plt.grid(False)
    plt.savefig(output_folder + "/confusion_matrix.png", bbox_inches="tight")
    #save confusion matrix to dataframe/csv
    pd.DataFrame(cm).to_csv(output_folder + "/confusion_matrix.csv")

    # save accuracy score to txt file
    score = accuracy_score(train_preds, y_train)
    f = open(output_folder + '/accuracy_score.txt','w')
    f.write('{}'.format(round(score, 3)))
    f.close()


if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="Creates ans saves figures from clean data")
    parse.add_argument("file_path", help = "Path to clean data file")
    parse.add_argument("output_path", help = "Filename to save ")
    arg = parse.parse_args()
    main(arg.file_path, arg.output_path)




