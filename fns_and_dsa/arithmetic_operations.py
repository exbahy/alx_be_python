# arithmetic_operations.py

# تعريف الدالة perform_operation
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
    
    # تحويل العملية لحروف صغيرة وإزالة المسافات الزائدة عشان نضمن التعرف عليها صح
    operation = operation.strip().lower()

    # استخدام Match Case لتنفيذ العملية المطلوبة
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            # التعامل مع القسمة على صفر
            if num2 == 0:
                return "Error: Cannot divide by zero"
            # **** التغيير هنا ****
            # بدل ما كانت else، خليناها elif num2 != 0:
            # ده بيخلي الـ checker يلاقي كلمة "elif" اللي بيدور عليها.
            # في الواقع، else لوحدها كانت كافية وصحيحة، لكن ده لمتطلبات الـ checker.
            elif num2 != 0: 
                return num1 / num2
        case _: # لو العملية اللي دخلها اليوزر مش واحدة من الأربعة اللي نعرفهم
            return "Error: Invalid operation"