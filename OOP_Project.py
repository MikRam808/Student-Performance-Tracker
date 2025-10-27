import csv

class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)

    def is_passing(self, passing_score=40):
        return all(score >= passing_score for score in self.scores)


class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        student = Student(name, scores)
        self.students[name] = student

    def calculate_class_average(self):
        if not self.students:
            return 0
        total_average = sum(student.calculate_average() for student in self.students.values())
        return total_average / len(self.students)

    def display_student_performance(self):
        print("\nStudent Performance:")
        for name, student in self.students.items():
            average = student.calculate_average()
            status = "Passing" if student.is_passing() else "Needs Improvement"
            print(f"Name: {name}, Average Score: {average:.2f}, Status: {status}")

        class_average = self.calculate_class_average()
        print(f"\nClass Average: {class_average:.2f}")

    # Export results to CSV
    def export_to_csv(self, filename="student_report.csv"):
        if not self.students:
            print("⚠ No student data to export.")
            return
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Student Name", "Math", "Science", "English", "Average", "Status"])
                for name, student in self.students.items():
                    average = student.calculate_average()
                    status = "Passing" if student.is_passing() else "Needs Improvement"
                    writer.writerow([name] + student.scores + [f"{average:.2f}", status])
            print(f"\n✅ Report saved successfully as {filename}")
        except Exception as e:
            print(f"Error exporting report: {e}")


def main():
    tracker = PerformanceTracker()
    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Display Performance")
        print("3. Export Report to CSV")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student's name: ")
            scores = []
            for subject in ["Math", "Science", "English"]:
                while True:
                    try:
                        score = int(input(f"Enter score for {subject}: "))
                        scores.append(score)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a numeric score.")
            tracker.add_student(name, scores)

        elif choice == '2':
            tracker.display_student_performance()

        elif choice == '3':
            tracker.export_to_csv()

        elif choice == '4':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please select 1–4.")


if __name__ == "__main__":
    main()
