# Hyperthyroid Disease Classification
Authors: Arman Moztarzadeh, Eric Liu, Ryan Lee, Matthew Gillies

## About
Hyperthyroidism is an issue that occurs when the thyroid gland makes more thyroid hormones than the body needs (De Leo et al., 2016). The body manages its energy by using thyroid hormones. By having an excessive amount, bodily functions may increase in speed resulting in weight loss, rapid heartbeat, fatigue, shaky hands, sweating, and more (U.S. Department of Health and Human Services, n.d.). The goal of our project is to create a tool to help predict the presence of hyperthyroidism using varying attributes such as age, sex, prior treatment for thyroid disease, and amount of thyroid hormones in the body.

## Report
The analysis report can be found [here](https://github.com/erliuu/dsci-310-group-17/blob/main/analysis.ipynb)

## Usage
The Docker environment can be built from the provided Dockerfile in this repository or pulled directly from Dockerhub [here](https://hub.docker.com/repository/docker/erliuu/dsci-310-group-17).
```
docker pull erliuu/dsci-310-group-17
docker run -it --rm erliuu/dsci-310-group-17:latest
jupyter lab
```

## Dependencies
Docker Base Image: jupyter/scipy-notebook:ubuntu-22.04

| Package  | Version |
| ------------- | ------------- |
| matplotlib  | 3.7.1 |
| numpy  | 1.24.2 |
| pandas  | 1.5 |
| seaborn | 0.12.2 |
| jupyter-book  | 0.14.0 |
| py-test  | 7.2.2 |

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
