# Function to book a seat
def book_seat(total_seats, booked_seats, seat_no):
    if seat_no < 1 or seat_no > total_seats:
        return f"Seat {seat_no} is invalid"
    if seat_no in booked_seats:
        return f"Seat {seat_no} is already booked"
    booked_seats.append(seat_no)
    return f"Seat {seat_no} booked successfully"
# Function to cancel a booked seat
def cancel_seat(booked_seats, seat_no):
    if seat_no in booked_seats:
        booked_seats.remove(seat_no)
        return f"Seat {seat_no} canceled successfully"
    return f"Seat {seat_no} was not booked"
# Function to get the list of available seats
def available_seats(total_seats, booked_seats):
    return [s for s in range(1, total_seats+1) if s not in booked_seats]
# Input total number of seats
total_seats = int(input("Enter total number of seats: "))
booked_seats = [] 
while True:
    print("\n--- Movie Ticket Booking System ---")
    print("1. Book Seat")
    print("2. Cancel Seat")
    print("3. View Available Seats")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":  
        seat_no = int(input("Enter seat number to book: "))
        print(book_seat(total_seats, booked_seats, seat_no))
    elif choice == "2":  
        seat_no = int(input("Enter seat number to cancel: "))
        print(cancel_seat(booked_seats, seat_no))
    elif choice == "3": 
        print("Available seats:", available_seats(total_seats, booked_seats))
    elif choice == "4":  
        print("Final booked seats:", booked_seats)
        break
    else: 
        print("Invalid choice! Try again.")
