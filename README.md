# django-site-Once-Upon-a-Time

## Description
### Introduction
#### Text Analysis  deployed on django framework & Data Intelligence
this site is building using django framework and python language programming as backend
the goal of this work to book and search & review books 
you can in this site search for books in region syria to book it, and for anyone has books he don't want it or he read it to donate it ,he can also see the reviews for each book 
and also show statistics for each aspect 
#### how it works :
1. booking a book :
   - each one can search for a book see reviews 
   - you can't book or comment without register in the site
2. stats for reviews
   - each review divide to 4 aspects 
     - book_info
     - plot_twist
     - character
     - content of book
   - automatically depand on algorithm of atificial inteligence , Sorts the reviews based on each of the above aspects and gives statistics for each aspects in percent




#### LDA model
In natural language processing, the latent Dirichlet allocation (LDA) is a generative statistical model that allows sets of observations to be explained by unobserved groups that explain why some parts of the data are similar.
#### spacy library
 Analyzing and Processing Text With spaCy. spaCy is an open-source natural language processing library for Python. It is designed particularly for production use, and it can help us to build applications that process massive volumes of text efficiently
#### models and examples:
we use mahine learning in this project and we use diferent model in each aspect 
models:
1. linear classification
2. logistic regression
3. random forrest
4. decision tree
5. ridge classifier 
6. support vector machine 
7. XGBoost
8. AdaBoost classifier  

### Requirements


requirements.txt:
```

bleach==3.1.5
blis==0.4.1
catalogue==1.0.0
certifi==2020.6.20
cycler==0.10.0
Django==3.1.1
django-crispy-forms==1.8.1
django-pandas==0.6.1
django-registration==3.1
django-registration-redux==2.7
en-core-web-sm==2.3.1
ipython-genutils==0.2.0
json2html==1.3.0
jsonschema==3.2.0
nltk==3.5
numpy==1.17.3
pandas==1.0.1
Pillow==6.2.1
regex==2020.7.14
requests==2.24.0
scikit-learn==0.22
scipy==1.3.3
seaborn==0.11.0
six==1.13.0
sklearn==0.0
spacy==2.3.2
xgboost==1.2.0

```
### Demo :
this demo for site :
https://drive.google.com/file/d/1lgtuOmuMD7T8Uvde9tWmV5ronN13aCxf/view?usp=sharing

### Known Issues
There are currently no know issues.

### Contributing
This solution crucially depend on django framework and spacy and nltk library.
