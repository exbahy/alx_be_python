# daily_reminder.py
# ده نسخة أسهل وأبسط لبرنامج التذكير اليومي لمهمة واحدة

print("\n--- Daily Task Reminder ---")

# 1. بنطلب من اليوزر يدخل وصف المهمة
task = input("Enter your task: ")

# 2. بنطلب منه يدخل مستوى الأولوية (Priority)
# بنستخدم .lower() عشان نحول الإدخال لحروف صغيرة، ده مهم للمقارنة
priority = input("Priority (high/medium/low): ").lower()

# 3. بنسأل إذا كانت المهمة دي مرتبطة بوقت معين ولا لأ (Time-bound)
# برضه بنحول الإدخال لحروف صغيرة
time_bound_input = input("Is it time-bound? (yes/no): ").lower()

# بنحول الإجابة بتاعت time_bound_input لـ True أو False عشان تبقى أسهل في جملة الـ if
# لو اليوزر كتب "yes"، المتغير is_time_bound هياخد قيمة True.
# أي حاجة تانية (زي "no" أو أي كلام تاني) هياخد قيمة False.
is_time_bound = (time_bound_input == "yes")

# 4. بنستخدم Match Case عشان نحدد رسالة التذكير بناءً على الأولوية
match priority:
    case "high": # لو الأولوية "high"
        if is_time_bound:
            # لو المهمة مرتبطة بوقت وhigh priority
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            # لو المهمة مش مرتبطة بوقت بس high priority
            print(f"Reminder: '{task}' is a high priority task. Aim to complete it soon.")
    
    case "medium": # لو الأولوية "medium"
        if is_time_bound:
            # لو المهمة مرتبطة بوقت وmedium priority
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            # لو المهمة مش مرتبطة بوقت بس medium priority
            print(f"Reminder: '{task}' is a medium priority task. Try to get it done today.")
    
    case "low": # لو الأولوية "low"
        if is_time_bound:
            # لو المهمة مرتبطة بوقت وlow priority
            print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
        else:
            # ده المثال اللي كان مطلوب منك بالظبط: لو low priority ومش مرتبطة بوقت
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    
    case _: # ده الـ Default Case: لو اليوزر دخل أولوية غلط (غير high/medium/low)
        print("Invalid priority level. Please choose high, medium, or low.")

print("\nDaily reminder process finished.")