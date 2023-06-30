# Defined a function called kelvienToFaherenheit to convert temperature from kelvin to fahrenheit. The function should have an assert that check if the temperature is greater or equal to zero, if not display a message 'Colder that absolute zero' Formula =(k-273.15)*9/5 + 32
def KelvinToFahrenheit(Temperature):
    assert (Temperature >= 0), "Colder than absolute zero!"
    return ((Temperature-273)*1.8)+32


print(KelvinToFahrenheit(273))
print(int(KelvinToFahrenheit(505.78)))
print(KelvinToFahrenheit(-5))
