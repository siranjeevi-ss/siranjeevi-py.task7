#task 7
# -------------------------------
# Task 1: super() usage
# -------------------------------
class Student():
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return f"Student: {self.name}, ID: {self.id}, Dept: {self.dept}, Fees: {self.fees}"


class Faculty():
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def get_details(self):
        return f"Faculty: {self.name}, ID: {self.id}, Salary: {self.salary}"


class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

    def get_details(self):
        return f"TempFaculty: {self.name}, ID: {self.id}, Salary: {self.salary}, Duration: {self.duration}"


# -------------------------------
# Sample Data
# -------------------------------
students = [
    Student("Indhu", 101, "CSE", 60000),
    Student("Ravi", 102, "ECE", 45000),
    Student("Priya", 103, "IT", 70000)
]

faculty = [
    Faculty("Arun", 201, 40000),
    Faculty("Meena", 202, 28000),
    TempFaculty("John", 203, 35000, "6 months")
]
# -------------------------------
# Task 2: Abstraction
# -------------------------------
class AbstractUser():
    
    def get_details(self):
        pass


# -------------------------------
# Base Class
# -------------------------------
class User(AbstractUser):
    def __init__(self, name, id):
        self.name = name
        self.id = id





# -------------------------------
# Task 3: Sorting
# -------------------------------
students.sort(key=lambda x: x.fees)
faculty.sort(key=lambda x: x.salary)


# -------------------------------
# Task 4: map()
# -------------------------------
student_names = list(map(lambda s: s.name, students))


# -------------------------------
# Task 5: filter()
# -------------------------------
high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))


# -------------------------------
# Task 6: reduce()
# -------------------------------
total_fees = (lambda acc, s: acc + s.fees, students, 0)
total_salary = (lambda acc, f: acc + f.salary, faculty, 0)


# -------------------------------
# Task 7: Higher Order Function
# -------------------------------
def process_users(users, func):
    return list(map(func, users))


# Example usage
processed_names = process_users(students, lambda s: s.name.upper())


# -------------------------------
# Final Output
# -------------------------------
print("\n--- All User Details ---")
for user in students + faculty:
    print(user.get_details())

print("\n--- Sorted Students (by Fees) ---")
for s in students:
    print(s.get_details())

print("\n--- Sorted Faculty (by Salary) ---")
for f in faculty:
    print(f.get_details())

print("\n--- Student Names (map) ---")
print(student_names)

print("\n--- High Fee Students (>50000) ---")
for s in high_fee_students:
    print(s.get_details())

print("\n--- High Salary Faculty (>30000) ---")
for f in high_salary_faculty:
    print(f.get_details())

print("\n--- Total Fees Collected ---")
print(total_fees)

print("\n--- Total Salary Paid ---")
print(total_salary)

print("\n--- Processed Names (Uppercase using HOF) ---")
print(processed_names)