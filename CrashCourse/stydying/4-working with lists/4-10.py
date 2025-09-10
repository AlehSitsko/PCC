# cars list
cars = ['bmw', 'audi', 'toyota', 'subaru', 'ford', 'honda']
# Print the message with first three cars
print("The first three cars in the list are:")
for car in cars[:3]:
    print(car.title())
# Print the message with three middle cars
print("The three middle cars in the list are:")
for car in cars[1:4]:
    print(car.title())
# Print the message with last three cars
print("The last three cars in the list are:")
for car in cars[-3:]:
    print(car.title())