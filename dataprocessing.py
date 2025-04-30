# data_analysis.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind, chi2_contingency


# ✅ 1. โหลดข้อมูล
df = pd.read_csv(r"C:\Users\Piyamon\OneDrive\Desktop\Keep\data_analyst3\staticcpe203\survey.csv")

# ✅ 2. สร้าง Boxplot ก่อนกรองอายุ (เพื่อดูค่าผิดปกติ)
plt.figure(figsize=(6, 4))
sns.boxplot(x=df["Age"], color="lightblue")
plt.xlabel("Age")
plt.title("Boxplot of Age (Before Filtering)")
plt.show()

# ✅ 2. ทำ Data Preprocessing
df = df[(df["Age"] >= 10) & (df["Age"] <= 100)]  # ลบอายุที่ไม่สมเหตุสมผล
df = df[df["benefits"].isin(["Yes", "No"])]  # ลบ 'Don't know'
df["benefits"] = df["benefits"].map({"Yes": 1, "No": 0})
df["treatment"] = df["treatment"].map({"Yes": 1, "No": 0})  
df_cleaned = df[["Age", "benefits", "treatment"]].dropna()  # ลบ Missing Values

# ✅ 3. บันทึกข้อมูลที่ทำความสะอาดแล้ว
df_cleaned.to_csv("survey_preprocessed.csv", index=False)
print("✅ Data Preprocessing เสร็จสมบูรณ์! ไฟล์ที่ถูกบันทึก: survey_preprocessed.csv")

# ✅ 4. สร้าง Boxplot หลังการกรองอายุ
plt.figure(figsize=(6, 4))
sns.boxplot(x=df_cleaned["Age"], color="lightgreen")
plt.xlabel("Age")
plt.title("Boxplot of Age (After Filtering)")
plt.show()


# ✅ 4. สร้างกราฟ Frequency ของ benefits และ treatment (รูปแบบเดิม)

# 📌 4.1 Bar Chart แสดงความถี่ของ benefits (เหมือนภาพต้นฉบับ)
benefits_frequency = df_cleaned["benefits"].value_counts()
plt.figure(figsize=(6,4))
sns.barplot(x=benefits_frequency.index, y=benefits_frequency.values, palette=["#76A999", "#E78B6F"])
plt.xticks([0, 1], ["No", "Yes"])
plt.xlabel("Benefits Availability")
plt.ylabel("Frequency")
plt.title("Frequency of Mental Health Benefits in Companies")
plt.savefig("benefits_graph.png")  # บันทึกภาพ
plt.show()

# 📌 4.2 Bar Chart แสดงความถี่ของ treatment (เหมือนภาพต้นฉบับ)
treatment_frequency = df_cleaned["treatment"].value_counts()
plt.figure(figsize=(6, 4))
sns.barplot(x=treatment_frequency.index, y=treatment_frequency.values, palette=["#A7C6C6", "#F9F5A6"])
plt.xticks([0, 1], ["No Treatment", "Received Treatment"])
plt.xlabel("Treatment Status")
plt.ylabel("Frequency")
plt.title("Frequency of Mental Health Treatment Received")
plt.savefig("treatment_graph.png")  # บันทึกภาพ
plt.show()



# # ✅7. Chi-Square Test ของตัวแปรเชิงคุณภาพ

# 📌 7.1 Chi-Square Test: Treatment vs Benefits
contingency_table_benefits = pd.crosstab(df_cleaned["treatment"], df_cleaned["benefits"])
chi2_benefits, p_benefits, _, _ = chi2_contingency(contingency_table_benefits)


# ✅ 8. แสดงผลลัพธ์ของ Chi-Square Test
print("\n📊 Chi-Square Test Results:")

print(f"\n📌 Treatment vs Benefits:")
print(f"- Chi-Square Statistic (χ²): {chi2_benefits:.4f}")
print(f"- P-Value: {p_benefits}")
print(f"- Significant: {'✅' if p_benefits < 0.05 else '❌'} (p < 0.05)")

# print(f"\n📌 Treatment vs Age (Grouped):")
# print(f"- Chi-Square Statistic (χ²): {chi2_age:.4f}")
# print(f"- P-Value: {p_age:.4f}")
# print(f"- Significant: {'✅' if p_age < 0.05 else '❌'} (p < 0.05)")


treated = df_cleaned[df_cleaned["treatment"] == 1]["Age"]
not_treated = df_cleaned[df_cleaned["treatment"] == 0]["Age"]

t_stat, p_value_age = ttest_ind(treated, not_treated)

print("\n📌 Age vs Treatment")
print("- t-statistic:", t_stat)
print("- p-value:", p_value_age)
print(f"- Significant: {'✅' if p_benefits < 0.05 else '❌'} (p < 0.05)")

