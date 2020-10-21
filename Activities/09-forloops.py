"""
    The list below is a list of patients. The tempretures are in fahrenheit.
    1. Loop through the list
    2. Convert the tempretures to Celsius using ((T - 32) * 5) / 9
    3. Print a formatted string in a format as such "Patient Name has a tempreture of 38 C"
"""
patients = [
    {
        'name': 'Marky Mark',
        'age': 49,
        'emergency_contacts': ["Tommy Wiseau", "Lewis Hamilton"],
        'vitals': {
            'heart_rate': 2,
            'temprature': 99
        }
    },
    {
        'name': 'Lewis Hamilton',
        'age': 29,
        'emergency_contacts': ["JayZ", "Beyonce"],
        'vitals': {
            'heart_rate': 3,
            'temprature': 98
        }
    },
    {
        'name': 'Tommy Wiseau',
        'age': 49,
        'emergency_contacts': ["Drake", "Lewis Hamilton", "Lewis Hamilton"],
        'vitals': {
            'heart_rate': 1,
            'temprature': 104
        }
    }
]