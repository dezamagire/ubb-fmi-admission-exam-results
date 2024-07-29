import PyPDF2
import re
import csv
import numpy as np
import matplotlib.pyplot as plt

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(reader.pages.__len__()):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

pdf_path = "rez.pdf"
text = extract_text_from_pdf(pdf_path)

pattern = re.compile(r'(\d+)\s+(\d+)\s+(\w+)\s+(\d+\.\d+)')
matches = pattern.findall(text)

csv_file_path = "admission_results.csv"
matches.sort(key=lambda x: float(x[3]), reverse=True)

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Nr. crt.', 'Legitimație', 'Disciplina', 'Nota'])
    for match in matches:
        writer.writerow(match)

grades = [float(match[3]) for match in matches]

num_bins = 1000
# uncomment this to set the number of bins to the number of unique grades (removes empty bins from the histogram) 
# num_bins = len(np.unique(grades))

plt.hist(grades, bins=num_bins)
plt.xlabel('Grade')
plt.ylabel('Frequency')
plt.title('Histogram of grades')

grades = np.array(grades)
mean = np.mean(grades)
median = np.median(grades)
std = np.std(grades)
min_grade = np.min(grades)
max_grade = np.max(grades)
most_common_grade = np.bincount((grades * 100).astype(int)).argmax() / 100

plt.text(0.95, 0.95, f"Mean: {mean:.2f}", ha='right', va='top', transform=plt.gca().transAxes)
plt.text(0.95, 0.90, f"Median: {median:.2f}", ha='right', va='top', transform=plt.gca().transAxes)
plt.text(0.95, 0.85, f"Std: {std:.2f}", ha='right', va='top', transform=plt.gca().transAxes)
plt.text(0.95, 0.80, f"Min: {min_grade:.2f}", ha='right', va='top', transform=plt.gca().transAxes)
plt.text(0.95, 0.75, f"Max: {max_grade:.2f}", ha='right', va='top', transform=plt.gca().transAxes)
plt.text(0.95, 0.70, f"Most common: {most_common_grade:.2f}", ha='right', va='top', transform=plt.gca().transAxes)

plt.show()