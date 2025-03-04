﻿# ubb-fmi-admission-exam-results

## Requirements
- Python 3.*
- Libraries PyPDF2, re, csv, numpy and matplotlib

```
pip install PyPDF2 numpy matplotlib
```

## Script overview
This Python script extracts text from a PDF containing admission results, processes the data to generate a CSV file, and visualizes the distribution of grades in a histogram. It also computes and displays statistical metrics such as mean, median, standard deviation, minimum, maximum, and the most common grade. By default, the number of bins in the histogram is set to the number of *possible* grades. This can be changed to the number of unique grades by uncommenting line #35 of the script.

## Disclaimer
**Not written to match any other PDF format than the one that comes in this repository, representing the results of the July session for Babes-Bolyai University's Faculty of Mathematics and Computer Science BSc admission exam.**
