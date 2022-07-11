class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(User())

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 20
    
    def spend_points(self,amount):
        self.gold_card_points = self.gold_card_points - amount

R2D2 = User("R2","D2","beepboop@gmail.com", 4)
C3PO = User("C3","PO","ohdear@gmail.com", 9)

spend_points(R2D2, 50)
enroll(C3PO)
spend_points(R2D2, 80)
display_info(R2D2)
display_info(C3PO)

