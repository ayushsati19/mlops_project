# Income Prediction API

This project is a machine learning-based API that predicts whether an individual's income exceeds $50K per year based on demographic and employment-related features. The model is trained on the **Adult Census Income Dataset**, which contains information about individuals' age, education, occupation, marital status, and more.

The API is built using **FastAPI** and uses a pre-trained machine learning model (e.g., Gradient Boosting) to make predictions. The model is serialized and loaded using `joblib`.

---

## Table of Contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Running the Application](#running-the-application)
5. [API Endpoints](#api-endpoints)
6. [Input Data Schema](#input-data-schema)
7. [Testing the API](#testing-the-api)
8. [Deployment](#deployment)
9. [Contributing](#contributing)
10. [License](#license)

---

## Features

- **Fast Predictions**: Uses a pre-trained machine learning model for real-time predictions.
- **Scalable**: Built with FastAPI, ensuring high performance and scalability.
- **Robust Validation**: Validates input data to ensure compatibility with the model.
- **Easy Deployment**: Can be deployed locally or on cloud platforms like AWS, GCP, or Azure.

---

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.7 or higher
- Pip (Python package manager)
- Virtual environment tool (optional but recommended)

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/income-prediction-api.git
   cd income-prediction-api
   ```

2. **Set Up a Virtual Environment** (Optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the Pre-trained Model**:
   - Ensure the pre-trained model (`Gradient_Boosting_best_model.pkl`) is available in the root directory of the project.
   - If not, train the model using the provided training script and save it as a `.pkl` file.

---

## Running the Application

1. Start the FastAPI server using Uvicorn:
   ```bash
   uvicorn app:app --reload
   ```

2. Access the API documentation:
   - Open your browser and navigate to:
     - **Swagger UI**: `http://127.0.0.1:8000/docs`
     - **ReDoc**: `http://127.0.0.1:8000/redoc`

---

## API Endpoints

### 1. Health Check
- **URL**: `/health`
- **Method**: `GET`
- **Description**: Checks if the server is running.
- **Response**:
  ```json
  {
    "status": "healthy"
  }
  ```

### 2. Predict Income
- **URL**: `/predict`
- **Method**: `POST`
- **Description**: Predicts whether an individual's income exceeds $50K based on input features.
- **Request Body**:
  ```json
  {
    "age": 39,
    "workclass": "State-gov",
    "fnlwgt": 77516,
    "education": "Bachelors",
    "education_num": 13,
    "marital_status": "Never-married",
    "occupation": "Adm-clerical",
    "relationship": "Not-in-family",
    "race": "White",
    "sex": "Male",
    "capital_gain": 2174,
    "capital_loss": 0,
    "hours_per_week": 40,
    "native_country": "United-States"
  }
  ```
- **Response**:
  ```json
  {
    "prediction": " <=50K"
  }
  ```

---

## Input Data Schema

The API expects input data in JSON format with the following fields:

| Field Name        | Type   | Description                                      |
|--------------------|--------|--------------------------------------------------|
| `age`             | int    | Age of the individual                            |
| `workclass`       | str    | Type of employment (e.g., Private, State-gov)    |
| `fnlwgt`          | int    | Final weight assigned to the individual         |
| `education`       | str    | Highest level of education                      |
| `education_num`   | int    | Numerical representation of education           |
| `marital_status`  | str    | Marital status                                   |
| `occupation`      | str    | Occupation                                       |
| `relationship`    | str    | Relationship within family                      |
| `race`            | str    | Race or ethnicity                                |
| `sex`             | str    | Gender                                           |
| `capital_gain`    | int    | Capital gains earned                             |
| `capital_loss`    | int    | Capital losses incurred                          |
| `hours_per_week`  | int    | Hours worked per week                            |
| `native_country`  | str    | Native country                                   |

---

## Testing the API

1. **Using Swagger UI**:
   - Navigate to `http://127.0.0.1:8000/docs`.
   - Use the interactive interface to test the `/predict` endpoint.

2. **Using Postman**:
   - Create a new POST request to `http://127.0.0.1:8000/predict`.
   - Set the `Content-Type` header to `application/json`.
   - Provide the input data in the request body.

3. **Using cURL**:
   ```bash
   curl -X 'POST' \
     'http://127.0.0.1:8000/predict' \
     -H 'Content-Type: application/json' \
     -d '{
       "age": 39,
       "workclass": "State-gov",
       "fnlwgt": 77516,
       "education": "Bachelors",
       "education_num": 13,
       "marital_status": "Never-married",
       "occupation": "Adm-clerical",
       "relationship": "Not-in-family",
       "race": "White",
       "sex": "Male",
       "capital_gain": 2174,
       "capital_loss": 0,
       "hours_per_week": 40,
       "native_country": "United-States"
     }'
   ```

---

## Deployment

1. **Local Deployment**:
   - Run the server using Uvicorn as described in the [Running the Application](#running-the-application) section.

2. **Cloud Deployment**:
   - Deploy the API on platforms like AWS, GCP, or Azure using containers (Docker) or serverless functions.
   - Example Dockerfile:
     ```dockerfile
     FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
     COPY ./app /app
     RUN pip install -r requirements.txt
     ```

3. **Scaling**:
   - Use tools like **Gunicorn** with multiple workers or deploy behind a reverse proxy (e.g., Nginx).

---

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or feedback, please contact:

- **Email**: ayushsati19@gmail.com
