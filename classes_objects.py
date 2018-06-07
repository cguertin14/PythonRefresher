lottery_player_dict = {
    'name': 'Marty D',
    'numbers': (5,6,7,8,9)
}

class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5,6,7,8,9)

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



anna = Student('Anna', 'MIT')
anna.marks.append(56)
anna.marks.append(71)

Student.go_to_school()








class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        return cls('{} - franchise'.format(store))
        # Return another store, with the same name as the argument's name, plus " - franchise"

    @staticmethod
    def store_details(store):
        return '{}, total stock price: '.format(store.name) + str(store.stock_price())
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'


print(Store.store_details(Store('Walmart')))