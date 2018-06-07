lottery_player_dict = {
    'name': 'Marty D',
    'numbers': (5, 6, 7, 8, 9)
}


class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5, 6, 7, 8, 9)

    def total(self):
        return sum(self.numbers)


player_one = LotteryPlayer('Marty D')
player_two = LotteryPlayer('Marty D')

# print(player_one.name == player_two.name)

##


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @staticmethod
    def go_to_school():
        print('I\'m going to school')

    @classmethod
    def friend(cls, origin, friend_name, *args, **kwargs):
        return cls(friend_name, origin.school, args, kwargs)


##

class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title


anna = WorkingStudent('Anna', 'MIT', 20.00, 'Caissiere')
# anna.marks.append(56)
# anna.marks.append(71)

friend = WorkingStudent.friend(anna, 'Natasha', 20.00, job_title='developer')
print(friend.name)
print(friend.school)
print(friend.salary)