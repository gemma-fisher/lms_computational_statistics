import numpy as np
import pandas as pd

# Reproducibility
np.random.seed(42)

# Parameters
n_genes = 500
genes = [f"gene_{i:04d}" for i in range(1, n_genes + 1)]

# Generate expression values
control_expr  = np.random.normal(5.0, 2, n_genes)
mutant1_expr  = np.random.normal(5.02, 2, n_genes)
mutant2_expr  = np.random.normal(6.0, 2, n_genes)

# Create dataframes
df_control = pd.DataFrame({
    "gene_name": genes,
    "avg_expression": control_expr
})

df_mutant1 = pd.DataFrame({
    "gene_name": genes,
    "avg_expression": mutant1_expr
})

df_mutant2 = pd.DataFrame({
    "gene_name": genes,
    "avg_expression": mutant2_expr
})

# Save to CSV
df_control.to_csv("exp_control.csv", index=False)
df_mutant1.to_csv("exp_mutant1.csv", index=False)
df_mutant2.to_csv("exp_mutant2.csv", index=False)

print("CSV files generated:")
print(" - exp_control.csv")
print(" - exp_mutant1.csv")
print(" - exp_mutant2.csv")
