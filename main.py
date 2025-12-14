from service.CabManagement import CabBookingService


def run_demo():
    """Demo class to execute all test cases from problem statement"""
    
    print("=" * 60)
    print("CAB BOOKING SYSTEM - DEMO")
    print("=" * 60)
    
    cab_service = CabBookingService()
    
    # ==================== USER ONBOARDING ====================
    print("\n--- Onboarding Users ---")
    
    print(cab_service.add_user("Abhishek, M, 23"))
    print(cab_service.update_user_location("Abhishek", (0, 0)))
    
    print(cab_service.add_user("Rahul, M, 29"))
    print(cab_service.update_user_location("Rahul", (10, 0)))
    
    print(cab_service.add_user("Nandini, F, 22"))
    print(cab_service.update_user_location("Nandini", (15, 6)))
    
    # ==================== DRIVER ONBOARDING ====================
    print("\n--- Onboarding Drivers ---")
    
    print(cab_service.add_driver("Driver1, M, 22", "Swift, KA-01-12345", (10, 1)))
    print(cab_service.add_driver("Driver2, M, 29", "Swift, KA-01-12346", (11, 10)))
    print(cab_service.add_driver("Driver3, M, 24", "Swift, KA-01-12347", (5, 3)))
    
    # ==================== RIDE BOOKING ====================
    print("\n--- Ride Booking Tests ---")
    
    # Test 1: Abhishek tries to find a ride (all drivers > 5 units away)
    print("\nTest 1: find_ride('Abhishek', (0,0), (20,1))")
    result = cab_service.find_ride("Abhishek", (0, 0), (20, 1))
    print(f"Output: {result}")
    
    # Test 2: Rahul finds a ride (Driver1 is within 5 units)
    print("\nTest 2: find_ride('Rahul', (10,0), (15,3))")
    result = cab_service.find_ride("Rahul", (10, 0), (15, 3))
    print(f"Output: {result}")
    
    # Test 3: Rahul chooses Driver1
    print("\nTest 3: choose_ride('Rahul', 'Driver1')")
    result = cab_service.choose_ride("Rahul", "Driver1")
    print(f"Output: {result}")
    
    # Test 4: Calculate bill for Rahul
    print("\nTest 4: calculateBill('Rahul')")
    result = cab_service.calculate_bill("Rahul")
    print(f"Output: {result}")
    
    # Test 5: Change Driver1 status to unavailable
    print("\nTest 5: change_driver_status('Driver1', False)")
    result = cab_service.change_driver_status("Driver1", False)
    print(f"Output: {result}")
    
    # Test 6: Nandini tries to find a ride (Driver1 unavailable)
    print("\nTest 6: find_ride('Nandini', (15,6), (20,4))")
    result = cab_service.find_ride("Nandini", (15, 6), (20, 4))
    print(f"Output: {result}")
    
    # ==================== EARNINGS ====================
    print("\n--- Total Earnings ---")
    print("\nfind_total_earning():")
    result = cab_service.find_total_earning()
    print(result)
    
    print("\n" + "=" * 60)
    print("DEMO COMPLETED")
    print("=" * 60)


def run_additional_tests():
    """Additional test cases for edge cases"""
    
    print("\n" + "=" * 60)
    print("ADDITIONAL TEST CASES")
    print("=" * 60)
    
    cab_service = CabBookingService()
    
    # Setup
    cab_service.add_user("TestUser, M, 25")
    cab_service.update_user_location("TestUser", (0, 0))
    cab_service.add_driver("TestDriver, M, 30", "Sedan, KA-00-0000", (1, 1))
    
    # Test: User not found
    print("\nTest: Invalid user")
    try:
        cab_service.find_ride("InvalidUser", (0, 0), (10, 10))
    except ValueError as e:
        print(f"Expected Error: {e}")
    
    # Test: Driver not found
    print("\nTest: Invalid driver")
    try:
        cab_service.find_ride("TestUser", (0, 0), (10, 10))
        cab_service.choose_ride("TestUser", "InvalidDriver")
    except ValueError as e:
        print(f"Expected Error: {e}")
    
    # Test: Duplicate user
    print("\nTest: Duplicate user")
    try:
        cab_service.add_user("TestUser, F, 30")
    except Exception as e:
        print(f"Expected Error: {e}")
    
    print("\nAdditional tests completed!")


if __name__ == "__main__":
    run_demo()
    run_additional_tests()
