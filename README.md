# 📊 CodeAlpha - Data Visualization

## 🎯 Internship Task
This project is submitted as part of the **Data Analytics Internship at CodeAlpha**.  
**Task 3: Data Visualization**

## 📌 Objective
To transform raw Titanic passenger data into clear, insightful visualizations that:
- Reveal patterns and relationships in the data
- Support data-driven storytelling around survival outcomes
- Build a strong portfolio of well-designed charts

## 🗂️ Dataset
The dataset used is the **Titanic Dataset** (`tested.csv`), containing information about passengers aboard the Titanic, including their age, gender, passenger class, fare, and survival status.

## 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| Python | Core programming language for analysis |
| Pandas | Data loading and handling |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualizations (bar plots, box plots) |
| VS Code | Development environment |
| GitHub | Version control and project documentation |

## 📈 Visualizations Created

1. **Survival Count** — Overall count of passengers who survived vs. did not survive
2. **Passenger Class Distribution** — Number of passengers in each class (1st, 2nd, 3rd)
3. **Gender Distribution** — Count of male vs. female passengers
4. **Survival Rate by Gender** — Comparing survival rate between male and female passengers
5. **Survival Rate by Passenger Class** — Comparing survival rate across passenger classes
6. **Survival Rate by Class and Gender (Combined)** — Combined view showing how class and gender together relate to survival
7. **Age Distribution by Survival (Box Plot)** — Comparing age spread between survivors and non-survivors
8. **Fare Distribution by Survival (Box Plot)** — Comparing fare spread between survivors and non-survivors

## 📊 Key Observations
1. Female passengers had a much higher survival rate than male passengers.
2. 1st class passengers had the highest survival rate (46.7%), followed by 3rd class (33%) and 2nd class (32.3%).
3. Combining class and gender shows that the same gender-based survival pattern holds across all three passenger classes.
4. Passengers who survived paid a noticeably higher average fare (≈49.7) compared to those who did not survive (≈27.5).
5. Age showed almost no difference between survivors and non-survivors (average age ≈30.3 in both groups), unlike gender, class, and fare.

## ⚠️ Important Note on Dataset
Upon deeper analysis, this dataset (`tested.csv`) was found to follow a strict gender-based survival pattern — every female passenger is marked as survived and every male passenger is marked as not survived, across all classes. This is not representative of the real, mixed historical outcomes of the Titanic disaster, and appears to be a simplified benchmark/prediction file rather than actual passenger outcomes. This explains why gender shows a perfect correlation with survival, and why the class and fare patterns above are largely a side-effect of this underlying gender split.

## ▶️ How to Run
1. Clone this repository
2. Install required libraries:
3. pip install pandas matplotlib seaborn

4. Run the script:

python visualization.py


---
**Internship:** CodeAlpha Data Analytics Internship  
**Task:** Data Visualization
