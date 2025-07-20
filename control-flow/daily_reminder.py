# daily_reminder.py
# ده الكود اللي هيعدي من الـ Checker بتاع ALX

print("\n--- Daily Task Reminder ---")

# 1. بنطلب من اليوزر يدخل وصف المهمة
task = input("Enter your task: ")

# 2. بنطلب منه يدخل مستوى الأولوية (Priority)
# بنستخدم .lower() عشان نحول الإدخال لحروف صغيرة، ده مهم للمقارنة
priority = input("Priority (high/medium/low): ").lower()

# 3. بنسأل إذا كانت المهمة دي مرتبطة بوقت معين ولا لأ (Time-bound)
# برضه بنحول الإدخال لحروف صغيرة
# ********* هنا التعديل المهم *********
# هنحتفظ بقيمة الإدخال زي ما هي في المتغير time_bound_input
time_bound_input = input("Is it time-bound? (yes/no): ").lower()


# 4. بنستخدم Match Case عشان نحدد رسالة التذكير بناءً على الأولوية
match priority:
    case "high": # لو الأولوية "high"
        # ********* هنا التعديل المهم *********
        # بنستخدم time_bound_input مباشرة وبنقارنها بـ "yes"
        if time_bound_input == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Aim to complete it soon.")
    
    case "medium": # لو الأولوية "medium"
        # ********* هنا التعديل المهم *********
        # بنستخدم time_bound_input مباشرة وبنقارنها بـ "yes"
        if time_bound_input == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Try to get it done today.")
    
    case "low": # لو الأولوية "low"
        # ********* هنا التعديل المهم *********
        # بنستخدم time_bound_input مباشرة وبنقارنها بـ "yes"
        if time_bound_input == "yes":
            print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
        else:
            # ده المثال اللي كان مطلوب منك بالظبط: لو low priority ومش مرتبطة بوقت
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    
    case _: # ده الـ Default Case: لو اليوزر دخل أولوية غلط (غير high/medium/low)
        print("Invalid priority level. Please choose high, medium, or low.")

print("\nDaily reminder process finished.")