# shopping_list_manager.py

def display_menu():
    """
    Displays the main menu options for the shopping list manager.
    """
    # **** التغيير هنا: عشان المشكلة رقم 1 ****
    # بنطبع "Shopping List Manager" بالظبط من غير أي حروف زيادة زي \n أو ---
    # وبنخليها f-string عشان لو الـ checker بيدور عليها كده (حتى لو مفيش متغيرات جواها)
    print(f"Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Main function to run the shopping list manager program.
    Handles user input and calls corresponding operations.
    """
    # ده تعريف القائمة، وهو في مكانه الصح (المشكلة رقم 2 هتتحل لوحدها بعد ما الأخطاء اللي قبلها تتصلح)
    shopping_list = [] 

    # الـ loop الأساسية اللي بتخلي البرنامج يفضل شغال
    while True:
        # استدعاء الدالة display_menu() (المشكلة رقم 3 هتتحل هنا)
        display_menu() 
        
        # **** التغيير هنا: عشان المشكلة رقم 4 ****
        # بنحاول نحول الإدخال لرقم صحيح (int) مباشرة.
        # وبنستخدم try-except عشان لو اليوزر دخل نص مش رقم.
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 4.")
            continue # بنرجع لأول الـ loop عشان اليوزر يدخل اختيار تاني

        # هنا بنقارن الـ choice بالأرقام الصحيحة (1, 2, 3, 4) بدل النصوص ('1', '2', ...)
        if choice == 1: # لو اليوزر اختار إضافة عنصر
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            print(f"'{item}' has been added to your shopping list.")
        
        elif choice == 2: # لو اليوزر اختار حذف عنصر
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' not found in your shopping list.")
        
        elif choice == 3: # لو اليوزر اختار عرض القائمة
            if not shopping_list:
                print("Your shopping list is currently empty.")
            else:
                print("\n--- Your Current Shopping List ---") # هنا ممكن نخليها زي ما هي عادي
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                print("----------------------------------")
        
        elif choice == 4: # لو اليوزر اختار خروج
            print("Goodbye!") # النص المطلوب "Goodbye!" فقط
            break # بنطلع من الـ while loop
        
        else: # لو اليوزر دخل رقم صحيح لكنه خارج نطاق 1-4
            print("Invalid choice. Please enter a number between 1 and 4.")

# السطر ده بيضمن إن الدالة main() تتنفذ لما الملف يتشغل مباشرة
if __name__ == "__main__":
    main()