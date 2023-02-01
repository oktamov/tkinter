class Person:
    def __init__(self, fullname, age, locatsion, date, grade, DOJ):
        self.fullname = fullname
        self.age = age
        self.locatsion = locatsion
        self.date = date
        self.grade = grade
        self.DOJ = DOJ

    def get_attrs(self, as_dict=False):
        if as_dict:
            return {
                "Fullname": self.fullname,
                "Age": self.age,
                "Locatsion": self.locatsion,
                "Date": self.date,
                "Grade": self.grade,
                "DOJ": self.DOJ

            }
        return [
            self.fullname,
            self.age,
            self.locatsion,
            self.date,
            self.grade,
            self.DOJ
        ]
