import csv

class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("Loading data...")
        try:
            with open(self.filename, mode='r', encoding='utf-8-sig') as f:
                self.students = list(csv.DictReader(f))
            print(f"Data loaded successfully: {len(self.students)} students")
            return self.students
        except FileNotFoundError:
            return []

    def preview(self, n=5):
        print(f"First {n} rows:")
        for s in self.students[:n]:
            print(f"{s.get('id', 'N/A')} | {s.get('age', 'N/A')} | {s.get('gender', 'N/A')} | {s.get('country', 'N/A')} | GPA: {s.get('gpa', 'N/A')}")