FROM jupyter/scipy-notebook:ubuntu-22.04

RUN conda install seaborn=0.12.2
RUN conda install pytest=7.1.2

USER root

WORKDIR /home/joyvan/dsci-310-group-17
