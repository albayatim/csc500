def calculate_book_club_points():
    books_purchased = int(input("Enter the number of books purchased this month: "))
    points = 0

    if books_purchased == 0:
        points = 0
    elif books_purchased == 2:
        points = 5
    elif books_purchased == 4:
        points = 15
    elif books_purchased == 6:
        points = 30
    elif books_purchased >= 8:
        points = 60

    print(f"Points awarded: {points}")

calculate_book_club_points()