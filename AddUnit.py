# AddUnit.py

import importlib.util
import sys

# Load the GeneratorTest.py module
spec = importlib.util.spec_from_file_location("GeneratorTest", "GeneratorTest.py")
generator_test = importlib.util.module_from_spec(spec)
sys.modules["GeneratorTest"] = generator_test
spec.loader.exec_module(generator_test)

def add_unit():
    unit_name = input("Enter the unit name: ")
    faction = input("Enter the faction name: ")
    try:
        unit_cost = int(input("Enter the unit cost: "))
        if unit_cost < 0:
            raise ValueError("Cost cannot be negative.")
    except ValueError as e:
        print(f"Invalid cost. Please enter a positive integer. Error: {e}")
        return

    new_unit = f"{unit_name} ({faction})"
    generator_test.unit.append(new_unit)
    generator_test.cost.append(unit_cost)
    print(f"Added {new_unit} with a cost of {unit_cost}.")

if __name__ == "__main__":
    while True:
        add_unit()
        cont = input("Do you want to add another unit? (yes/no): ").strip().lower()
        if cont != 'yes':
            break

    print("\nUpdated unit list:")
    print(generator_test.unit)
    print("\nUpdated cost list:")
    print(generator_test.cost)

    # Save the updated lists to the GeneratorTest.py file
    with open("GeneratorTest.py", "r") as file:
        lines = file.readlines()

    with open("GeneratorTest.py", "w") as file:
        for line in lines:
            if line.startswith("unit = ["):
                file.write(f"unit = {generator_test.unit}\n")
            elif line.startswith("cost = ["):
                file.write(f"cost = {generator_test.cost}\n")
            else:
                file.write(line)
