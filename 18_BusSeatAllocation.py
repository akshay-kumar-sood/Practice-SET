# Bus Seat Allocation

available_seats = 40

N = int(input("Enter number of requests: "))

for i in range(N):
    request = int(input("Enter seats requested: "))

    if request <= available_seats:
        print("CONFIRMED")
        available_seats -= request
    else:
        print("WAITLISTED")