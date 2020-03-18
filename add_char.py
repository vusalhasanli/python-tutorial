import os



# ---- Adding ids to each line of the text in a file
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
# print(final_numbers)

# ---- writing new text to a file
path2 = '/Users/vusal/Desktop/Office/scripts/files1.timestamp'
with open (path2, 'w') as output_file:
    for l in final_numbers:
        output_file.write(l)