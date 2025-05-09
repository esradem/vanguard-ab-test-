# Vanguard A/B Test Analysis

## 📊 Overview
This project analyzes the results of a digital A/B test conducted by Vanguard, a US-based investment management company. The experiment aimed to evaluate whether a redesigned user interface (UI) improved the process completion rate among clients.

## 🔍 Objective
Determine whether the new UI led to:
- Higher completion rates
- Statistically significant improvements
- Justifiable changes based on cost-effectiveness (≥ 5% improvement)

## 📁 Data Sources
- `df_final_experiment_clients.txt`: Experiment group assignment (Test vs Control)
- `df_final_demo.txt`: Client demographic and account data
- `df_final_web_data_pt_1.txt` and `df_final_web_data_pt_2.txt`: Clickstream data detailing process steps

## 🧹 Data Preparation
- Merged the three datasets on `client_id`
- Identified process completion by detecting the final `process_step` per client
- Filtered for valid gender values (M, F) and removed duplicates
- Created derived columns: `completed`, `Variation`, and demographic summaries

## 📈 Exploratory Data Analysis (EDA)
- Analyzed client age, gender, tenure, and interaction behavior
- Explored process completion patterns across groups
- Identified drop-off points in the digital funnel

## 🧪 Hypothesis Testing
1. **Test vs Control Completion Rates** (Z-test): Test group had significantly higher completion rate.
2. **Cost-Effectiveness Threshold**: Improvement exceeded 5%, justifying redesign costs.
3. **Age Differences** (T-test): No significant age difference between groups.
4. **Gender Completion Differences** (Chi-Square Test): No significant relationship between gender and completion.
5. **Group-specific Gender Differences**: Analyzed using Chi-Square tests within each group.

## 📊 Visualizations
- Completion rate bar charts by group, age, and gender
- Funnel step drop-off visualization
- Tableau dashboards for interactive filtering and demographic insights

## 📌 Conclusion
The data supports rolling out the new UI due to a statistically and practically significant improvement in completion rates. No demographic biases were detected, and further improvements are recommended using post-rollout behavioral feedback.

## 🛠 Tools Used
- Python (Pandas, NumPy, Matplotlib, Seaborn, SciPy)
- Jupyter Notebook
- Tableau
- Git & GitHub

## 📁 Repository Structure
- `Project_Week5_cleaning.ipynb`: Main analysis notebook
- `README.md`: Project overview and documentation
- Tableau file (`.twbx`) for dashboards
- Supporting data files (hosted externally via URL)

## 🚀 How to Run
1. Clone this repository
2. Install required Python libraries
3. Open the notebook and run cells in sequence
4. Load the Tableau workbook to explore dashboards

---

© 2025 | Created for the Module 2 Data Analysis Project
