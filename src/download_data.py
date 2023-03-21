import os
import urllib.request
import argparse

def main(url, output_path):
    try:
        urllib.request.urlretrieve(url, output_path)
    except urllib.error.HTTPError as error:
        print(f'HTTP Error {error.code} {error.reason}')

if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="Downloads a file based on a URL and saves it to a given file path")
    parse.add_argument("url", help = "URL of the file")
    parse.add_argument("output_path", help = "Path to save the file to")
    arg = parse.parse_args()
    main(arg.url, arg.output_path)