import csv 

class datos:
    def __init__(self):
        self.file = open(r"C:\Users\Luis Reyes\Downloads\exam_results.csv", "r", newline="")
        self.reader = csv.DictReader(self.file, delimiter=",")

    def find_exam_name(self, subject):
        names = ""
        for data in self.reader:
            if data["Exam Name"] == subject:
                names+=subject
            else:
                continue
            self.file.seek(0)
            self.reader = csv.DictReader(self.file, delimiter=",")
            return names
        
    def find_students(self, subject):
        number_of_candidates = []
        for data in self.reader:
            if data["Exam Name"] == subject and data["Candidate ID"] not in number_of_candidates:
                number_of_candidates.append(data["Candidate ID"])
        self.file.seek(0)
        self.reader = csv.DictReader(self.file, delimiter=",")
        return number_of_candidates
    
    def find_passed(self, subject):
        lst = self.find_students(subject)
        number_of_passed = []
        for data in self.reader:
            if data["Exam Name"] == subject and data["Candidate ID"] in lst and data["Grade"] == "Pass":
                    number_of_passed.append(data["Grade"])
        self.file.seek(0)
        self.reader = csv.DictReader(self.file, delimiter=",")
        return len(number_of_passed)

    def find_failed(self, subject):
        lst = self.find_students(subject)
        number_of_failed = []
        for data in self.reader:
            if data["Exam Name"] == subject and data["Candidate ID"] in lst and data["Grade"] == "Fail":
                number_of_failed.append(data["Grade"])
        self.file.seek(0)
        self.reader = csv.DictReader(self.file, delimiter=",")
        return len(number_of_failed)
    
    def find_best_score(self, subject):
        best_score = []
        for data in self.reader:
            if data["Exam Name"] == subject:
                best_score.append(data["Score"])
        self.file.seek(0)
        self.reader = csv.DictReader(self.file, delimiter=",")
        return max(best_score)

    def find_worst_score(self, subject):
        worst_score = []
        for data in self.reader:
            if data["Exam Name"] == subject:
                worst_score.append(data["Score"])
        self.file.seek(0)
        self.reader = csv.reader(self.file, delimiter=",")
        return min(worst_score)
    
class informe(datos):
    def __init__(self):
        self.file2 = open(r"C:\Users\Luis Reyes\Downloads\info_exam_results.csv", "w", newline="")
        fields = ["Exam Name", "Number of Candidates", "Number of Passed Exams", "Number of Failed Exams", "Best Score", "Worst Score"]
        self.writer = csv.DictWriter(self.file2, delimiter=",", quotechar="#", quoting=csv.QUOTE_MINIMAL, fieldnames=fields)

    def write(self):

        dato1 = datos()

        valores_maths = {
            "Exam Name": dato1.find_exam_name("Maths"),
            "Number of Candidates": len(dato1.find_students("Maths")),
            "Number of Passed Exams": dato1.find_passed("Maths"),
            "Number of Failed Exams": dato1.find_failed("Maths"),
            "Best Score": dato1.find_best_score("Maths"),
            "Worst Score": dato1.find_worst_score("Maths")
            }


        dato2 = datos()

        valores_physics = {
            "Exam Name": dato2.find_exam_name("Physics"),
            "Number of Candidates": len(dato2.find_students("Physics")),
            "Number of Passed Exams": dato2.find_passed("Physics"),
            "Number of Failed Exams": dato2.find_failed("Physics"),
            "Best Score": dato2.find_best_score("Physics"),
            "Worst Score": dato2.find_worst_score("Physics")
            }

        dato3 = datos()

        valores_biology = {
            "Exam Name": dato3.find_exam_name("Biology"),
            "Number of Candidates": len(dato3.find_students("Biology")),
            "Number of Passed Exams": dato3.find_passed("Biology"),
            "Number of Failed Exams": dato3.find_failed("Biology"),
            "Best Score": dato3.find_best_score("Biology"),
            "Worst Score": dato3.find_worst_score("Biology")
            }

        self.writer.writeheader()
        self.writer.writerow(valores_maths)
        self.writer.writerow(valores_physics)
        self.writer.writerow(valores_biology)

info = informe()
info.write()
info.file2.close()

