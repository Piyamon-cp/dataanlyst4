Mental Health Survey Analysis

This project performs data cleaning, visualization, and statistical analysis on a mental health survey dataset to explore the relationships between **age**, **mental health treatment**, and **company-provided mental health benefits**.

Project Files

- `data_analysis.py` – Python script for preprocessing, visualization, and hypothesis testing  
- `survey.csv` – Raw survey data (source: [Kaggle Dataset](https://www.kaggle.com/datasets/osmi/mental-health-in-tech-survey))  
- `survey_preprocessed.csv` – Cleaned dataset after filtering and encoding  
- `benefits_graph.png` – Bar chart showing the distribution of mental health benefits  
- `treatment_graph.png` – Bar chart showing the distribution of mental health treatment  

Data Preprocessing Steps

1. **Age filtering** – Keep only entries with `Age` between 10 and 100  
2. **Categorical filtering** – Remove entries with "Don't know" responses in `benefits`  
3. **Encoding**:  
   - `benefits`: Yes → 1, No → 0  
   - `treatment`: Yes → 1, No → 0  
4. **Drop missing values**  

Visualizations

- Boxplots of `Age` before and after filtering  
- Bar Charts for:  
  - Mental health benefits availability  
  - Mental health treatment received  

Statistical Tests

Chi-Square Test
- **Purpose**: Determine if there is a relationship between `treatment` and `benefits`  
- **Result**:  
  - χ² statistic and p-value printed  
  - Significance is checked at α = 0.05  

Independent t-Test
- **Purpose**: Compare average age between those who received treatment and those who didn’t  
- **Result**:  
  - t-statistic and p-value printed  
  - Significance evaluated at α = 0.05  

How to Run

Make sure you have the following Python libraries installed:
```bash
pip install pandas numpy matplotlib seaborn scipy
```

Run the script:
```bash
python data_analysis.py
```

---
