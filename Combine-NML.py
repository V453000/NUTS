import os
from subprocess import Popen

def process_line(line, prefix, output_nml):
  if prefix in line:
    output_nml.write(line)
    filename_to_import = line[prefix_length:][:-1]
    if os.path.isfile(filename_to_import):
      with open(filename_to_import,'r') as file_to_import:
        file_to_import = open(filename_to_import, 'r')
        for l in file_to_import:
          process_line(l, prefix, output_nml)
          #output_nml.write(l)
        print('Included', filename_to_import)
    else:
      print(filename_to_import, 'NOT FOUND!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      #raise Exception(filename_to_import, 'NOT FOUND!!!')
  else:
    output_nml.write(line)

main_nml = open('NUTS.nml', 'r')
output_nml = open('NUTS-x-combined.nml', 'w')
output_nml.close() # clear the content of the file
output_nml = open('NUTS-x-combined.nml', 'w')

prefix = '//#include '
prefix_length = len(prefix)

for line in main_nml:
  process_line(line, prefix, output_nml)

main_nml.close()
output_nml.close()

script_path = os.path.realpath(__file__)
script_folder = os.path.dirname(script_path)
#compiling = Popen('compile.bat', cwd=script_folder, shell = True)
#compiling = Popen('C:/NML/nmlc -c --default-lang=english.lng --grf=PART.grf PART-x-combined.nml', cwd=script_folder, shell = False)

print('Success! NML combined.')
