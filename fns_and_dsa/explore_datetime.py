# explore_datetime.py

# أول حاجة وأهم حاجة: بنستورد الحاجات اللي محتاجينها من مكتبة datetime
# - datetime: الكلاس الرئيسي للتعامل مع التاريخ والوقت (مثل 2024-07-27 10:30:00)
# - timedelta: الكلاس للتعامل مع "فترات زمنية" (زي 10 أيام، أو 3 ساعات) عشان نقدر نضيفها أو نطرحها.
from datetime import datetime, timedelta

def display_current_datetime():
    """
    بيجيب التاريخ والوقت الحالي وبيطبعه بتنسيق معين.
    بيرجع كائن datetime عشان ممكن نستخدمه في حسابات تانية.
    """
    # 1. بنجيب التاريخ والوقت الحاليين بالظبط (بالساعة والدقيقة والثانية)
    current_date = datetime.now()

    # 2. بنعمل تنسيق للتاريخ والوقت عشان يظهر بالشكل المطلوب "YYYY-MM-DD HH:MM:SS"
    # strftime() دي دالة بتخلينا نغير شكل التاريخ والوقت لطريقة عرض معينة (string format time)
    # %Y: السنة بأربع أرقام (مثلاً 2024)
    # %m: الشهر كرقم (من 01 لـ 12)
    # %d: اليوم كرقم (من 01 لـ 31)
    # %H: الساعة بنظام 24 ساعة (من 00 لـ 23)
    # %M: الدقائق (من 00 لـ 59)
    # %S: الثواني (من 00 لـ 59)
    formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    # 3. بنطبع التاريخ والوقت الحاليين بعد التنسيق
    print(f"Current date and time: {formatted_current_date}")
    
    # بنرجع الـ current_date كـ datetime object (مش كـ نص)
    # ده مهم عشان الدالة اللي بعدها (calculate_future_date) محتاجة datetime object عشان تعمل عليه عمليات حسابية.
    return current_date

def calculate_future_date(start_date):
    """
    بيطلب من المستخدم يدخل عدد أيام، وبيحسب التاريخ المستقبلي بعد إضافة الأيام دي.
    """
    # 1. بنطلب من اليوزر يدخل عدد الأيام اللي عايز يضيفها.
    # بنحاول نحول الإدخال لرقم صحيح (int) لأننا هنتعامل معاه كرقم.
    # بنستخدم try-except عشان لو اليوزر دخل حاجة مش رقم، البرنامج ميضربش.
    try:
        num_days_str = input("Enter the number of days to add to the current date: ")
        num_days = int(num_days_str)
    except ValueError:
        print("Invalid input. Please enter a whole number for the number of days.")
        return # بنطلع من الدالة لو الإدخال فيه مشكلة عشان ميكملش ويضرب.

    # 2. بنحسب التاريخ المستقبلي:
    # بنضيف الـ timedelta object للـ start_date.
    # timedelta(days=num_days) بتخلق "مدة زمنية" بتساوي عدد الأيام اللي اليوزر دخلها.
    future_date = start_date + timedelta(days=num_days)

    # 3. بنعمل تنسيق للتاريخ المستقبلي عشان يظهر بالشكل المطلوب "YYYY-MM-DD"
    # %Y: السنة
    # %m: الشهر
    # %d: اليوم
    formatted_future_date = future_date.strftime("%Y-%m-%d")

    # 4. بنطبع التاريخ المستقبلي المنسق
    print(f"Future date: {formatted_future_date}")

# ده الجزء الرئيسي من البرنامج اللي بيشتغل لما بتشغل الملف ده مباشرة.
# if __name__ == "__main__": ده بيضمن ان الكود اللي جواه هيتنفذ بس لما تشغل الملف ده مباشرة،
# مش لو الملف ده تم استيراده (import) في ملف تاني.
if __name__ == "__main__":
    # بنستدعي الدالة الأولى عشان تعرض التاريخ والوقت الحاليين.
    # وبنخزن القيمة اللي بترجعها (اللي هي current_date كـ datetime object) في متغير اسمه current_dt.
    current_dt = display_current_datetime()
    
    # بنعمل Check بسيط عشان نتأكد إن display_current_datetime مرجعتش None (لو كان فيه خطأ مثلاً)
    if current_dt:
        # بنستدعي الدالة التانية calculate_future_date وبنديها التاريخ الحالي (اللي هو current_dt)
        calculate_future_date(current_dt)