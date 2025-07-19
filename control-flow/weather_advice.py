weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
# لو الجو مش مشمس، بنشوف هل هو "ممطر" (rainy)
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
# لو مش ممطر، بنشوف هل هو "بارد" (cold)
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
# لو ولا حاجة من اللي فوق، يبقى ده "else" (أي حاجة تانية)
else:
    print("Sorry, I don't have recommendations for this weather.")