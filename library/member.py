from db import conn, cursor

def add_member():

    print("\n===== Add New Member =====")

    name = input("Enter Full Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone Number: ")
    city = input("Enter City (Leave blank for default): ")

    if city == "":
        city = None

    query = """
        INSERT INTO members(full_name, email, phone, city)
        VALUES(%s, %s, %s, %s)
    """

    try:
        cursor.execute(query, (name, email, phone, city))
        conn.commit()
        print("\n✅ Member Added Successfully!")

    except Exception as e:
        print("\n❌ Error:", e)

def view_members():

    print("\n========== MEMBER LIST ==========")

    cursor.execute("SELECT * FROM members")

    members = cursor.fetchall()

    if not members:
        print("No Members Found.")
        return

    print("-" * 75)
    print(f"{'ID':<5}{'Name':<25}{'Email':<25}{'Phone':<15}")
    print("-" * 75)

    for member in members:
        print(f"{member[0]:<5}{member[1]:<25}{member[2]:<25}{member[3]:<15}")

def update_member():

    print("\n===== Update Member =====")

    member_id = int(input("Enter Member ID: "))

    name = input("New Name: ")
    email = input("New Email: ")
    phone = input("New Phone: ")

    query = """
        UPDATE members
        SET full_name=%s,
            email=%s,
            phone=%s
        WHERE member_id=%s
    """

    cursor.execute(query, (name, email, phone, member_id))
    conn.commit()

    print("✅ Member Updated Successfully")

def delete_member():

    print("\n===== Delete Member =====")

    member_id = int(input("Enter Member ID: "))

    query = "DELETE FROM members WHERE member_id=%s"

    cursor.execute(query, (member_id,))
    conn.commit()

    print("✅ Member Deleted Successfully")


def search_member():

    print("\n========== Search Member ==========")

    keyword = input("Enter Member Name: ").strip()

    query = """
    SELECT *
    FROM members
    WHERE full_name LIKE %s
    """

    cursor.execute(query, ('%' + keyword + '%',))

    members = cursor.fetchall()

    if not members:
        print("\n❌ No Member Found.")
        return

    print()

    print(f"{'ID':<5}{'Name':<25}{'Email':<30}{'Phone'}")
    print("-"*90)

    for member in members:

        print(
            f"{member[0]:<5}"
            f"{member[1]:<25}"
            f"{member[2]:<30}"
            f"{member[3]}"
        )