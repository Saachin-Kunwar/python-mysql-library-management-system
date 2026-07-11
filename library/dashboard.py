from db import conn, cursor

def dashboard():

    print("\n")
    print("=" * 45)
    print("         LIBRARY DASHBOARD")
    print("=" * 45)

    # Total Books
    cursor.execute("SELECT COUNT(*) FROM books")
    total_books = cursor.fetchone()[0]

    # Available Books
    cursor.execute("""
        SELECT COUNT(*)
        FROM books
        WHERE status='Available'
    """)
    available_books = cursor.fetchone()[0]

    # Borrowed Books
    cursor.execute("""
        SELECT COUNT(*)
        FROM books
        WHERE status='Borrowed'
    """)
    borrowed_books = cursor.fetchone()[0]

    # Total Members
    cursor.execute("SELECT COUNT(*) FROM members")
    total_members = cursor.fetchone()[0]

    # Total Borrow Records
    cursor.execute("SELECT COUNT(*) FROM borrow")
    total_borrow = cursor.fetchone()[0]

    print(f"\n📚 Total Books          : {total_books}")
    print(f"✅ Available Books      : {available_books}")
    print(f"📕 Borrowed Books       : {borrowed_books}")
    print(f"👤 Total Members        : {total_members}")
    print(f"📖 Total Borrow Records : {total_borrow}")

    print("\n" + "=" * 45)