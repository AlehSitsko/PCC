# Cars
def make_car(manufacturer, model, **car_info):
    """ Build a dictionary containing everything we know about a car. """
    car_info['manufacturer'] = manufacturer.title()
    car_info['model'] = model.title()
    return car_info
# Call the function with different car information
car1 = make_car('subaru', 'outback', color='blue', tow_package=True)
car2 = make_car('tesla', 'model s', color='red', autopilot=True, battery='long range')
car3 = make_car('ford', 'mustang', color='black', convertible=True, horsepower=450)
# Display the car profiles
print(car1)
print(car2)
print(car3)