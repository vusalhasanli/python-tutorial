import csv


with open('users.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([ 'id', 'email', 'name'])
    writer.writerow([ 1, 'mail@example.com', 'mail'])
    writer.writerow([ 2, 'some@example.com', 'some'])
    writer.writerow([ 3, 'another@example.com', 'This is "another" , user'])
