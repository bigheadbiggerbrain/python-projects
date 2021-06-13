number_of_temperatures = 0
sum_of_temperatures = 0

while (number_of_temperatures<32):
      temperatures = int(input("Introduce the temperature "))
      sum_of_temperatures = temperatures + sum_of_temperatures
      number_of_temperatures = number_of_temperatures + 1
      
average = sum_of_temperatures + number_of_temperatures
print(average)