# ⚡ Transformer Life Expectancy Prediction

This project predicts the remaining useful life (RUL) of power transformers using a combination of machine learning techniques and domain-specific health index formulas. The system monitors key electrical and thermal parameters to compute a Transformer Health Index and forecasts potential failure or maintenance needs. This work supports predictive maintenance, operational efficiency, and cost savings in the energy sector.

Transformers are critical to power grids and their failure can result in major disruptions. This project models the aging and health of transformers by:

- Using real and simulated condition-monitoring data
- Calculating a Transformer Health Index based on weighted parameters (temperature, current, oil condition)
- Training regression models to predict remaining life
- Generating synthetic datasets when real data is limited

Health Index Formula:
> Health Index = (0.2 × TR) + (0.2 × TY) + (0.2 × TB) + (0.15 × IR) + (0.15 × IY) + (0.1 × IB) + (0.1 × TO)  
Where each parameter is normalized and weighted based on operational importance.

## 🛠️ Features

- Custom dataset generation for transformer parameters  
- Calculates normalized health scores for each metric  
- Machine learning models (regression-based) for predicting age or failure risk  
- Modular scripts for simulation, training, and evaluation  
- Scalable and ready for real-time monitoring systems  

## 📁 Files

- `Generate data set.py`: Script to generate synthetic transformer data  
- `Transformer age prediction.py`: Core model for predicting age based on indicators  
- `Transformer age prediction 2.py`: Variation or extended version of the model  
- `Life expectancy.py`: Additional calculations for RUL  
- `final.py`: Final pipeline combining all steps  
- `Transformer code`, `Transformer code 1/2.py`: Support modules and health index calculations  
- `TRANSFORMER HEALTH INDEX.pdf`, `Transformer Health Index Monitoring Formula - report.pdf`: Project documentation and mathematical basis  

## 💻 Tech Stack

- Python  
- NumPy, pandas  
- scikit-learn  
- matplotlib / seaborn  
- Jupyter Notebook (optional for testing)

## 📈 Parameters Monitored

- TR: Temperature at R phase  
- TY: Temperature at Y phase  
- TB: Temperature at B phase  
- IR: Current at R phase  
- IY: Current at Y phase  
- IB: Current at B phase  
- TO: Transformer oil temperature  
- Ambient conditions & load factors (optional)

## ✍️ Author

**Sri Kalyan Reddy Akiti**  
Data Science and Artificial Intelligence  
