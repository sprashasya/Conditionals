# Weather Advisory: Check if the temperature is below freezing, above a heat threshold, or within a comfortable range, and provide appropriate advice.
temperature=int(input("enter the temperature: \n"))

if temperature < 0:
    print("Below freezing")
    Advice='Suggest wearing warm clothes, protecting exposed pipes, and being cautious of icy roads and sidewalks.'
elif  0<=temperature<18:
    print("Cool Range")
    Advice=(" Recommend wearing a jacket or sweater and being prepared for potentially chilly conditions, especially in the morning or evening.")
elif 18<=temperature<24:
    print("Comfortable range")
    Advice="Indicate that no special precautions are necessary and that the weather is pleasant for outdoor activities."
elif 24<=temperature<29:
    print("Warm Range")
    Advice="Suggest dressing in light clothing, staying hydrated, and enjoying outdoor activities while being mindful of the heat."
else:
    print("Above Heat")
    Advice="Recommend staying hydrated, wearing light clothing, avoiding strenuous activities during peak heat hours, and staying in shaded or air-conditioned areas if possible."

print("Ai Advice you to ",Advice)