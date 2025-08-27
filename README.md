# Student Exam Performance Predictor Model

## Summary + Demonstration Use

##### The Goal of this project was to design a machine learning model that can take a data structure, like a csv, and be trained to predict a value within the csv. Currently, the model has taken 'stud.csv', stored in notebook/data and can predict values for "math_score".
##### To run this model, from the mlproject directory, run "python app.py" and open one of the links provided in the terminal in your local browser. Afterwards, navigate to the "Prediction" page, and input the values given, and the model will predict an appropriate "math_score".


## Going into detail

##### Within the src directory are 3 .py files, exception, logger, and utils, as well as 2 more directories. The exception and logger files contain utility functions, that provide more information when testing my code. The utils file contains functions used in training the model and saving the trained model.

##### Within the first directory, components, is the brunt of the code designed to train the model. The data_ingestion file is responsible for reading the data structure and splitting it into a train and test set, and then storing them within the artifact folder. The data_transformation file is responsible for preparing the data further, and providing a more direct form of the test and train data for the model. Finally, the model_trainer file trains the model using various processes and settles on the one with the highest accuracy.
##### Running python src/components/data_ingestion.py retrains the model and prints the accuracy score chosen.

##### Within the second directory, pipeline, is predict_pipeline.py. This file designs a pipeline that, given input values can predict the target value using the trained model.

##### Outside of the src directory is app.py, which displays the html page through which users can interact with the model to receive predictions.