import pandas as pd

print("Loading dataset...")

# Load dataset
df = pd.read_csv("data/loan.csv")

print("Creating sample dataset...")

# Create smaller sample
sample = df.sample(n=50000, random_state=42)

# Save sample
sample.to_csv("data/loan_sample.csv", index=False)

print("Sample dataset created successfully.")