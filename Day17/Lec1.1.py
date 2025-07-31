#Constructor
class User:
    #whenever we create an object using this class, below constructor is triggered automatically
    def __init__(self,user_id,username):
        print("new user being created....")
        self.id=user_id
        self.username=username
        #let's set a default value for all the objects
        self.followers=0
        self.following=0

    def follow(self,user):
        user.followers+=1
        self.following+=1

user1=User(1,"Mimo")
user2=User(2,"Golu")
user3=User(3,"Nimo")

user1.follow(user2)
print(user1.following)
print(user2.following)



