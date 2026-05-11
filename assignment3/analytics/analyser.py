class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def __str__(self):
        return f"{self.__class__.__name__}: Base Analyser"

    def analyse(self):
        pass

    def print_results(self):
        pass

class SleepAnalyser(DataAnalyser):
    def __str__(self):
        return f"SleepAnalyser: Sleep vs GPA Analysis, {len(self.students)} students"

    def analyse(self):
        low = [float(s['gpa']) for s in self.students if float(s['sleep_hours']) < 6]
        high = [float(s['gpa']) for s in self.students if float(s['sleep_hours']) >= 6]
        
        avg_low = round(sum(low) / len(low), 2) if low else 0
        avg_high = round(sum(high) / len(high), 2) if high else 0
        
        self.result = {
            "low_sleep": {"count": len(low), "avg_gpa": avg_low},
            "high_sleep": {"count": len(high), "avg_gpa": avg_high},
            "gpa_difference": round(abs(avg_high - avg_low), 2)
        }
        return self.result

    def print_results(self):
        print("Sleep vs GPA Analysis")
        print(f"Students sleeping < 6 hours: {self.result['low_sleep']['count']} avg GPA: {self.result['low_sleep']['avg_gpa']}")
        print(f"Students sleeping >= 6 hours: {self.result['high_sleep']['count']} avg GPA: {self.result['high_sleep']['avg_gpa']}")
        print(f"GPA difference: {self.result['gpa_difference']}")