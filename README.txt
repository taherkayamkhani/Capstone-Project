# PCAM ZC321-C3-CAPSTONE PROJECT - G21
capstone project


# NLP system for creating Relevant Question and Answer based on job role

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)]()

## Problem Statement.

Due to different reasons like lack of domain knowledge, experience, preparation time etc., many a times the questions asked to evaluate the candidate are not useful to understand his/her capabilities.

An AI based approach will provide level wise list of question and answers which will help the interviewer to assess the applicant better than traditional approach.

## Objective
Implement an NLP system to recommend the relevant questions and their standard answers based on role and experience.
- Data set should be created for various job descriptions from various domains like Information Technology, Engineering, Accounting, Architecture, Automobile and Electrical etc., and creates Tags such as Skills, responsibility and department using Name Entity Recognition model and manually filter the required tags.
- Once this dataset is ready, Different models will be trained such as Spacy, BERT and LSTM.
- Once this training is completed, after that if we test the model with some new JD, then it will identify responsibility and role from that JD based on context also, and then it will find similarity of that responsibility with the one available in metadata then accordingly.
- Model will be trained on question and answers from various tags like Skills, responsibility and department from various domains
-  Model will respond back with the  relevant Question and Answers based on the given Tag(s), which will help the interviewer to assess the applicant better than traditional approach.


## Architecture

<img src="static/Architecture.png" width="700" height="400" />

## Technologies Used

- Python
- Jupyter Notebook
- Fast API
- HTML, CSS
- ML Libraries  [Spacy, Tensorflow, Keras,  SimpleTransformers, Beautiful Soup, NLTK and Selenium driver]

## Models Trained
- Spacy
- BERT
- LSTM

## Data Description

### 
| Features | Description |
| --- | --- |
| domain | Job postings in different sectors |
| title | Job work title |
| salary | Job salary in range |
| experience | Experience required to apply the job |
| skills | key skill required for job |
| location | Job Location |
| functional_area | Functional role for job |
| description | Job Description |
| role_category |  Role Categor |


## Installation

Install the dependencies and start the Flask server.

```sh
pip install -r requirements.txt
```

## Runbook

Run the QA_FastAPI.ipynb from jupyter notebook to start the  FAST API endpoint service

<img src="static/FastAPI.gif" width="700" height="400" />

 Run the Python UI.py file in command line to start the Flask server
```sh
> python UI.py
```

## Model Output

<img src="static/NER.png" width="600" height="25" />


## Model Evaluation

Below are the most commonly used evaluation metrics for NER systems

<img src="static/Peformance.PNG" width="300" height="200" />

In this experiment, we compare the performance of Spacy, BERT and LSTM models. The results of this work indicates that the SPACY extraction method is the best choice.

## Demo
<img src="static/Demo.gif" width="700" height="400" />
