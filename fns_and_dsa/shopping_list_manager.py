
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item: ")
            shopping_list.append(item)
            
        elif choice == '2':
            item = input("Enter the item: ")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print(f"{item} not found in the list")
                
        elif choice == '3':
            for item in shopping_list:
                print(item)
                
        elif choice == '4':
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
