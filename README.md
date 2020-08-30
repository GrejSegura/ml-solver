# Work in Progress
## Machine Learning Classification / Regression Process for Production

Disclaimer: This is the process that I follow when doing machine learning from problem framing to production. It is based on my experience and research through out the years. This may vary between structured and unstructured data but the overall structure remains.

### Part 1 - Data Preparation and Visualization
1. Collect raw data
    - Merge, join, union tables.
    - if big data then extract only enough sample
2. EDA
3. Data Preprocess
    - Imputation
    - One Hot Encoding, Label Encoding, etc
    - Split train/test data
    - Scaling, Standardization, Normalization
4. Visualization
5. Optional: Statistical Analysis
    - Test for Dependence/Independence, Regression Analysis, etc.

### Part 2 - Machine Learning Modeling (Do everything in CV)
1. Base Model - Multiple Models
    - LogisticReg, DT, NB, RF, ADA, LGB, XGB, LDA for classification
    - LinearReg, DT, RF, ADA, LGB, XGB, LDA for regression
2. Fine Tuning Top Models
3. Improvements
    - Feature Engineering
    - Fine Tuning Again
    - Blending/Stacking/Ensembling Models
    - Optional: DNN
4. Model Selection / Performance Comparison
5. Train final model on full dataset (big data)

### Part 3 - For Production: Create API / Prototype Application
1. Create Data Pipeline
2. Create API using Flask/FastAPI or deploy to any cloud framework
3. Deploy using Docker
4. Optional: Create Prototype using Streamlit

### Part 4 - Monitor / Retrain
1. Create Model Score Monitoring
2. Repeat Part 2 if model performance starts declining
