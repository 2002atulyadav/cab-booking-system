from typing import Dict, Optional
from models.user import User
from models.location import Location


class UserService:
    def __init__(self):
        self._users: Dict[str, User] = {}
    
    def add_user(self, user_details: str) -> str:
        """Add a new user. Format: 'name, gender, age'"""
        try:
            parts = [p.strip() for p in user_details.split(',')]
            if len(parts) != 3:
                raise ValueError("Invalid user details format")
            
            name, gender, age = parts
            if name in self._users:
                raise ValueError(f"User {name} already exists")
            
            user = User(username=name, gender=gender, age=int(age))
            self._users[name] = user
            return f"User {name} added successfully"
        except Exception as e:
            raise Exception(f"Failed to add user: {str(e)}")
    
    def update_user(self, username: str, updated_details: str) -> str:
        """Update user details"""
        if username not in self._users:
            raise ValueError(f"User {username} not found")
        
        parts = [p.strip() for p in updated_details.split(',')]
        user = self._users[username]
        
        if len(parts) >= 1 and parts[0]:
            user.gender = parts[0]
        if len(parts) >= 2 and parts[1]:
            user.age = int(parts[1])
        
        return f"User {username} updated successfully"
    
    def update_user_location(self, username: str, location: tuple) -> str:
        """Update user's current location"""
        if username not in self._users:
            raise ValueError(f"User {username} not found")
        
        self._users[username].current_location = Location(x=location[0], y=location[1])
        return f"User {username} location updated to {location}"
    
    def get_user(self, username: str) -> Optional[User]:
        """Get user by username"""
        return self._users.get(username)
    
    def get_all_users(self) -> Dict[str, User]:
        """Get all users"""
        return self._users    
        
        
    
