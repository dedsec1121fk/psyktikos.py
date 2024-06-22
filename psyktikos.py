#!/data/data/com.termux/files/usr/bin/python
# -*- coding: utf-8 -*-

def show_menu():
    print("\n")
    print("Please select one of the following options:")
    print("1) Refrigerants and Pressures")
    print("2) Purchase")
    print("3) Issues")
    print("4) Parts")
    print("5) E Errors")
    print("6) Exit")
    print("\n")

def refrigerants_and_pressures():
    print("\nLast 5 types of refrigerants and their pressures in hot and cold:")
    # Replace with actual code to display last 5 refrigerants and pressures

    refrigerants = [
        {"type": "R410A", "hot_pressure": "250 psi", "cold_pressure": "120 psi"},
        {"type": "R32", "hot_pressure": "280 psi", "cold_pressure": "110 psi"},
        {"type": "R134a", "hot_pressure": "270 psi", "cold_pressure": "115 psi"},
        {"type": "R22", "hot_pressure": "240 psi", "cold_pressure": "125 psi"},
        {"type": "R407C", "hot_pressure": "260 psi", "cold_pressure": "118 psi"}
    ]

    for refrigerant in refrigerants:
        print(f"{refrigerant['type']}: Hot Pressure - {refrigerant['hot_pressure']}, Cold Pressure - {refrigerant['cold_pressure']}")

def top_and_worst_brands():
    print("\nTop 20 and Worst 20 air conditioner brands:")
    # Replace with actual code to display top and worst air conditioner brands

    top_brands = [
        "Daikin", "Mitsubishi Electric", "Fujitsu", "LG", "Samsung",
        "Panasonic", "Carrier", "Trane", "Lennox", "Hitachi",
        "Sharp", "Toshiba", "Gree", "Electrolux", "Haier",
        "Sanyo", "Bryant", "American Standard", "York", "Maytag"
    ]
    worst_brands = [
        "Hisense", "TCL", "Kelvinator", "Whirlpool", "Rinnai",
        "Olsen", "General Electric", "Westinghouse", "Heil", "Bosch",
        "Amana", "Coleman", "Goodman", "Ducane", "Ruud",
        "Comfortmaker", "Janitrol", "Tempstar", "Payne", "Day & Night"
    ]

    print("Top Brands:")
    for i, brand in enumerate(top_brands, start=1):
        print(f"{i}. {brand}")

    print("\nWorst Brands:")
    for i, brand in enumerate(worst_brands, start=1):
        print(f"{i}. {brand}")

def common_issues():
    print("\nTop 15 common air conditioner issues and their solutions in simple steps:")
    # Replace with actual code to display common issues and solutions

    issues = [
        {"issue": "Air conditioner not cooling", "solution": "Check air filters and clean if necessary."},
        {"issue": "Air conditioner making noise", "solution": "Inspect fan blades and motor for issues."},
        {"issue": "Air conditioner not turning on", "solution": "Check power supply and thermostat settings."},
        {"issue": "Air conditioner leaking water", "solution": "Clear blocked drain pipe."},
        {"issue": "Air conditioner freezing up", "solution": "Ensure proper airflow and check for refrigerant leaks."},
        {"issue": "Air conditioner emitting bad smell", "solution": "Clean or replace air filters and check for mold."},
        {"issue": "Air conditioner not blowing air", "solution": "Inspect fan motor and capacitor."},
        {"issue": "Air conditioner running but not cooling", "solution": "Check refrigerant levels and compressor."},
        {"issue": "Air conditioner producing weak airflow", "solution": "Clean air vents and ensure no obstructions."},
        {"issue": "Air conditioner thermostat problems", "solution": "Check for loose connections and calibration."},
        {"issue": "Air conditioner cycling on and off", "solution": "Inspect thermostat and check for system capacity."},
        {"issue": "Air conditioner compressor not working", "solution": "Test capacitors and contactors."},
        {"issue": "Air conditioner condenser fan not working", "solution": "Check fan motor and replace if necessary."},
        {"issue": "Air conditioner not cooling enough", "solution": "Clean evaporator coils and check for leaks."},
        {"issue": "Air conditioner tripping the circuit breaker", "solution": "Check for electrical faults and loose connections."}
    ]

    for i, issue in enumerate(issues, start=1):
        print(f"{i}. {issue['issue']}: {issue['solution']}")

def air_conditioner_parts():
    print("\nGeneric air conditioner parts and their functions:")
    # Replace with actual code to display air conditioner parts and their functions

    parts = [
        {"part": "Compressor", "function": "Pumps refrigerant through the system."},
        {"part": "Condenser Coil", "function": "Removes heat from the refrigerant."},
        {"part": "Evaporator Coil", "function": "Absorbs heat from indoor air."},
        {"part": "Expansion Valve", "function": "Regulates refrigerant flow."},
        {"part": "Thermostat", "function": "Monitors and controls the temperature."},
        {"part": "Fan Motor", "function": "Circulates air over coils."},
        {"part": "Capacitor", "function": "Provides extra power to start the compressor and fan motors."},
        {"part": "Contactor", "function": "Controls the flow of electricity to the compressor and fan motor."},
        {"part": "Air Filter", "function": "Removes dust and debris from the air."},
        {"part": "Refrigerant", "function": "Cools and dehumidifies the air."},
        {"part": "Ductwork", "function": "Distributes air throughout the building."},
        {"part": "Condensate Drain Line", "function": "Removes condensation from the evaporator coil."},
        {"part": "Heat Exchanger", "function": "Transfers heat between refrigerant and air."},
        {"part": "Solenoid Valve", "function": "Controls the flow of refrigerant in heat pump systems."},
        {"part": "Defrost Control Board", "function": "Activates defrost mode in heat pump systems."}
    ]

    for i, part in enumerate(parts, start=1):
        print(f"{i}. {part['part']}: {part['function']}")

def e_errors():
    print("\nE Errors and their solutions:")
    # Replace with actual E Errors and their solutions

    e_errors = {
        "E1": "Issue with the air conditioner's power supply. Check for tripped circuit breakers or blown fuses. Reset the breaker if necessary.",
        "E2": "Indoor temperature sensor fault. Check the sensor wiring and replace if necessary.",
        "E3": "Outdoor temperature sensor fault. Inspect the sensor for damage or wiring issues. Replace if necessary.",
        "E4": "Indoor coil temperature sensor fault. Check sensor wiring and replace if necessary.",
        "E5": "Outdoor coil temperature sensor fault. Inspect sensor for damage or wiring issues. Replace if necessary.",
        "E6": "Communication error between indoor and outdoor units. Check wiring connections and reset communication settings.",
        "E7": "Faulty compressor. Check compressor wiring and connections. Test the compressor and replace if necessary.",
        "E8": "Faulty fan motor. Inspect fan motor and connections. Test the motor and replace if necessary.",
        "E9": "Low refrigerant level. Check for leaks and refill refrigerant as per manufacturer's specifications."
    }

    for error, solution in e_errors.items():
        print(f"{error}: {solution}")

# Main program
if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Select an option (1/2/3/4/5/6): ")

        if choice == '1':
            refrigerants_and_pressures()
        elif choice == '2':
            top_and_worst_brands()
        elif choice == '3':
            common_issues()
        elif choice == '4':
            air_conditioner_parts()
        elif choice == '5':
            e_errors()
        elif choice == '6':
            print("Exiting Psyktikos Program.")
            break
        else:
            print("Invalid choice. Please try again.")
