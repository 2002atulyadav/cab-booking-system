from models.user import User
from models.location import Location

class UserManager:
    def __init__(self):
        self.users = {}
    def add_user(self, newuser : User):
        self.users.append(newuser)
        return "User register successfully"
    
    def update_user_profile(self, user_details : User):
        for user in self.users :
            if user.user_id == user_details.user_id :
                user.username = user_details.username
                user.email_id = user_details.email_id
                user.phone_number = user_details.phone_number
                break
        return "user profile updated succesfully"
    def update_user_current_locaton(self, user_id : int , current_location : Location):
        for user in self.users:
            if user.user_id == user_id :
                user.current_location = Location
                break
        return "User location updated succesfully"
    

            

        


