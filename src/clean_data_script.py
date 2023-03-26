import argparse
import pandas as pd
import numpy as np
from clean_data import relabel_bclass, col_dtype_reformat

def main(file_path, output_path):
    df = pd.read_csv(file_path)
    df = relabel_bclass(df)

    #i think this line is useless?
    df.binaryClass.unique().tolist()

    hyperthyroid = df.replace("?", np.nan)

    hyper = hyperthyroid.drop(columns=["TBG", "TBG measured", "T3", "T3 measured", "TSH measured",
                                   "TT4 measured", "FTI measured", "T4U measured", "referral source"])
    hyper_clean = hyper.dropna()
    num_cols = ['age', 'TSH', 'TT4', 'T4U', 'FTI']
    cat_cols = ['sex', 'on thyroxine', 'query on thyroxine', 'on antithyroid medication',
            'sick', 'pregnant', 'thyroid surgery', 'I131 treatment', 'query hypothyroid',
            'query hyperthyroid', 'lithium', 'goitre', 'tumor', 'psych', 'binaryClass', 'hypopituitary']
    hyper_clean = col_dtype_reformat(num_cols, cat_cols, hyper_clean)
    hyper_clean['binaryClass'] = hyper_clean['binaryClass'].replace(["N", "P"], [1, 0])
    
    hyper_clean.to_csv(output_path)




if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="Cleans data ans saves it to a CSV")
    parse.add_argument("file_path", help = "Path to unclean CSV file")
    parse.add_argument("output_path", help = "Path to save clean CSV file to")
    
    arg = parse.parse_args()
    main(arg.file_path, arg.output_path)




