FROM jupyter/scipy-notebook:ubuntu-22.04

RUN conda install --yes -c conda-forge numpy=1.24.2
RUN conda install --yes -c conda-forge matplotlib=3.7.0
RUN conda install --yes -c conda-forge pandas=1.5.3
RUN conda install --yes -c conda-forge scikit-learn=1.2.1
RUN conda install --yes -c conda-forge seaborn=0.12.2
RUN conda install --yes -c conda-forge jupyter-book=0.13.2
