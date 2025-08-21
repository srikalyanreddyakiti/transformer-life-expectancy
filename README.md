# Transformer Life Expectancy Prediction

This project is about predicting how long a power transformer will keep working before it needs repair or replacement. By looking at things like temperature, current, and oil condition, we calculate a **health score** (called the Transformer Health Index) and then use machine learning to estimate how much life is left.  

- Uses both real and simulated data from transformers  
- Calculates a health score based on temperature, current, and oil levels  
- Trains models to predict how much longer a transformer will last  
- Can generate its own test data when real data is not available  

---

## Health Index Formula

```
Health Index = (0.2 × TR) + (0.2 × TY) + (0.2 × TB) + 
               (0.15 × IR) + (0.15 × IY) + (0.1 × IB) + (0.1 × TO)
```

In simple terms, this formula takes measurements (like temperatures and currents), gives each one a weight depending on how important it is, and combines them into a single score between 0 and 1.  

---

## Features

- Creates sample transformer data when real data is missing  
- Calculates a single health score for each transformer  
- Uses machine learning to predict when a transformer might fail  
- Includes scripts for testing, training, and running the model  
- Can be expanded for use in real-time monitoring systems  

---

## Files

- `Generate data set.py`: Makes synthetic (fake but realistic) transformer data  
- `Transformer age prediction.py`: Main script to predict transformer age/life  
- `Transformer age prediction 2.py`: Another version of the prediction script  
- `Life expectancy.py`: Extra calculations for predicting life span  
- `final.py`: Full pipeline combining all steps together  
- `Transformer code`, `Transformer code 1/2.py`: Helper scripts for health index  
- `TRANSFORMER HEALTH INDEX.pdf`, `Transformer Health Index Monitoring Formula - report.pdf`: Documentation explaining the formula and approach  

---

## Tech Stack

- Python (main programming language)  
- NumPy, pandas (for handling data)  
- scikit-learn (for machine learning)  
- matplotlib, seaborn (for graphs and charts)  
- Jupyter Notebook (for testing and analysis)  

---

## Parameters Monitored

- TR: Temperature at R phase  
- TY: Temperature at Y phase  
- TB: Temperature at B phase  
- IR: Current at R phase  
- IY: Current at Y phase  
- IB: Current at B phase  
- TO: Transformer oil temperature  
- Extra factors: outside temperature and load (optional)  

---

## Author

**Sri Kalyan Reddy Akiti**  
Data Science and Artificial Intelligence  
