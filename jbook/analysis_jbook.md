---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.4
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Analysis

+++ {"user_expressions": []}

```{tableofcontents}
```


+++

## Summary
In this report, we trained a classifier to predict the presence of hyperthyroidism using varying attributes such as age, sex, prior treatment for thyroid disease, and amount of thyroid hormones in the body. Our classifier has a 98% accuracy rate on the test set.

+++

## Introduction
The **Thyroid Disease dataset** obtained from the **UCI Machine Learning Repository** will be used to predict the presence of hyperthyroidism. Hyperthyroidism is an issue that occurs when the thyroid gland produces an excess amount of thyroid hormones (De Leo et al., 2016). As a result, the body's metabolism greatly "speeds up", resulting in weight loss, rapid heartbeat, fatigue, shaky hands, sweating, and more (U.S. Department of Health and Human Services, n.d.). 
<br>
Studies have shown that within the population, certain groups are more predisposed to getting hyperthyroidism. Hyperthyroidism is more common in women, women who were recently pregnant, those with type 1 or type 2 diabetes, alongside other factors (Allahabadia, 2000). In order to help predict whether someone has hyperthyroidism, we are using 19 attributes provided from the Thyroid Disease dataset. The attributes we are using are age, sex, if they take medication for thyroid disease (thyroxine or antithyroid medication), pregnant status, prior treatment for thyroid disease (thyroid surgery or Ii131 radiotherapy for hyperthyroidism), and amount of different hormones in the body (TSH, TT4, T4U, and FTI). **With these factors, we are hoping to make an accurate classifier in to predict whether or not someone has hyperthyroidism.**

+++

## Methods and Results

+++

### Data-Cleaning
To begin this analysis we read in the data from the original source, merging **solely** for pre-processing. The `binaryClass` feature is manipulated so that all values are either positive or negative, removing all other diagnoses. Next, we replaced all `?` values with `NaN` values, and removed all columns that were irrelevant to our classification model or had an extremely large amount of `NaN` values. We then remove all of the remaining rows with NA values from the data set. Since all of the columns are of datatype `Object`, they are converted to their respective data-types (either numeric or categorical). Following this we converted the `binaryClass` column from character values ("P" and "N") to the reverse in boolean integer values ("0" and "1" respectively) to match the classification model. In this data set positive labels actually represented a negative diagnosis.

<br>
### Exploratory Data Analysis
After data-cleaning we preformed exploratory data analysis (EDA) through summary statistics, correlations of numeric features, and value counts for the entire data set.

We get the following column descriptions and information from the data:
```
Data columns (total 21 columns):
 #   Column                     Non-Null Count  Dtype   
---  ------                     --------------  -----   
 0   age                        3085 non-null   float64 
 1   sex                        3085 non-null   category
 2   on thyroxine               3085 non-null   category
 3   query on thyroxine         3085 non-null   category
 4   on antithyroid medication  3085 non-null   category
 5   sick                       3085 non-null   category
 6   pregnant                   3085 non-null   category
 7   thyroid surgery            3085 non-null   category
 8   I131 treatment             3085 non-null   category
 9   query hypothyroid          3085 non-null   category
 10  query hyperthyroid         3085 non-null   category
 11  lithium                    3085 non-null   category
 12  goitre                     3085 non-null   category
 13  tumor                      3085 non-null   category
 14  hypopituitary              3085 non-null   category
 15  psych                      3085 non-null   category
 16  TSH                        3085 non-null   float64 
 17  TT4                        3085 non-null   float64 
 18  T4U                        3085 non-null   float64 
 19  FTI                        3085 non-null   float64 
 20  binaryClass                3085 non-null   category
```
```
                age          TSH          TT4          T4U         FTI
count  3085.000000  3085.000000  3085.000000  3085.000000  3085.00000
mean     52.821718     4.982172   108.694814     0.995246   110.31154
std      20.099428    23.975905    35.763281     0.194844    32.79471
min       1.000000     0.005000     2.000000     0.250000     2.00000
25%      37.000000     0.480000    88.000000     0.880000    93.00000
50%      55.000000     1.300000   104.000000     0.980000   107.00000
75%      68.000000     2.600000   125.000000     1.080000   124.00000
max     455.000000   530.000000   430.000000     2.320000   395.00000
 
```

+++

:::{figure-md} correlation
<img src="../results/correlation_of_numeric_features.png" width = "500px" height = "300px">

Correlation of Numeric Features
:::

+++

<br>
### Model Training
We split the data into training and testing set with a 70/30 split, while also separating the `binaryClass` feature (**target**) from the rest of the data set. Following this a `ColumnTransformer` was created to scale all numeric variables and one-hot-encode all categorical variables to ensure they are in a state that the model can process. The `ColumnTransformer` was then fitted and transformed on the training set, along with transforming the test set. We then performed cross-validation with a LogisticRegression model on the training data, which returned an average validation score of 98%. Applying the model again to the full training set, we again produced a 98% accuracy score. Furthermote, we visualized the training predictions with `TSH` and `TT4` concentrations on the x and y axes respectively. Finally, **The model was applied to the test set, which produced a 99% accuracy**.

+++

:::{figure-md} TSH-vs-TT4-train
<img src="../results/TSH_vs_TT4_concentration_training_set.png" width = "500px" height = "500px">

TSH vs TT4 concentration with classified points for the training set
:::

+++

:::{figure-md} TSH-vs-TT4-test
<img src="../results/TSH_vs_TT4_concentration_test_set.png" width = "500px" height = "500px">

TSH vs TT4 concentration with classified points for the test set
:::

Another plot visualizing the class predictions were created along with a confusion matrix to realize the impact of the predictions. From the confusion matrix we can see that most of our incorrect predictions are false negatives, which are not preferable as an incorrect positive disease diagnose would have less consequential impact than an incorrectly predicting some as disease free.

+++

:::{figure-md} confusion-matrix
<img src="../results/confusion_matrix.png" width = "400px" height = "400px">

Confusion Matrix for the classifier with 0 as negative and 1 as positive
:::

+++ {"user_expressions": []}

## Discussion
The model we trained has a 98% accuracy when tested on a test set. As we were provided by a plethora of measurements specific to thyroid hormones tied to hyperthyroidism, we expected to be able to train a classifier with a high level of accuracy. We believe that this model could act as a further test to backup a doctor's medical opinion for hyperthyroidism. Additionally, due to the lower analysis cost of prediction, this could potentially be an easy resource for people to self-test for the disease. Currently, there are at-home thyroid tests you can administer to measure thyroid hormone levels. By lowering the barrier of entry, more potential hyperthyroidism patients can detect their diseases early on instead of waiting for a medical appointment. A future project could be to model hyperthyroidism disease progression over time. Thyroid hormone levels exist on a spectrum, and simply saying someone has hyperthyroidism or hypothyroidism is severely oversimplifying the disease. Additionally, other projects could look if the dataset holds out in a modern setting. The dataset was published in 1987 and it has been studied that hyperthyroidism increased between 1987 and 1995 due to an increase in salt in food {cite}`Mostbeck et al., 1998`.

+++

## Bibliography

+++ {"user_expressions": []}

```{bibliography}
```



