# Cab Booking System

A machine coding implementation of a cab booking application.

## Features

- **User Management**: Register users, update profiles, track locations
- **Driver Management**: Onboard drivers with vehicle details, manage availability
- **Ride Booking**: Find nearby available drivers (within 5 units), book rides
- **Billing**: Calculate fare based on distance ($1 per unit)
- **Earnings Tracking**: Track total earnings per driver

## Project Structure

```
cab-booking-system/
├── models/
│   ├── __init__.py
│   ├── location.py          # Location with distance calculation
│   ├── user.py              # User entity
│   ├── driver.py            # Driver entity
│   ├── vehicle.py           # Vehicle entity
│   └── booking.py           # Ride entity with status
├── service/
│   ├── __init__.py
│   ├── UserManagement.py    # User operations
│   ├── DriverManager.py     # Driver operations
│   ├── RouteManagement.py   # Ride operations
│   └── CabManagement.py     # Main orchestrator
├── tests/
│   └── test_cab_booking.py  # Unit tests
├── main.py                   # Demo/driver class
├── Problem.txt              # Problem statement
└── README.md
```

## How to Run

### Run Demo
```bash
python main.py
```

### Run Tests
```bash
python -m pytest tests/test_cab_booking.py -v
# OR
python tests/test_cab_booking.py
```

## API Reference

### User Operations
```python
add_user("name, gender, age")
update_user(username, "gender, age")
update_user_location(username, (x, y))
```

### Driver Operations
```python
add_driver("name, gender, age", "model, registration", (x, y))
update_driver_location(driver_name, (x, y))
change_driver_status(driver_name, True/False)
```

### Ride Operations
```python
find_ride(username, (source_x, source_y), (dest_x, dest_y))
choose_ride(username, driver_name)
calculate_bill(username)
find_total_earning()
```

## Sample Output

```
======================================
CAB BOOKING SYSTEM - DEMO
======================================

--- Onboarding Users ---
User Abhishek added successfully
User Abhishek location updated to (0, 0)
User Rahul added successfully
User Rahul location updated to (10, 0)
User Nandini added successfully
User Nandini location updated to (15, 6)

--- Onboarding Drivers ---
Driver Driver1 added successfully
Driver Driver2 added successfully
Driver Driver3 added successfully

--- Ride Booking Tests ---

Test 1: find_ride('Abhishek', (0,0), (20,1))
Output: No ride found

Test 2: find_ride('Rahul', (10,0), (15,3))
Output: Driver1 [Available]

Test 3: choose_ride('Rahul', 'Driver1')
Output: Ride Started

Test 4: calculateBill('Rahul')
Output: Ride Ended bill amount $6

Test 5: change_driver_status('Driver1', False)
Output: Driver Driver1 is now unavailable

Test 6: find_ride('Nandini', (15,6), (20,4))
Output: No ride found

--- Total Earnings ---

find_total_earning():
Driver1 earned $6
Driver2 earned $0
Driver3 earned $0

======================================
DEMO COMPLETED
======================================
```

## Design Decisions

1. **Euclidean Distance**: Used for calculating distance between locations
2. **Rate**: $1 per unit distance
3. **Max Pickup Distance**: 5 units (drivers shown only within this radius)
4. **Single Active Ride**: Users can have only one active ride at a time
5. **Driver Availability**: Automatically managed during ride lifecycle
6. **In-Memory Storage**: Uses dictionaries for all data storage

## Key Components

### Models
- `Location`: Stores x, y coordinates with distance calculation
- `User`: Stores user details and current location
- `Driver`: Stores driver info, vehicle, location, availability, and earnings
- `Vehicle`: Stores vehicle model and registration number
- `Ride`: Represents an active ride with status and billing

### Services
- `UserService`: Handles user registration and location updates
- `DriverService`: Manages driver onboarding and availability
- `RideService`: Manages ride lifecycle from search to completion
- `CabBookingService`: Orchestrates all operations

## Exception Handling

- Invalid user/driver not found
- Duplicate user registration
- Invalid input formats
- User already in active ride
- Driver not available
- Invalid ride search attempts

## Future Enhancements

- [ ] Concurrency handling with locks
- [ ] Ride history tracking
- [ ] Multiple vehicle types with different pricing
- [ ] Surge pricing during peak hours
- [ ] Rating system for users and drivers
- [ ] Ride cancellation support
- [ ] Payment processing integration
- [ ] Real-time driver tracking with WebSocket
- [ ] Machine learning for demand prediction
