import pandas as pd
import os

# Read the CSV file
input_file = '2025-07-01.csv'
output_file = '2025-07-01_reduced.csv'

print(f"Reading {input_file}...")
df = pd.read_csv(input_file)

print(f"Original shape: {df.shape}")
print(f"Original size: {os.path.getsize(input_file) / (1024**2):.2f} MB")

# Calculate target number of rows to stay under 100MB
target_size_mb = 100
current_size_mb = os.path.getsize(input_file) / (1024**2)

if current_size_mb > target_size_mb:
    # Calculate fraction of rows to keep
    fraction = target_size_mb / current_size_mb * 0.8  # 0.8 for safety margin
    target_rows = int(len(df) * fraction)
    
    # Keep first n rows
    df_reduced = df.head(target_rows)
    
    print(f"Reducing to {target_rows} rows...")
    df_reduced.to_csv(output_file, index=False)
    
    print(f"New shape: {df_reduced.shape}")
    print(f"New size: {os.path.getsize(output_file) / (1024**2):.2f} MB")
    print(f"Saved as {output_file}")
else:
    print("File is already under 100MB, no reduction needed.")
