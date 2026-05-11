class Report:
    def __init__(self, analyser):
        self.analyser = analyser

    def generate(self):
        print("=" * 30)
        print("STUDENT ANALYSIS REPORT")
        print("=" * 30)
        self.analyser.analyse()
        self.analyser.print_results()
        print("=" * 30)