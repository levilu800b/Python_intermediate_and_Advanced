class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

user1 = User("001", "Angela")
user2 = User("002", "Jack")

# user2 = User()
# user2.id = "002"
# user2.username = "Jack"