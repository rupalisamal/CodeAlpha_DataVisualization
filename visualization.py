import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("tested.csv")

print(df['Sex'].value_counts())
sns.set_style("whitegrid")


# Chart 1: Survival Count

plt.figure(figsize=(6,4))
sns.countplot(x="Survived", data=df)
plt.title("Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Number of Passengers")
plt.show()


# Chart 2: Passenger Class Distribution

plt.figure(figsize=(6,4))
sns.countplot(x="Pclass", data=df)
plt.title("Passenger Class Distribution")
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")
plt.show()


# Chart 3: Gender Distribution

plt.figure(figsize=(6,4))
sns.countplot(x="Sex", data=df)
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Passengers")
plt.show()


# Chart 4: Survival Rate by Gender

plt.figure(figsize=(6,4))
sns.barplot(x="Sex", y="Survived", data=df, estimator="mean", errorbar=None)
plt.title("Survival Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Survival Rate")
plt.show()


# Chart 5: Survival Rate by Passenger Class

plt.figure(figsize=(6,4))
sns.barplot(x="Pclass", y="Survived", data=df)
plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.show()


# Chart 6: Survival Rate by Class and Gender (Combined Story)

plt.figure(figsize=(7,5))
sns.barplot(x="Pclass", y="Survived", hue="Sex", data=df, estimator="mean", errorbar=None)
plt.title("Survival Rate by Class and Gender")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.legend(title="Gender")
plt.show()


# Chart 7: Age Distribution by Survival (Box Plot)

plt.figure(figsize=(7,5))
sns.boxplot(x="Survived", y="Age", data=df)
plt.title("Age Distribution by Survival")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Age")
plt.show()


# Chart 8: Fare Distribution by Survival

plt.figure(figsize=(7,5))
sns.boxplot(x="Survived", y="Fare", data=df)
plt.title("Fare Distribution by Survival")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Fare")
plt.show()


# Observations

# 1. Female passengers had a much higher survival rate than male passengers.
# 2. 1st class passengers had the highest survival rate, followed by 2nd and 3rd class.
# 3. Combining class and gender shows that 1st class females had the highest 
#    survival rate, while 3rd class males had the lowest.
# 4. Passengers who survived generally paid higher fares compared to those who did not.
# 5. Age alone did not show a strong pattern with survival, unlike gender, class, and fare.
# Note: This dataset (tested.csv) appears to follow a gender-based survival 
# pattern (all females marked as survived, all males marked as not survived), 
# rather than representing real mixed historical outcomes. This explains why 
# gender shows a perfect correlation with survival in this analysis.