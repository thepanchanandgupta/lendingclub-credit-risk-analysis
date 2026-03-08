import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("LendingClub Credit Risk Analytics")

st.write(
"This interactive dashboard explores loan portfolio characteristics and credit risk drivers using the LendingClub dataset."
)

# Load data
df = pd.read_csv("data/loan_sample.csv")

# Default flag
df["default_flag"] = df["loan_status"].str.contains(
    "Charged Off|Default", case=False, na=False
).astype(int)

# Sidebar filters
st.sidebar.header("Filters")

grade = st.sidebar.multiselect(
    "Select Credit Grade",
    options=sorted(df["grade"].unique()),
    default=sorted(df["grade"].unique())
)

df = df[df["grade"].isin(grade)]

# KPIs
st.subheader("Portfolio KPIs")

col1, col2, col3 = st.columns(3)

col1.metric("Total Applications", len(df))
col2.metric("Default Rate", f"{df['default_flag'].mean():.2%}")
col3.metric("Average Interest Rate", f"{df['int_rate'].mean():.2f}%")

# Loan Distribution by Grade
st.subheader("Loan Distribution by Credit Grade")

fig, ax = plt.subplots()
sns.countplot(data=df, x="grade", order=sorted(df["grade"].unique()), ax=ax)
st.pyplot(fig)

# Default Rate by Grade
st.subheader("Default Rate by Credit Grade")

default_rate = df.groupby("grade")["default_flag"].mean()

fig2, ax2 = plt.subplots()
default_rate.plot(kind="bar", ax=ax2)
st.pyplot(fig2)

# Loan Purpose
st.subheader("Top Loan Purposes")

fig3, ax3 = plt.subplots()
df["purpose"].value_counts().head(10).plot(kind="bar", ax=ax3)
st.pyplot(fig3)