import pandas as pd

# Read from TSV (tab-separated)
url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
df = pd.read_csv(url, sep='\t', header=None, names=['label', 'message'])

# Save it as proper CSV
df.to_csv("spam.csv", index=False)
print("✅ spam.csv created successfully!")
