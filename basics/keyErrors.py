car_owned_by = {'Vusal': 'BMW', 'Michael': 'Zapi', 'John': 'Mercedes'}
cars = []



for owner in ('Vusal', 'Mamed', 'Milashka'):
    default = 'He does not have a car'
    cars.append(car_owned_by.setdefault(owner, default))
print(cars)


# dogs = {'Dogname': 'Buldog'}
# default = 'There is no name for this dog'
# a = dogs.get('dogname', default); print(a)
