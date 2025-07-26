# arithmetic_operations.py

# ده تعريف الدالة perform_operation.
# تأكد ان السطر ده (سطر التعريف) بالظبط زي ما هو كده:
# - الاسم perform_operation مكتوب صح.
# - الاقواس وفيها num1, num2, operation بالترتيب ده وبنفس الاسماء.
# - النقطتين اللي في الاخر : موجودة.
def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations based on input.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The type of operation ('add', 'subtract', 'multiply', 'divide').

    Returns:
        float or str: The result of the operation, or an error message if division by zero or invalid operation.
    """
    
    # الكود ده بيخلي الـ operation كلها حروف صغيرة وبيشيل المسافات الزيادة
    # ده بيضمن ان لو اليوزر كتب "Add" او " ADD "، الدالة تتعرف عليها صح
    # main.py بيعمل كده اصلا، بس حلو ان الدالة تكون قوية لوحدها
    operation = operation.strip().lower()

    # بنستخدم Match Case عشان ننفذ العملية المطلوبة بناءً على قيمة operation
    match operation:
        case 'add':
            return num1 + num2 # لو العملية "add"، بنرجع نتيجة الجمع
        case 'subtract':
            return num1 - num2 # لو العملية "subtract"، بنرجع نتيجة الطرح
        case 'multiply':
            return num1 * num2 # لو العملية "multiply"، بنرجع نتيجة الضرب
        case 'divide':
            if num2 == 0: # ده شرط مهم جداً: لو بنقسم على صفر
                # بنرجع رسالة خطأ محددة عشان main.py يعرف يتعامل معاها
                return "Error: Cannot divide by zero"
            else:
                return num1 / num2 # لو القسمة صحيحة، بنرجع النتيجة
        case _: # ده الـ default case (case _) لو operation مش واحدة من اللي فوق
            # بنرجع رسالة خطأ ان العملية غير صالحة
            return "Error: Invalid operation"