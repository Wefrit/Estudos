class School:
    def __init__(self):
        self.students_list = {}
        self._added_history = []

    def add_student(self, name, grade):
        for students in self.students_list.values():
            if name in students:
                self._added_history.append(False)
                return False

        if grade not in self.students_list:
            self.students_list[grade] = set()

        self.students_list[grade].add(name)
        self._added_history.append(True)
        return True

    def added(self):
        return self._added_history

    def grade(self, grade_number):
        return sorted(self.students_list.get(grade_number, []))

    def roster(self):
        all_students = []
        for grade in sorted(self.students_list):
            all_students.extend(sorted(self.students_list[grade]))
        return all_students
