import json
import os

# File to store hotel data
DATA_FILE = 'hotel_data.json'

# Initialize hotel data
def init_data():
    if not os.path.exists(DATA_FILE):
        data = {
            'rooms': [
                {'room_number': 101, 'status': 'available'},
                {'room_number': 102, 'status': 'available'},
                {'room_number': 201, 'status': 'available'},
                {'room_number': 202, 'status': 'available'}
            ],
            'bookings': []
        }
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)

# Load data from file
def load_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Save data to file
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Show available rooms
def show_available_rooms():
    data = load_data()
    available_rooms = [room for room in data['rooms'] if room['status'] == 'available']
    if available_rooms:
        print("Available Rooms:")
        for room in available_rooms:
            print(f"Room Number: {room['room_number']}")
    else:
        print("No rooms available.")

# Book a room
def book_room():
    data = load_data()
    show_available_rooms()
    room_number = int(input("Enter the room number you want to book: "))
    customer_name = input("Enter customer name: ")

    # Check if the room is available
    room = next((room for room in data['rooms'] if room['room_number'] == room_number), None)
    if room and room['status'] == 'available':
        room['status'] = 'booked'
        data['bookings'].append({'room_number': room_number, 'customer_name': customer_name})
        save_data(data)
        print("Room booked successfully!")
    else:
        print("Room is not available or does not exist.")

# Check out a room
def check_out():
    data = load_data()
    room_number = int(input("Enter the room number you want to check out: "))
    booking = next((booking for booking in data['bookings'] if booking['room_number'] == room_number), None)

    if booking:
        # Find the room and update status
        room = next((room for room in data['rooms'] if room['room_number'] == room_number), None)
        if room:
            room['status'] = 'available'
            data['bookings'].remove(booking)
            save_data(data)
            print("Checked out successfully!")
        else:
            print("Room does not exist.")
    else:
        print("No booking found for this room.")

# Main menu
def main_menu():
    init_data()
    while True:
        print("\nHotel Management System")
        print("1. Show Available Rooms")
        print("2. Book a Room")
        print("3. Check Out")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            show_available_rooms()
        elif choice == '2':
            book_room()
        elif choice == '3':
            check_out()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
