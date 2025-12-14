import unittest
import sys
sys.path.append('..')

from service.CabManagement import CabBookingService
from models.location import Location


class TestCabBookingService(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures"""
        self.service = CabBookingService()
        
        # Add users
        self.service.add_user("Abhishek, M, 23")
        self.service.update_user_location("Abhishek", (0, 0))
        
        self.service.add_user("Rahul, M, 29")
        self.service.update_user_location("Rahul", (10, 0))
        
        self.service.add_user("Nandini, F, 22")
        self.service.update_user_location("Nandini", (15, 6))
        
        # Add drivers
        self.service.add_driver("Driver1, M, 22", "Swift, KA-01-12345", (10, 1))
        self.service.add_driver("Driver2, M, 29", "Swift, KA-01-12346", (11, 10))
        self.service.add_driver("Driver3, M, 24", "Swift, KA-01-12347", (5, 3))
    
    def test_add_user(self):
        """Test user registration"""
        result = self.service.add_user("NewUser, M, 25")
        self.assertIn("successfully", result.lower())
    
    def test_add_duplicate_user(self):
        """Test duplicate user registration fails"""
        with self.assertRaises(Exception):
            self.service.add_user("Abhishek, M, 30")
    
    def test_add_driver(self):
        """Test driver registration"""
        result = self.service.add_driver("NewDriver, M, 28", "Honda, KA-99-9999", (0, 0))
        self.assertIn("successfully", result.lower())
    
    def test_find_ride_no_drivers_nearby(self):
        """Test that no ride is found when all drivers are far"""
        result = self.service.find_ride("Abhishek", (0, 0), (20, 1))
        self.assertEqual(result, "No ride found")
    
    def test_find_ride_driver_available(self):
        """Test finding available driver within range"""
        result = self.service.find_ride("Rahul", (10, 0), (15, 3))
        self.assertIn("Driver1", result)
        self.assertIn("Available", result)
    
    def test_choose_ride_and_billing(self):
        """Test complete ride flow"""
        self.service.find_ride("Rahul", (10, 0), (15, 3))
        
        result = self.service.choose_ride("Rahul", "Driver1")
        self.assertEqual(result, "Ride Started")
        
        result = self.service.calculate_bill("Rahul")
        self.assertIn("Ride Ended", result)
        self.assertIn("$", result)
    
    def test_driver_unavailable_after_status_change(self):
        """Test driver not shown after marking unavailable"""
        # Complete a ride first
        self.service.find_ride("Rahul", (10, 0), (15, 3))
        self.service.choose_ride("Rahul", "Driver1")
        self.service.calculate_bill("Rahul")
        
        # Mark driver unavailable
        self.service.change_driver_status("Driver1", False)
        
        # Nandini should not see Driver1
        result = self.service.find_ride("Nandini", (15, 6), (20, 4))
        self.assertEqual(result, "No ride found")
    
    def test_total_earnings(self):
        """Test total earnings calculation"""
        # Complete a ride
        self.service.find_ride("Rahul", (10, 0), (15, 3))
        self.service.choose_ride("Rahul", "Driver1")
        self.service.calculate_bill("Rahul")
        
        result = self.service.find_total_earning()
        self.assertIn("Driver1 earned $", result)
    
    def test_invalid_user_find_ride(self):
        """Test error when invalid user tries to find ride"""
        with self.assertRaises(ValueError):
            self.service.find_ride("InvalidUser", (0, 0), (10, 10))
    
    def test_location_distance(self):
        """Test distance calculation"""
        loc1 = Location(0, 0)
        loc2 = Location(3, 4)
        self.assertEqual(loc1.distance_to(loc2), 5.0)


class TestLocation(unittest.TestCase):
    
    def test_distance_calculation(self):
        """Test Euclidean distance calculation"""
        loc1 = Location(0, 0)
        loc2 = Location(3, 4)
        self.assertEqual(loc1.distance_to(loc2), 5.0)
    
    def test_zero_distance(self):
        """Test distance to same location is 0"""
        loc = Location(5, 5)
        self.assertEqual(loc.distance_to(loc), 0.0)


if __name__ == '__main__':
    unittest.main()
