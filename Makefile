# Makefile
# DSCI 310 Group 17
# Last Mofiied: March 2023
# Authors: Arman Moztarzadeh, Eric Liu, Ryan Lee, Matthew Gillies

# Description: Makefile that runs the project's scripts and analysis and generates the report



# render report
# doc/hyperthyroidism.md doc/hyperthyroidism.html doc/hyperthyroidism.pdf:
# 	Rscript -e "rmarkdown::render('doc/hyperthyroidism.rmd', c('bookdown::html_document2', 'bookdown::pdf_document2'))"

# clean:
# 		rm -rf data/*.csv
# 		rm -rf results
# 		rm -rf doc/hyperthyroidism.html doc/hyperthyroidism.pdf