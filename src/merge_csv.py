import argparse
import pandas as pd

def main(file1_path, file2_path, output_path, column_names):
    """
    Merges 2 dataframes together and adds column names 

    Parameters
    ----------
    file1_path: (string) -> file path to first CSV file

    file2_path: (string) -> file path to second CSV file

    output_path: (string) -> Stores the dataframe/csv at this path

    column_names: (string) -> renames columns by these names
    
    Returns
    ----------
    None
    """ 
    columns = (column_names.strip('][').split('.'))[0].split(", ")
    df1 = pd.read_csv(file1_path, names = columns)
    df2 = pd.read_csv(file2_path, names = columns)

    output = pd.concat([df1, df2])

    output.to_csv(output_path, index = False)
    print (columns)

if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="Merges 2 CSV files into 1 based on specific columns")
    parse.add_argument("file1_path", help = "Path to first CSV")
    parse.add_argument("file2_path",  help = "Path to second CSV")
    parse.add_argument("output_path", help = "Path to save the file to")
    parse.add_argument("column_names", help = "List of columns you want to keep when file is merged")
    
    arg = parse.parse_args()
    main(arg.file1_path, arg.file2_path, arg.output_path, arg.column_names)




