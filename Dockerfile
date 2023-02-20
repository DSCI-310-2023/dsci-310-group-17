FROM jupyter/scipy-notebook:ubuntu-22.04

RUN conda install seaborn=0.12.2
