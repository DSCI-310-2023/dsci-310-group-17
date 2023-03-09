# Hyperthyroid Disease Classification
Authors: Arman Moztarzadeh, Eric Liu, Ryan Lee, Matthew Gillies

## About
Hyperthyroidism is an issue that occurs when the thyroid gland makes more thyroid hormones than the body needs (De Leo et al., 2016). The body manages its energy by using thyroid hormones. By having an excessive amount, bodily functions may increase in speed resulting in weight loss, rapid heartbeat, fatigue, shaky hands, sweating, and more (U.S. Department of Health and Human Services, n.d.). The goal of our project is to create a tool to help predict the presence of hyperthyroidism using varying attributes such as age, sex, prior treatment for thyroid disease, and amount of thyroid hormones in the body.

## Report
The full report can be found [here](https://github.com/erliuu/dsci-310-group-17/blob/main/analysis.ipynb)

## Usage
### Method 1 - Running jupyter lab to reproduce analysis without edit permissions
1. Clone this GitHub repository onto your local computer.
2. Ensure that your terminal is in the root of the project.
3. Run the following command:

```
docker run --rm -p 8888:8888 \
    -v /$(pwd):/home/joyvan/dsci-310-group-17 \
    erliuu/dsci-310-group-17:latest \
    jupyter nbconvert --to notebook --execute dsci-310-group-17/analysis.ipynb
```
### Method 2 - Running with jupyter lab interactively with ability to edit project
1. Clone this GitHub repository onto your local computer.
2. Ensure that your terminal is in the root of the project.
3. Run the following command:
```
docker run --rm -p 8888:8888 \
    -v /$(pwd):/home/joyvan/dsci-310-group-17 \
    erliuu/dsci-310-group-17:latest \
```
4. Once you have run the command, copy the URL that will come up that looks something like http://127.0.0.1:8888/lab?token=... into your web browser.
5. You may now run the entire analysis in the file analysis.ipynb.

## Dependencies
R version 4.2.2 & Jupyterlab 3.6.1
Docker Base Image: jupyter/scipy-notebook:ubuntu-22.04

Our list of dependencies with the package and version number can be found below:
| Package  | Version |
| ------------- | ------------- |
| matplotlib  | 3.7.1 |
| numpy  | 1.24.2 |
| pandas  | 1.5 |
| seaborn | 0.12.2 |
| jupyter-book  | 0.14.0 |
| py-test  | 7.2.2 |

## License
This project uses the MIT license for its code and the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0) license for the analysis.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC_BY--NC--ND_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
