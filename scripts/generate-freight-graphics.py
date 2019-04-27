import math

with open('generated-freight-graphics.nml', 'w') as output_nml:
  for i in range(1, 65):
    # write _end version
    if i>1:
      output_nml.write('switch(FEAT_TRAINS, SELF, switch_railmedium9_graphics_both_draw' + str(i) + '_end, position_in_consist_from_end){\n')
      i_half = float(i)/2
      i_test = math.floor(i_half)
      i_range = int(i_test-1)
      i_text = '..' + str(i_range)
      if i_range == 0:
        i_text = ''
      
      output_nml.write('  ' + '0' + i_text + ': switch_rail_freight_vehid_back;\n')
      output_nml.write('  switch_rail_freight_vehid_wagons;\n')
      output_nml.write('}\n')

    # write switch without _end
    output_nml.write('switch(FEAT_TRAINS, SELF, switch_railmedium9_graphics_both_draw' + str(i) + ', position_in_consist){\n')
    i_half = float(i)/2
    i_test = math.ceil(i_half)
    i_range = int(i_test-1)
    i_text = '..' + str(i_range)
    if i_range == 0:
      i_text = ''
    
    output_nml.write('  ' + '0' + i_text + ': switch_rail_freight_vehid_front;\n')
    if i>1:
      output_nml.write('  switch_railmedium9_graphics_both_draw' + str(i) + '_end;\n')
    else:
      output_nml.write('  switch_rail_freight_vehid_wagons;\n')
    output_nml.write('}\n')

  output_nml.write('switch(FEAT_TRAINS, PARENT, switch_railmedium9_graphics_both, count_veh_id(47)){\n')
  for i in range(0,64):
    output_nml.write('  ' + str(i*2+1) + '..' + str(i*2+2) + ': switch_railmedium9_graphics_both_draw' + str(i+1) + ';\n')
  output_nml.write('  switch_railmedium9_graphics_both_draw64;\n')
  output_nml.write('}\n')


  for i in range(1, 65):
    output_nml.write('switch(FEAT_TRAINS, SELF, switch_railmedium9_graphics_front_draw' + str(i) + ', position_in_consist){\n')
    output_nml.write('  0..' + str(i-1) + ': switch_rail_freight_vehid_front;\n')
    output_nml.write('  switch_rail_freight_vehid_wagons;\n')
    output_nml.write('}\n')
  output_nml.write('switch(FEAT_TRAINS, PARENT, switch_railmedium9_graphics_front, count_veh_id(47)){\n')
  for i in range(0,64):
    output_nml.write('  ' + str(i*2+1) + '..' + str(i*2+2) + ': switch_railmedium9_graphics_front_draw' + str(i+1) + ';\n')
  output_nml.write('  switch_railmedium9_graphics_front_draw64;\n')
  output_nml.write('}\n')
  