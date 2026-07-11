from book import *
from member import *
from borrow import *
from dashboard import *

while True:
    print("1. Add Book")
    print("2. View Books")
    print("3. Update Book")
    print("4. Delete Book")

    print("5. Add Member")
    print("6. View Members")
    print("7. Update Member")
    print("8. Delete Member")

    print("9. Borrow Book")
    print("10. View Borrowed Books")

    print("11. Return Book")
    print("12. Borrow Book")

    print("13. Search Book")
    print("14. Search Member")

    print("15. Dashboard")

    print("16. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        update_book()

    elif choice == "4":
        delete_book()

    elif choice == "5":
        add_member()

    elif choice == "6":
        view_members()

    elif choice == "7":
        update_member()

    elif choice == "8":
        delete_member()

    elif choice == "9":
        borrow_book()

    elif choice == "10":
        view_borrowed_books()
    
    elif choice == "11":
        return_book()
    
    elif choice == "12":
        borrow_history()
    
    elif choice =="13":
        search_book()
    elif choice =="14":
        search_member()

    elif choice == "15":
        dashboard()
    
    elif choice == "16":

         print("\nThank You")
         break
    
    else:
        print("Invalid Choice!")