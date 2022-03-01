class User:
    def __init__(self, user_id, user_name):
        print('New user being created') 
        self.id = user_id    #initiialise attribites
        self.username = user_name 
        self.followers = 20
        self.following = 20
        

    def follow(self, user):
        user.followers += 2
        self.following += 4

    #initiialise attribites

user_1 = User('2kliff', 'kliff')

print(user_1.username)

user_2 = User('2rood', 'rood')
# print(user_2.username)

# print(user_1.followers)

user_1.follow(user_2) #user.1 gets entered into self and (user_2) inside the function get executed on user 
# print('User 1:',user_1.followers) 
# print('User 1:',user_1.following)
# print('User 2:',user_2.followers)
# print('User 2:',user_2.following)
