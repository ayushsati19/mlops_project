MLOps Final Project: 

Assignment Requirements
1. Dataset Selection
●	Task: Datasets to be shared with participants.
2. Dataset Schema and Storage
●	Task: Define the dataset schema and store it in Parquet format.
●	Implementation:
o	Define the feature types (e.g., numerical, categorical) and constraints (e.g., allowed values, nullability).
3. Profiling the Dataset
●	Task: Generate a profile report of the dataset.
●	Tools: Use the pandas_profiling or ydata-profiling library to create a data profile report.
4. Train-Test Split
●	Task: Split the dataset into three parts: Training, Test and Production
o	Save the datasets as a Parquet file.
●	Requirements:
o	Example 60-20-20 split for training, test and production.
o	Ensure reproducibility by setting a random seed.
5. Data Version Control
●	Task: 
o	Create a github repo with a datasets directory and store all datasets (train, test and prod in parquet format) and the original dataset (csv or json format)
o	Version control the dataset and related files using GitHub to read and write from the GitHub.
●	Requirements:
o	Push the Parquet file, profiling report, and the original dataset to GitHub.
o	Use meaningful commit messages and organize the repository well.
6. ML Pipeline with Scikit-Learn
●	Task: Read the dataset from GitHub and create an ML pipeline using scikit-learn.
●	The pipeline should contain the transformation for fields like scaling, encoding, imputation etc.
●	Requirements:
o	Use GitHub raw file links to load the dataset into your notebook.
o	Build a data pre-processing and model pipeline.
7. ML Experimentation and Tracking with MLflow/Weights and Biases
●	Read the train and test sets from the github
●	Run at least 5 ML experiments and track them using MLflow/WB. 
o	These experiments can include trying different algorithms (e.g., Linear Regression, Decision Trees), modifying hyperparameters (e.g., max depth, criteria), or experimenting with different data transformations (e.g., scaling, encoding). Each experiment should be logged with MLflow/WB for tracking purposes.
●	Evaluate the models using k-fold cross-validation to ensure that the model generalizes well to unseen data.
●	Evaluate the model against the test set
●	Requirements:
o	Track all information about the model in the experiment tracking tool including k-fold evaluation metrics, and test evaluation metrics, hyperparameters, if any, and data transformations for each experiment.
o	Log the models to MLflow for versioning and future reference.
8. Model Deployment Using FastAPI
●	Task: Deploy the model as an endpoint using FastAPI.
●	Requirements:
o	Load the best model from MLflow.
o	Create a RESTful API using FastAPI to serve predictions which takes the input as a json and returns the predictions also as a json, if possible.
9. User Interface Development with Streamlit or Gradio
●	Task: Create a UI for the ML application using Streamlit or Gradio.
●	Requirements:
o	The UI should allow users to input data for all features and get predictions from the FastAPI endpoint.
o	Use the appropriate UI fields for creating the UI
o	It should display appropriate messages and results based on the inputs.
10. Model Monitoring
●	Task: Conduct a data drift analysis between train and prod data.
●	Requirements:
o	Use alibi-detect library
o	Print the test details in tabular format
![image](https://github.com/user-attachments/assets/41558186-9666-4e75-b7d9-3a1d47bd2334)
