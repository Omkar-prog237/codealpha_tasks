#🚗 CodeAlpha Car Price Prediction 💰#

🧠 Overview

This project focuses on predicting the selling price of used cars using supervised machine learning. The goal is to estimate a car’s market value based on its specifications and condition.

The model analyzes features such as:

1. Car brand

2. Year of manufacture

3. Kilometers driven

4. Fuel type

5. Seller type

6. Transmission

7. Owner history

8. Mileage

9. Engine capacity

10. Max power

11. Number of seats

This project demonstrates real-world regression modeling and data preprocessing techniques.

🎯 Objectives

1. Load and explore the car dataset

2. Clean and preprocess raw data

3. Convert categorical features into numerical values

4. Train a machine learning model for price prediction

5. Evaluate model performance

6. Save the trained model for future use

🛠️ Technologies Used

1. Python

2. Pandas – Data handling & preprocessing

3. NumPy – Numerical operations

4. Scikit-learn – Model building

5. Pickle – Model saving

📂 Dataset

Dataset Name: CarDetails Dataset

Features Used:

1. *name*

2. *year*

3. *selling_price*

4. *km_driven*

5. *fuel*

6. *seller_type*

7. *transmission*

8. *owner*

9. *mileage*

10. *engine*

11. *max_power*

12. *seats*

🔍 Data Analysis & Preprocessing

The following preprocessing steps were performed:

✅ Removed unnecessary column (torque)

✅ Handled missing values using dropna()

✅ Removed duplicate records

✅ Extracted brand name from car name

✅ Cleaned numerical text columns (mileage, engine, max_power)

✅ Converted categorical data to numeric using label replacement

1. Fuel type encoded

2. Seller type encoded

3. Transmission encoded

4. Owner type encoded

5. Brand names encoded numerically

✅ Reset dataset index

✅ Split dataset into training and testing sets (80/20)

📊 Model Evaluation

The model predicts selling prices based on car features.

Linear Regression provides a strong baseline for regression problems like price estimation.

Performance depends on:

1. Quality of feature encoding

2. Data cleanliness

3. Real-world variability in car prices

📈 Results

Model successfully predicts car selling prices

Important factors influencing price:

1. Car brand

2. Year

3. Kilometers driven

4. Engine & power

The system can estimate realistic used-car prices

👨‍💻 Author

*Omkar Bansode*

AI & Data Science Student | ML Enthusiast
