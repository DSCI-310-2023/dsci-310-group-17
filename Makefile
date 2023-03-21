# Makefile
# DSCI 310 Group 17
# Last Mofiied: March 2023
# Authors: Arman Moztarzadeh, Eric Liu, Ryan Lee, Matthew Gillies

# Description: Makefile that runs the project's scripts and analysis and generates the report
all: data/rawdata.csv data/unclean.csv

#download data
data/rawdata.csv: src/download_data.py
	python3 src/download_data.py http://archive.ics.uci.edu/ml/machine-learning-databases/thyroid-disease/allhyper.data data/raw1.csv
	python3 src/download_data.py http://archive.ics.uci.edu/ml/machine-learning-databases/thyroid-disease/allhyper.test data/raw2.csv
#Merges 2 CSVs together into 1 with appropriate column names
data/unclean.csv: src/merge_csv.py
	python3 src/merge_csv.py data/raw1.csv data/raw2.csv data/unclean.csv "[age, sex, on thyroxine, query on thyroxine, on antithyroid medication, sick, pregnant, thyroid surgery, I131 treatment, query hypothyroid, query hyperthyroid, lithium, goitre, tumor, hypopituitary, psych, TSH measured, TSH, T3 measured, T3, TT4 measured, TT4, T4U measured, T4U, FTI measured, FTI, TBG measured, TBG, referral source, binaryClass]"
#TODO create script that cleans data
#TODO create script that deletes temporary files (data/raw1.csv, data/raw2.csv)

# render report
# doc/hyperthyroidism.md doc/hyperthyroidism.html doc/hyperthyroidism.pdf:
# 	Rscript -e "rmarkdown::render('doc/hyperthyroidism.rmd', c('bookdown::html_document2', 'bookdown::pdf_document2'))"

# clean:
# 		rm -rf data/*.csv
# 		rm -rf results
# 		rm -rf doc/hyperthyroidism.html doc/hyperthyroidism.pdf