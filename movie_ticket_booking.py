def book_seat(booked_seats, seat_number, total_seats):
    if seat_number in booked_seats:
        print(f"Seat {seat_number} is already booked.")
    elif seat_number > total_seats or seat_number < 1:
        print("Invalid seat number.")
    else:
        booked_seats.append(seat_number)
        print(f"Seat {seat_number} has been successfully booked.")
def cancel_seat(booked_seats, seat_number):
    if seat_number in booked_seats:
        booked_seats.remove(seat_number)
        print(f"Seat {seat_number} has been successfully canceled.")
    else:
        print(f"Seat {seat_number} was not booked.")
def available_seats(total_seats, booked_seats):
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]
total_seats = 10
booked_seats = [2, 5, 7]
book_seat(booked_seats, 3, total_seats)
cancel_seat(booked_seats, 5)
available = available_seats(total_seats, booked_seats)
print("Available seats:", available)
