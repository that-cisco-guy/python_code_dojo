class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = False
        self.gold_card_points = 0
    def display_info(self):
        print(self.first_name, self.last_name, self.email, self.age, self.is_reward_member, self.gold_card_points)
        return self
    def enroll(self):
        if self.is_reward_member == False:
            self.is_reward_member = True
            self.gold_card_points += 200
        else:
            print('Already Enrolled')
        return self
    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
        else:
            print('Insufficient Points')
        return self

jerry = User('Jerry','Anderson', 'someemail@email.com',36)
jerry.display_info().enroll().spend_points(50).display_info().enroll()
niko = User('Nicholas','Anderson','niki@nikomail.com',7)
rachel = User('Rachel','Anderson','Rachel@rachelmail.com',36)
niko.enroll().spend_points(80).display_info()
rachel.spend_points(500).display_info()