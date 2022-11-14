def liters_100km_to_miles_gallon(liters):
    gallon_100km = liters / 3.785411784
    miles_gallon = ((gallon_100km/100)/1000)*1609.344
    return(miles_gallon)

def miles_gallon_to_liters_100km(gallon):
    liters_miles = gallon*3.785411784
    liters_100km = (liters_miles/1609.344)*1000*100
    return liters_100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
