import pandas as pd

# Define constants for the seat states
FREE = 'F'
BOOKED = 'R'
AISLE = 'X'
STORAGE = 'S'

# Initialize the DataFrame for the seat layout
rows = ['A', 'B', 'C', 'X', 'D', 'E', 'F']  # Define row labels (including 'X' for aisles)
columns = [str(i) for i in range(1, 81)]  

# Create the DataFrame with all seats initially free
seating_chart = pd.DataFrame(FREE, index=rows, columns=columns)

# Set the 'X' row (4th row) as the aisle, not bookable
seating_chart.loc['X'] = AISLE

# Set specific seats in the 77th and 78th columns for rows D, E, F as storage areas
for col in ['77', '78']:
    seating_chart.loc[['D', 'E', 'F'], col] = STORAGE

def display_menu():
    print("\nMenu:")
    print("1. Check availability of seat")
    print("2. Book a seat")
    print("3. Free a seat")
    print("4. Show booking state")
    print("5. Exit program")
    choice = input("Select an option: ")
    return choice

def check_availability(row, col):
    try:
        if seating_chart.at[row, col] == FREE:
            print(f"Seat {row}{col} is available.")
            return True
        else:
            print(f"Seat {row}{col} is not available.")
            return False
    except KeyError:
        print("Invalid seat position.")
        return False

def book_seat(row, col):
    if check_availability(row, col):
        seating_chart.at[row, col] = BOOKED
        print(f"Seat {row}{col} has been booked.")
    else:
        print(f"Seat {row}{col} cannot be booked.")

def free_seat(row, col):
    if seating_chart.at[row, col] == BOOKED:
        seating_chart.at[row, col] = FREE
        print(f"Seat {row}{col} has been freed.")
    else:
        print("Only booked seats can be freed.")

def show_booking_state():
    print(seating_chart)

def main():
    while True:
        choice = display_menu()
        if choice == '5':
            print("Exiting program.")
            break
        elif choice in {'1', '2', '3'}:
            row = input("Enter seat row (A-F, X for aisle): ").upper()
            col = input("Enter seat column (1-80): ")
            if row not in rows or col not in columns:
                print("Invalid row or column. Please try again.")
                continue

        if choice == '1':
            check_availability(row, col)
        elif choice == '2':
            book_seat(row, col)
        elif choice == '3':
            free_seat(row, col)
        elif choice == '4':
            show_booking_state()
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
