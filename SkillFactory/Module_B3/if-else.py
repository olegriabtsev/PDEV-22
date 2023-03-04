is_rainy = True  # дождь будет
heavy_rain = False  # несильный дождь

if is_rainy:
    # в данный блок дописали ещё один условный оператор
    if heavy_rain:
        print("Брать зонт")
    else:
        print("Надеть дождевик")
else:
    print("Не брать зонт")
