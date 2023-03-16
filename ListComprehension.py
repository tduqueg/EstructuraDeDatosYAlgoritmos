# Comprender las listas nos permite crear nuevsa listas basadas en 
#los valores de una lista ya existente

numbers = [1,-5,0,2435,6,3,234,-85,3,75,23]

new_list=[num for num in numbers if num % 2 == 0]

print(new_list)

names = ["Juan","Tomás", "Miguel", "Sebastian", "Esteban", "Daniel"]

filtered_names = [name for name in names if len(name) == 6]

print(filtered_names)