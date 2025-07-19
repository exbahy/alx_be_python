# match_case_calculator.py
# ده نسخة أسهل وأبسط للآلة الحاسبة باستخدام match case

# 1. بنطلب من اليوزر يدخل الرقم الأول
# هنا بنفترض إن اليوزر هيدخل رقم صح دايماً عشان نسهل الكود عليك
num1 = float(input("Enter the first number: "))
# 2. بنطلب من اليوزر يدخل الرقم الثاني
# برضه بنفترض إنه هيدخل رقم صح
num2 = float(input("Enter the second number: "))

# 3. بنطلب من اليوزر يختار العملية الحسابية
operation = input("Choose the operation (+, -, *, /): ")
# 4. بنستخدم Match Case عشان ننفذ العملية المطلوبة ونطبع النتيجة على طول
match operation: 
    case '+':
        print(f"ther result is {num1+num2}")
          case '-': # لو العملية طرح
        print(f"The result is {num1 - num2}.")
    case '*': # لو العملية ضرب
        print(f"The result is {num1 * num2}.")
    case '/': # لو العملية قسمة
        if num2 == 0: # ده الشرط المهم عشان نمنع القسمة على صفر
            print("Cannot divide by zero.")
        else:
            print(f"The result is {num1 / num2}.")
    case _: # لو اليوزر دخل أي عملية غير اللي فوق (ده الـ default case)
        print("Invalid operation. Please choose one of +, -, *, /.")