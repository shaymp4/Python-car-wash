# Python-car-wash
A simple command-line car wash management application built in Python. This system allows you to manage car registrations, track washing status, and monitor revenue simulating a car wash business.

## Features

- **Car Registration**: Add new cars with owner details and specifications
- **Washing Management**: Track which cars need washing and mark them as clean
- **Revenue Tracking**: Monitor total earnings from car washing services
- **Persistent Storage**: All data is saved to text files and restored on startup
- **Settings Management**: Easily update car wash name and pricing
- **Input Validation**: Comprehensive validation for all user inputs

## Getting Started

### Prerequisites

- Python 3.6 or higher
- No additional libraries required (uses only standard library)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/shaymp4/Python-car-wash.git
   cd Python-car-wash
   ```

2. Run the application:
   ```bash
   python car_wash.py
   ```

### First Run

When you first run the application, you'll be prompted to create your car wash:
- Enter your car wash name
- Set pricing for small cars
- Set pricing for large cars
all of which can be edited later in settings

## Usage

### Main Menu Options

1. **Add Car**: Register a new car with owner details
2. **View Dirty Cars**: Display all cars that need washing
3. **Wash Car**: Mark a car as clean and add to revenue
4. **View Revenue**: Check total earnings
5. **Settings**: Modify car wash name and pricing
6. **Exit**: Close the application

### Adding a Car

When adding a car, you'll need to provide:
- Owner's name
- Registration number
- Contact number
- Car make and model
- Manufacturing year (1884-current year)
- Size (Small or Large)

### Washing Cars

- Search by registration number
- System automatically calculates price based on car size
- Revenue is updated and saved automatically
- Cars are marked as clean in the system

## File Structure

```
car-wash-management/
│
├── car_wash.py          # Main application file
├── car_wash.txt         # Car wash settings (created automatically)
├── cars.txt             # Car database (created automatically)
└── README.md            # This file
```

## Data Storage

The application uses two text files for data persistence:

- **car_wash.txt**: Stores car wash name, pricing, and total revenue
- **cars.txt**: Stores all registered cars and their status

## Classes and Structure

### Car Class
Represents individual cars with attributes:
- Owner information
- Vehicle specifications
- Cleaning status

### CarWash Class
Manages the car wash business with methods for:
- Adding and managing cars
- Processing washes
- Tracking revenue
- Settings management

## Input Validation

The system includes robust validation for:
- **Empty inputs**: Prevents blank entries
- **Year validation**: Ensures realistic manufacturing years (1884-present)
- **Size validation**: Only accepts "small" or "large"
- **Numeric inputs**: Validates pricing and menu selections

## Example Usage

```
|||***Mike's Car Wash***|||
1| Add car
2| View dirty cars
3| Wash car
4| View revenue
5| Settings
6| Exit
Please select an option (1/6): 1

Enter owners name: John Smith
Enter registration number: ABC123
Enter owner's contact number: 077
Enter the make of the car: Toyota
Enter the model of the car: Camry
Enter the year of the car: 2020
Enter the size of the car (Small/Large): large
John Smith's car has been added and saved.
```

## Error Handling

The application handles common errors:
- File not found (creates new files)
- Invalid data formats
- User input errors
- Value conversion errors

## Known Issues

- Duplicate registration numbers are not prevented
- Comma characters in data fields may cause parsing issues
- No backup mechanism for data files

## Future Enhancements

- Add duplicate registration prevention
- Add customer history tracking
- Include appointment scheduling
