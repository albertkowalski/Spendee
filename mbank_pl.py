import csv
import re

input_file = "input.csv"
output_file = "output.csv"

category_mapping = {
# Expenses
    # Beauty
    # Bills
    "DEVELOPER": "Bills",
    "PHONE-COMPANY": "Bills",
    # Education
    # Entertainment
    # Food
    # Gifts
    # Healthcare
    # Kids
    "POCKET MONEY": "Kids",
    "ENGLISH LESSONS": "Kids",
    # Other
    # Shopping
    # Transport
    # Vacation 

# Income
    # Extra Income
    # Gifts
    # Salary Agata
    # Salary Albert
    # Social Benefits
    "SOCIAL": "Social Benefits",
    # Sales
}

label_mapping = {
# Expenses
    # Beauty
    # Bills
    "GIARDINI VERONA": "Bills,Home",
    "GIARDINI VERONA GARAŻ": "Garage",
    "GIARDINI VERONA FUNDUSZ REMONTOWY": "Renovation Fund",
    "NJU": "Bills,Phone",
    # Education
    # Entertainment
    # Food
    # Gifts
    # Healthcare
    # Kids
    "KIESZONKOWE": "Kids,Pocket Money",
    "HIFIVE": "Kids,Language Learning",
    # Other
    # Shopping
    # Transport
    # Vacation 

# Income
    # Extra Income
    # Gifts
    # Salary Agata
    # Salary Albert
    # Social Benefits
    "social": "Social Benefits",
    # Sales

}


data_entries = []
with open(input_file, "r", encoding="utf-8-sig") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=';')
    found_data = False
    for row in csv_reader:
        if not row or not row[0].strip():
            continue  
        if row[0].startswith("#Data operacji"):
            found_data = True
            continue
        if found_data and len(row) > 0:
            date = row[0]
            note = row[1]
            note = note.split("PRZELEW")[0].strip()
            amount = row[4]
            category_mapped = next((category for key, category in category_mapping.items() if re.search(fr'\b{re.escape(key)}\b', note, flags=re.IGNORECASE)), "Other")
            labels_matched = ",".join(label for key, label in label_mapping.items() if any(re.search(fr'\b{re.escape(key)}\b', note, flags=re.IGNORECASE) for key in key.split()))
            data_entries.append([category_mapped, date, amount, note, labels_matched])


with open(output_file, "w", encoding="utf-8-sig", newline='') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=';')
    csv_writer.writerow(["Category Name", "Date", "Amount", "Note","Labels"])
    csv_writer.writerows(data_entries)

print("Conversion completed. Output saved to", output_file)
