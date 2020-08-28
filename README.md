## Machine Learning Process for Classification / Regression

### Author: Grejell Segura

### Part 1 - Data Preparation and Visualization
1. Collect raw data
    - if big data then extract only enough sample
2. EDA
3. Visualization
4. Statistical Analysis
    - Test for Dependence/Independence, Regression Analysis, etc.
5. Data Preprocess
    - One Hot Encoding, Label Encoding, etc
    - Scaling, Standardization, Normalization

### Part 2 - Machine Learning Modeling (Do everything in CV)
1. Base Model - Multiple Models
    - LogisticReg, NB, RF, ADA, LGB, XGB, LDA for classification
    - LinearReg, RF, ADA, LGB, XGB for regression
2. Fine Tuning Top Models
3. Improvements
    - Feature Engineering
    - Fine Tuning Again
    - Blending/Stacking/Ensembling Models
    - Optional: DNN
4. Model Selection / Performance Comparison
5. Train final model on full dataset (big data)

### Part 3 - Create API / Prototype Application
1. Create Data Pipeline
2. Create API using Flask/FastAPI
3. Deploy using Docker
4. Optional: Create Prototype using Streamlit

### Part 4 - Create Monitoring / Retraining Pipeline
1. Create Model Score Monitoring
2. Repeat Part 2 if model performance starts declining
