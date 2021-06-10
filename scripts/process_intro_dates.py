import os
import shutil
import re

input_folder = '../src-includes'

def process_line(line):
    if 'introduction_date' in line and line.endswith('//fixed_date\n') == False:
        resplit = re.split(' |,|\(|\)', line)
        
        date_list = []
        for i in resplit:
            if i.isnumeric() == True:
                date_list.append(int(i))

        #result = '        introduction_date: date(0,1,1) + (param_date_start * 365) + (((' + str(date_list[0]) + ' - 1900)/199)*(param_date_end-param_date_start) * 365.25);'
        #print(date_list[0])
        position_in_range = (date_list[0] - 1900)# / 199
        #print(position_in_range)
        position_in_range_in_days = position_in_range * 365.25# * 199
        #print(position_in_range_in_days)
        position_in_range_for_nml = int(position_in_range_in_days / 100)
        result = '        introduction_date:            date( param_date_start, 1, 1) + ( ' + str(position_in_range_for_nml) + ' * param_date_multiplier) + 120;\n'
    else:
        result = line
    return result

def process_file(file_path):
    temp_file_path = file_path + '.tmp'
    temp_file = open(temp_file_path, 'w')
    temp_file.close()
    temp_file = open(temp_file_path, 'w')
    with open(file_path, 'r') as nml_file:
        for line in nml_file:
            temp_file.write(process_line(line))
    temp_file.close()
    shutil.copy(temp_file_path, file_path)
    os.remove(temp_file_path)

# for root,dirs,files in os.walk(input_folder):
#     for f in files:
#         if f.endswith('.nml'):
#             f_relpath = os.path.join(root, f)
#             process_file(f_relpath)

process_file('../NUTS-x-combined.nml')
#print(process_line('        introduction_date:            date(2066, 1, 1);'))
