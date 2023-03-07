# Hyperthyroid Disease Classification
Authors: Arman Moztarzadeh, Eric Liu, Ryan Lee, Matthew Gillies

## About
Hyperthyroidism is an issue that occurs when the thyroid gland makes more thyroid hormones than the body needs (De Leo et al., 2016). The body manages its energy by using thyroid hormones. By having an excessive amount, bodily functions may increase in speed resulting in weight loss, rapid heartbeat, fatigue, shaky hands, sweating, and more (U.S. Department of Health and Human Services, n.d.). The goal of our project is to create a tool to help predict the presence of hyperthyroidism using varying attributes such as age, sex, prior treatment for thyroid disease, and amount of thyroid hormones in the body.

## Report
The full report can be found [here](https://github.com/erliuu/dsci-310-group-17/blob/main/analysis.ipynb)

## Usage
### Method 1 - For those that want to run with jupyter lab interactively
1. Clone the GitHub repositry onto your local computer.
2. Navigate to the root of the project directory.
3. In your terminal, run the following command:

```
docker pull erliuu/dsci-310-group-17
docker run -it --rm erliuu/dsci-310-group-17:latest
jupyter lab
```


## Dependencies
- R version 4.2.2 & Jupyterlab 3.6.1
- Docker Base Image: jupyter/scipy-notebook:ubuntu-22.04

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
