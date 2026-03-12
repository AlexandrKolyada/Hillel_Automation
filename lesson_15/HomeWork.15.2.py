import os
import csv
from os import write

path = 'ideas_for_test/work_with_csv'
file1 = os.path.join(path, 'random-michaels.csv')
file2 = os.path.join(path, 'random.csv')

unique_rows = set()

for file_path in [file1, file2]:
    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            unique_rows.add(tuple(row))


output_file = 'result_kolyada.csv'
with open(output_file, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(unique_rows)

print(f"Done. Result in file - {output_file}")