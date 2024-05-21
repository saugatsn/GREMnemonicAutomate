import pandas as pd
import webbrowser
import time

# Read the Excel file
file_path = 'names.xlsx'  # Replace with the path to your Excel file
df = pd.read_excel(file_path)

# Extract GRE words from the first column starting from the first row
gre_words = df.iloc[:, 0].tolist()

# Base URL
base_url = "https://mnemonicdictionary.com/word/"

# Open each GRE word in a new browser tab serially
for word in gre_words:
    url = base_url + word
    webbrowser.open_new_tab(url)
    time.sleep(1)  # Add a delay of 1 second (adjust as needed)
