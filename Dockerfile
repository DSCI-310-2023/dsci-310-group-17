# Group 17 Dockerfile
FROM docker pull jupyter/scipy-notebook{Need to get ID}

RUN conda install --yes -c conda-forge r-numpy=1.24.2
RUN conda install --yes -c conda-forge r-matplotlib=3.7.0
RUN conda install --yes -c conda-forge r-pandas=1.5.3
RUN conda install --yes -c conda-forge r-scikit-lear=1.2.1
RUN conda install --yes -c conda-forge r-seaborn=0.12.2
RUN conda install --yes -c conda-forge r-jupyter-book=0.13.2
