

# car_owned_by = {'Vusal': 'BMW', 'Michael': 'Zapi', 'John': 'Mercedes'}
# cars = []


# for car in car_owned_by:
#     print(car) #prints keys not values

# for car in car_owned_by.keys():
#     print(car) #prints keys

# for car in car_owned_by.values():
#     print(car)





""" ========================================= """

# for (owners, cars) in car_owned_by.items():
#     print("{0} ownes {1}".format(owners, cars))


# dog_owners = {'Vusal': 'Husky', 'Mamed': 'Puppy', 'Milashka': 'Buldog'}


# for (owner, dog) in dog_owners.items():
#     print("{0} ownes {1}".format(owner, dog))


# del dog_owners['Milashka']
# print(dog_owners)




""" ========================================= """

# countries = { 'AZ': 'Azerbaijan', 'TR': 'Turkey', 'RU': 'Russia', 'USA': "United States of America"}

# for (code, country) in countries.items():
#     print('<option val="{0}">{1}</option>'.format(code, country)) #generate html tags




""" ========================================= """

# thumbnail = None

# condition = "Cloudy"

# if condition == "Cloudy": thumbnail = "cloudy.png"
# print(thumbnail)

# if condition == "Rainy": thumbnail = "rainy.png"
# print(thumbnail)

#replace if else with the dictionary
#if we get weather condition from database, we can just simply change the thumbnail using dict


""" ==================================== """

# weather = {"Cloudy": "cloudy.png", "Rainy": "rainy.png"}
# print(weather[condition])

# thumbnail = weather.get(condition)
# print(thumbnail)

# #we can set default thumbnail image to handle key errors
# condition = "keyError"
# default = "default.png"
# thumbnail = weather.setdefault(condition, default)
# print(thumbnail)



""" ========================================= """
#nested dicts
# users = { 
#     1: { "name": "Vusal", "email": "mail@vhasanov.com"},
#     2: { "name": "Vendetta", "email": "vforvendetta@mail.com"}        
#         }