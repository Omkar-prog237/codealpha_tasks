🌸 CodeAlpha Iris Flower Classification 🧠

🧠 Overview

This project focuses on classifying iris flowers into three species — Setosa, Versicolor, and Virginica — using supervised machine learning.

The Iris dataset is a classic dataset in data science and is widely used to test classification algorithms. In this project, a Logistic Regression model is trained to predict the species of an iris flower based on its measurements.

The model uses four flower features:

1. Sepal Length

2. Sepal Width

3. Petal Length

4. Petal Width

to predict the flower species.

🎯 Objectives

1. Load and explore the Iris dataset

2. Perform data preprocessing and cleaning

3. Encode categorical labels into numeric form

4. Train a classification model

5. Evaluate model performance

6. Save the trained model for reuse

🛠️ Technologies Used

1. Python

2. Pandas – Data handling & preprocessing

3. NumPy – Numerical operations

4. Matplotlib – Basic visualization

5. Scikit-learn – Machine learning algorithms

6. Pickle – Model saving

📂 Dataset

Dataset Name: Iris Dataset

Features:

*SepalLengthCm*

*SepalWidthCm*

*PetalLengthCm*

*PetalWidthCm*

*Species* (Target Variable)

🔍 Data Analysis & Preprocessing

The following steps were performed:

✅ Loaded dataset using Pandas

✅ Removed unnecessary column (Id)

✅ Checked class distribution using value_counts()

✅ Generated statistical summary using describe()

✅ Checked for missing values using isnull()

✅ Verified duplicate records

✅ Encoded species labels into numeric form using LabelEncoder

✅ Dropped original species column after encoding

✅ Split dataset into features (X) and target (y)

✅ Applied train-test split (80/20)

🤖 Model Building

A Logistic Regression classifier was used.

Steps:

1. Imported LogisticRegression from sklearn

2. Trained model on training data

3. Predicted species on test data

4. Compared predictions with actual values

📊 Model Evaluation

Model performance was evaluated using:

1. Accuracy Score

2. Classification Report (Precision, Recall, F1-score)

The model achieved high accuracy, showing strong ability to distinguish between flower species.

📈 Results

1. Logistic Regression performed very well on the dataset

2. Clear separation between species improved accuracy

3. Petal measurements were highly influential in classification

4. The model can reliably classify iris species

👨‍💻 Author

**Omkar Bansode**

AI & Data Science Student | ML Enthusiast
