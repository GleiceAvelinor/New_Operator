import csv
import os

path = r"c:\Users\ednar\OneDrive\Imagens\recog_system\gesture_dataset.csv"

if os.path.exists(path):
    with open(path, 'r', newline='') as f:
        lines = list(csv.reader(f))
    
    if lines and lines[0][0] != 'target':
        header = ['target']
        for i in range(21):
            header += [f'x{i}', f'y{i}', f'z{i}']
        
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(lines)
        print("✅ Header added to gesture_dataset.csv")
    else:
        print("ℹ️ Header already exists or file is empty")
else:
    print("❌ File not found")
