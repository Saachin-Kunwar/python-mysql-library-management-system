from db import conn, cursor

def borrow_book():

    print("\n===== Borrow Book =====")

    member_id = int(input("Enter Member ID: "))
    book_id = int(input("Enter Book ID: "))
    borrow_date = input("Enter Borrow Date (YYYY-MM-DD): ")
    return_date = input("Enter Return Date (YYYY-MM-DD): ")

    # पहिले Book Available छ कि छैन जाँच गर्ने
    cursor.execute(
        "SELECT status FROM books WHERE book_id=%s",
        (book_id,)
    )

    result = cursor.fetchone()

    if result is None:
        print("❌ Book ID not found.")
        return

    if result[0] == "Borrowed":
        print("❌ This book is already borrowed.")
        return

    try:

        query = """
        INSERT INTO borrow(member_id, book_id, borrow_date, return_date)
        VALUES(%s,%s,%s,%s)
        """

        cursor.execute(query, (member_id, book_id, borrow_date, return_date))

        # Book status update
        cursor.execute(
            "UPDATE books SET status='Borrowed' WHERE book_id=%s",
            (book_id,)
        )

        conn.commit()

        print("\n✅ Book Borrowed Successfully")

    except Exception as e:
        print("❌ Error :", e)

def view_borrowed_books():

    print("\n========== Borrowed Books ==========")

    query = """
    SELECT

        borrow.borrow_id,
        members.full_name,
        books.title,
        borrow.borrow_date,
        borrow.return_date

    FROM borrow

    JOIN members
        ON borrow.member_id = members.member_id

    JOIN books
        ON borrow.book_id = books.book_id
    """

    cursor.execute(query)

    data = cursor.fetchall()

    if not data:
        print("No Borrow Records Found.")
        return

    print("-"*90)
    print(f"{'ID':<5}{'Member':<25}{'Book':<25}{'Borrow':<15}{'Return'}")
    print("-"*90)

    for row in data:

        print(
            f"{row[0]:<5}"
            f"{row[1]:<25}"
            f"{row[2]:<25}"
            f"{str(row[3]):<15}"
            f"{row[4]}"
        )

from db import conn, cursor

def return_book():

    print("\n========== Return Book ==========")

    borrow_id = int(input("Enter Borrow ID: "))

    # Borrow Record खोज्ने
    cursor.execute(
        "SELECT book_id, status FROM borrow WHERE borrow_id=%s",
        (borrow_id,)
    )

    data = cursor.fetchone()

    if data is None:
        print("❌ Borrow Record Not Found")
        return

    if data[1] == "Returned":
        print("❌ Book Already Returned")
        return

    book_id = data[0]

    try:

        # Borrow Status Update
        cursor.execute(
            """
            UPDATE borrow
            SET status='Returned'
            WHERE borrow_id=%s
            """,
            (borrow_id,)
        )

        # Book Status Available
        cursor.execute(
            """
            UPDATE books
            SET status='Available'
            WHERE book_id=%s
            """,
            (book_id,)
        )

        conn.commit()

        print("✅ Book Returned Successfully")

    except Exception as e:
        print("❌ Error :", e)

def borrow_history():

    query = """
    SELECT

    borrow.borrow_id,
    members.full_name,
    books.title,
    borrow.borrow_date,
    borrow.return_date,
    borrow.status

    FROM borrow

    JOIN members
        ON borrow.member_id=members.member_id

    JOIN books
        ON borrow.book_id=books.book_id
    """

    cursor.execute(query)

    records = cursor.fetchall()

    print("\n========== Borrow History ==========")

    print("-"*110)
    print(f"{'ID':<5}{'Member':<25}{'Book':<25}{'Borrow':<15}{'Return':<15}{'Status'}")
    print("-"*110)

    for row in records:

        print(
            f"{row[0]:<5}"
            f"{row[1]:<25}"
            f"{row[2]:<25}"
            f"{str(row[3]):<15}"
            f"{str(row[4]):<15}"
            f"{row[5]}"
        )