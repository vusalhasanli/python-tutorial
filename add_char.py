import os



path = './files.timestamp'

with open (path, 'r+') as plain_text:
    numbers = plain_text.readlines()
    # print(numbers)
    frame_id = 0
    final_numbers = ''
    for n in numbers:
        fin_numbers = str(frame_id) + ' ' + n
        frame_id +=1
        final_numbers += fin_numbers
print(final_numbers)





# with open (path, 'w+') as old_file:
#     old_file = open(path, 'w+')
#     n = plain_text.write(final_numbers)

    


        




    # frame_id = '0'
    # second = chr(ord(frame_id[0])+1)
    # print(type(second))
# add_id = frame_id + ' ' + n
#         frame_id = chr(ord(frame_id[0])+1)
#         final_numbers += add_id
#     print(final_numbers)