from db import conn, cursor

def add_book():
    print("\n===== Add New Book =====")

    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    isbn = input("Enter ISBN: ")
    price = float(input("Enter Price: "))

    query = """
        INSERT INTO books(title, author, isbn, price)
        VALUES(%s, %s, %s, %s)
    """

    values = (title, author, isbn, price)

    try:
        cursor.execute(query, values)
        conn.commit()
        print("\n✅ Book Added Successfully!")

    except Exception as e:
        print("\n❌ Error:", e)

def view_books():

    print("\n========= BOOK LIST =========")

    cursor.execute("SELECT * FROM books")

    books = cursor.fetchall()

    if not books:
        print("No Books Found.")
        return

    for book in books:
        print(book)

def update_book():

    print("\n===== Update Book =====")

    book_id = int(input("Enter Book ID: "))

    title = input("Enter New Title: ")
    author = input("Enter New Author: ")
    price = float(input("Enter New Price: "))

    query = """
        UPDATE books
        SET title=%s,
            author=%s,
            price=%s
        WHERE book_id=%s
    """

    values = (title, author, price, book_id)

    cursor.execute(query, values)
    conn.commit()

    print("✅ Book Updated Successfully")

def delete_book():

    print("\n===== Delete Book =====")

    book_id = int(input("Enter Book ID: "))

    query = "DELETE FROM books WHERE book_id=%s"

    cursor.execute(query, (book_id,))
    conn.commit()

    print("✅ Book Deleted Successfully")

def search_book():

    print("\n========== Search Book ==========")

    keyword = input("Enter Book Title: ").strip()

    query = """
    SELECT *
    FROM books
    WHERE title LIKE %s
    """

    cursor.execute(query, ('%' + keyword + '%',))

    books = cursor.fetchall()

    if not books:
        print("\n❌ No Book Found.")
        return

    print("\n=========== Search Result ===========")

    print(f"{'ID':<5}{'Title':<30}{'Author':<20}{'Price':<10}{'Status'}")
    print("-"*80)

    for book in books:
        print(
            f"{book[0]:<5}"
            f"{book[1]:<30}"
            f"{book[2]:<20}"
            f"{book[4]:<10}"
            f"{book[5]}"
        )