import os
from analytics.file_manager import FileManager
from analytics.data_loader import DataLoader
from analytics.analyser import SleepAnalyser
from analytics.report import Report
from analytics.result_saver import ResultSaver

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    fm = FileManager('students.csv')
    if not fm.check_file():
        exit()
    fm.create_output_folder()

    dl = DataLoader('students.csv')
    dl.load()
    dl.preview()

    analyser = SleepAnalyser(dl.students)
    print(analyser) 
    
    report = Report(analyser) 
    report.generate()


    print("\nRunning Task C3 filters:")
    low_sleep = list(filter(lambda s: float(s['sleep_hours']) < 6, dl.students))
    print(f"Filtered (sleep < 6): {len(low_sleep)}")

    gpa_values = list(map(lambda s: float(s['gpa']), dl.students))
    print(f"First 5 GPA map: {gpa_values[:5]}")

    saver = ResultSaver(analyser.result, 'output/result.json')
    saver.save_json()