# shopping_list_manager.py

def display_menu():
    """
    Displays the main menu options for the shopping list manager.
    """
    print("\n--- Shopping List Manager ---") # \n بتنزل سطر جديد عشان المنظر يبقى أحسن
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print("----------------------------")

def main():
    """
    Main function to run the shopping list manager program.
    Handles user input and calls corresponding operations.
    """
    shopping_list = [] # دي القائمة الفاضية اللي هنخزن فيها مشترياتنا

    # دي الـ loop الأساسية اللي بتخلي البرنامج يفضل شغال لحد ما اليوزر يختار خروج
    while True:
        display_menu() # بنعرض القائمة لليوزر
        # بناخد اختيار اليوزر وبنشيل أي مسافات زيادة قبل أو بعد الرقم
        choice = input("Enter your choice: ").strip() 

        if choice == '1': # لو اليوزر اختار إضافة عنصر
            item = input("Enter the item to add: ").strip() # بناخد اسم العنصر وبنشيل المسافات الزايدة
            shopping_list.append(item) # بنضيف العنصر للقائمة في آخرها
            print(f"'{item}' has been added to your shopping list.")
        
        elif choice == '2': # لو اليوزر اختار حذف عنصر
            item = input("Enter the item to remove: ").strip() # بناخد اسم العنصر اللي عايز يحذفه
            if item in shopping_list: # بنشوف هل العنصر ده موجود في القائمة أصلاً؟
                shopping_list.remove(item) # لو موجود، بنحذفه
                print(f"'{item}' has been removed from your shopping list.")
            else: # لو العنصر مش موجود في القائمة
                print(f"'{item}' not found in your shopping list.")
        
        elif choice == '3': # لو اليوزر اختار عرض القائمة
            if not shopping_list: # بنشوف هل القائمة فاضية (if not shopping_list يعني لو القائمة فاضية)
                print("Your shopping list is currently empty.")
            else:
                print("\n--- Your Current Shopping List ---")
                # بنلف على القائمة ونطبع كل عنصر برقمه
                # enumerate بتديني رقم العنصر (i) والعنصر نفسه (item)
                # 1, معناها ابدأ الترقيم من 1 مش من 0 (لأن القوائم بتبدأ من 0)
                for i, item in enumerate(shopping_list, 1): 
                    print(f"{i}. {item}")
                print("----------------------------------")
        
        elif choice == '4': # لو اليوزر اختار خروج
            print("Goodbye! Happy shopping!")
            break # بنطلع من الـ while loop، وده بيوقف البرنامج
        
        else: # لو اليوزر دخل أي رقم أو حرف مش في القائمة
            print("Invalid choice. Please enter a number between 1 and 4.")

# السطر ده مهم عشان الكود اللي جوه main() يتنفذ بس لما تشغل الملف ده مباشرة
# ومش هيتنفذ لو الملف ده تم استيراده (import) في ملف تاني.
if __name__ == "__main__":
    main()