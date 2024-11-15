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


def main():
    tracker = PerformanceTracker()
    while True:
        name = input("Enter student's name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
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

    tracker.display_student_performance()


if __name__ == "__main__":
    main()
