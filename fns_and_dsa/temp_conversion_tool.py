# temp_conversion_tool.py

# 1. تعريف المتغيرات العامة (Global Conversion Factors)
# تأكد ان السطور دي بالظبط زي ما هي، خصوصاً الارقام وعلامات القسمة ومفيش اقواس
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 # 5/9 بدون اقواس وبدون مسافات زيادة
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5 # 9/5 بدون اقواس وبدون مسافات زيادة

# 2. تعريف دوال التحويل

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.
    Uses the global FAHRENHEIT_TO_CELSIUS_FACTOR.

    Args:
        fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature converted to Celsius.
    """
    # بنستخدم الـ Global Factor في المعادلة
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.
    Uses the global CELSIUS_TO_FAHRENHEIT_FACTOR.

    Args:
        celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature converted to Fahrenheit.
    """
    # بنستخدم الـ Global Factor في المعادلة
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# 3. الجزء الرئيسي للتعامل مع اليوزر (Main User Interaction)
if __name__ == "__main__":
    while True: # بنعمل loop عشان لو اليوزر دخل حاجة غلط، يقدر يحاول تاني
        try:
            # بنطلب من اليوزر يدخل درجة الحرارة
            temp_str = input("Enter the temperature to convert: ")
            # بنحاول نحول الإدخال لرقم عشري (float).
            # لو الإدخال مش رقم، هيحصل ValueError هنا.
            temperature = float(temp_str)

            # بنطلب من اليوزر يحدد الوحدة (C أو F)
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

            if unit == 'C':
                # لو الوحدة سيلزيوس، بنحولها لفهرنهايت
                converted_temp = convert_to_fahrenheit(temperature)
                # بنطبع النتيجة بالشكل المطلوب بالضبط
                print(f"{temperature}°C is {converted_temp}°F")
                break # بنطلع من الـ loop لأن العملية تمت بنجاح
            elif unit == 'F':
                # لو الوحدة فهرنهايت، بنحولها لسيلزيوس
                converted_temp = convert_to_celsius(temperature)
                # بنطبع النتيجة بالشكل المطلوب بالضبط
                print(f"{temperature}°F is {converted_temp}°C")
                break # بنطلع من الـ loop لأن العملية تمت بنجاح
            else:
                # لو اليوزر دخل وحدة غير C أو F
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
                # الـ loop هتلف تاني عشان اليوزر يدخل بيانات جديدة
        
        except ValueError:
            # لو حصل ValueError (يعني float(temp_str) فشل)، بنطبع رسالة الخطأ دي
            # النص ده لازم يكون بالظبط زي ما الـ checker بيدور عليه
            print("Invalid temperature. Please enter a numeric value.")
            # الـ loop هتلف تاني عشان اليوزر يدخل بيانات جديدة
        except Exception as e:
            # ده عشان نمسك أي أخطاء تانية غير متوقعة
            print(f"An unexpected error occurred: {e}")
            break