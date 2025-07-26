# shopping_list_manager.py

def display_menu():
    print("\nShopping List Manager") # \n بتنزل سطر جديد عشان المنظر يبقى أحسن
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = [] # دي القائمة الفاضية اللي هنخزن فيها مشترياتنا

    while True: # دي الـ loop الأساسية اللي بتخلي البرنامج يفضل شغال لحد ما اليوزر يختار خروج
        display_menu() # بنعرض القائمة لليوزر
        choice = input("Enter your choice: ").strip() # بناخد اختيار اليوزر وبنشيل أي مسافات زيادة

        if choice == '1': # لو اليوزر اختار إضافة
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item) # بنضيف العنصر للقائمة في آخرها
            print(f"'{item}' added to the list.")
        elif choice == '2': # لو اليوزر اختار حذف
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list: # بنشوف هل العنصر ده موجود في القائمة أصلاً؟
                shopping_list.remove(item) # لو موجود، بنحذفه
                print(f"'{item}' removed from the list.")
            else: # لو مش موجود
                print(f"'{item}' not found in the list.")
        elif choice == '3': # لو اليوزر اختار عرض القائمة
            if not shopping_list: # بنشوف هل القائمة فاضية؟
                print("Your shopping list is empty.")
            else:
                print("\n--- Your Shopping List ---")
                for i, item in enumerate(shopping_list, 1): # بنلف على القائمة ونطبع كل عنصر برقمه
                    # enumerate بتديني رقم العنصر (i) والعنصر نفسه (item)
                    # 1, معناها ابدأ الترقيم من 1 مش من 0
                    print(f"{i}. {item}")
                print("--------------------------")
        elif choice == '4': # لو اليوزر اختار خروج
            print("Goodbye!")
            break # بنطلع من الـ while loop، وده بيوقف البرنامج
        else: # لو اليوزر دخل أي رقم أو حرف مش في القائمة
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()