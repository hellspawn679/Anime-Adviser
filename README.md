### anime-search-engine
### Dependencies

hyppo requires the following:

* [python](https://www.python.org/) (>= 3.6)
* [numba](https://numba.pydata.org/) (>= 0.46)
* [numpy](https://numpy.org/)  (>= 1.17)
* [scipy](https://docs.scipy.org/doc/scipy/reference/) (>= 1.4.0)
* [scikit-learn](https://scikit-learn.org/stable/) (>= 0.22)
* [joblib](https://joblib.readthedocs.io/en/latest/) (>= 0.17.0)
# Overview
This is a anime search engine  which give you top 10 anime recommendation of the chosen anime and the results are based on  cosine similarity.Fortend part of the web page is done using streamlit 
and there is no different backend or fortend code. most of it is written in python and i have also included the datasets that is used to train my model  
1) Installation
2) working
3) dataset
## INSTALL
there are two ways you can install it on you system:-
* you can clone it and run it locally using streamlit 
* you can run it docker container
  # Method 1
clone this repo first 
```
git clone https://github.com/hellspawn679/anime-search-engine.git
cd anime-search-engine
```
now make sure you have all the required modules of python and you have python version (<=3.9 and >=3.7)
```
python -m pip install -r requirements.txt
```
now launch you flask backend 
```
python server.py
```
now change the dir 
```
cd model
```
now simply run streamlit 
```
streamlit run final.py
```
  # Method 2 
if you [docker](https://www.docker.com/) engine in you machine you can simply build up the docker file and use the container 
clone this repo first 
```
git clone https://github.com/hellspawn679/anime-search-engine.git
cd anime-search-engine
```
after cloning it build the docker image 
```
docker compose up --build
```
then go to you
```
http://localhost:8501/
```
