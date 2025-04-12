from backend.utils import calculate_actual_size

def main():
    username = input("Enter your username: ")
    specimen_size = float(input("Enter the specimen size in mm: "))
    magnification = float(input("Enter the microscope magnification: "))
    
    actual_size = calculate_actual_size(specimen_size, magnification)
    print(f"Actual size: {actual_size} mm")

if __name__ == "__main__":
    main()