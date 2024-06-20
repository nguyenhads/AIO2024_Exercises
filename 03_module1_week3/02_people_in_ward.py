from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):

    def __init__(self, name: str, yob: int, grade: str):
        self._name = name
        self._yob = yob
        self._grade = grade

    def get_yob(self):
        return self._yob

    def describe(self):
        print(f"Student - Name: {self._name} -YoB: {self._yob} \
              - Grade: {self._grade}")


class Teacher(Person):

    def __init__(self, name: str, yob: int, subject: str):
        self._name = name
        self._yob = yob
        self._subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self._name} -YoB: {self._yob} \
                - Grade: {self._subject}"
        )


class Doctor(Person):

    def __init__(self, name: str, yob: int, specialist: str):
        self._name = name
        self._yob = yob
        self._specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self._name} -YoB: {self._yob} \
                - Grade: {self._specialist}"
        )


class Ward:

    def __init__(self, name: str):
        self.__name = name
        self.__list_of_people = []

    def add_person(self, person: Person):
        self.__list_of_people.append(person)

    def describe(self):
        print(f"Ward name: {self.__name}")
        for p in self.__list_of_people:
            p.describe()

    def count_doctor(self):
        count = 0
        for p in self.__list_of_people:
            if isinstance(p, Doctor):
                count += 1
        return count


if __name__ == "__main__":
    # Create a list of people
    student1 = Student(name="studentA", yob=2010, grade="7")
    teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
    teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
    doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
    doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")

    ward1 = Ward(name="Ward1")
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    ward1.add_person(doctor2)

    ward1.describe()
    print(f"Number of doctors: {ward1.count_doctor()}")
