import math

with open('generated-freight-short-graphics.nml', 'w') as output_nml:
  for i in range(1, 65):

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    # dual headed drawing ---------------------------------------------------------------------------------------------------------------------------

    # write _end version
    if i>1:
      # write switch header
      output_nml.write('switch(FEAT_TRAINS, SELF, switch_rail_freight_short_graphics_both_draw' + str(i) + '_end, position_in_consist_from_end){\n')
      # do stuff with i
      i_half = float(i)/2
      i_test = math.floor(i_half)#floor for _end
      i_range = int(i_test-1)
      # define i_text, change it if i == 0
      i_text = '..' + str(i_range)
      if i_range == 0:
        i_text = ''
      
      # define which spritesheet is to be used
      spritesheet = 'switch_rail_freight_short_vehid_back;\n'
      default_spritesheet = '  switch_rail_freight_short_vehid_wagons_self;\n'
      
      for n in range(0, int(i_test*1)):
        #if (n%2)==0:
        #  spritesheet = 'sprite_INVISIBLE;\n'
        #else:
        spritesheet = 'switch_rail_freight_short_vehid_back;\n'
        output_nml.write('  ' + str(n) + ': ' + spritesheet)
      output_nml.write(default_spritesheet)
      output_nml.write('}\n')

    # write switch without _end
    # write switch header
    output_nml.write('switch(FEAT_TRAINS, SELF, switch_rail_freight_short_graphics_both_draw' + str(i) + ', position_in_consist){\n')
    # do stuff with i
    i_half = float(i)/2
    i_test = math.ceil(i_half)#floor for _end
    i_range = int(i_test-1)
    # define i_text, change it if i == 0
    i_text = '..' + str(i_range)
    if i_range == 0:
      i_text = ''
    
    # define which spritesheet is to be used
    spritesheet = 'switch_rail_freight_short_vehid_front;\n'
    default_spritesheet = '  switch_rail_freight_short_graphics_both_draw' + str(i) + '_end;\n'
    
    for n in range(0, int(i_test*2)):
      if (n%2)==0:
        spritesheet = 'sprite_INVISIBLE;\n'
      else:
        spritesheet = 'switch_rail_freight_short_vehid_front;\n'
      output_nml.write('  ' + str(n) + ': ' + spritesheet)
    output_nml.write(default_spritesheet)
    output_nml.write('}\n')


  # both drawing switch
  output_nml.write('switch(FEAT_TRAINS, PARENT, switch_rail_freight_short_graphics_both,\n')
  output_nml.write('  count_veh_id(7) + // rail EARLY 01\n')
  output_nml.write('  count_veh_id(8) +\n')
  output_nml.write('  count_veh_id(9) + // rail EARLY 03\n')
  output_nml.write('  count_veh_id(11) + // railstrong1\n')
  output_nml.write('  count_veh_id(13) +\n')
  output_nml.write('  count_veh_id(15) + //railstrong3\n')
  output_nml.write('  count_veh_id(31) + //railmedium1\n')
  output_nml.write('  count_veh_id(33) +\n')
  output_nml.write('  count_veh_id(35) + //raiilmedium3\n')
  output_nml.write('  count_veh_id(51) + //railfast1\n')
  output_nml.write('  count_veh_id(53) +\n')
  output_nml.write('  count_veh_id(55) //railfast3\n')
  output_nml.write('  ){\n')
  for i in range(0,64):
    start = i*4+1
    end = i*4+4
    if i == 0:
      start = 0
    output_nml.write('  ' + str(start) + '..' + str(end) + ': switch_rail_freight_short_graphics_both_draw' + str(i+1) + ';\n')
  output_nml.write('  switch_rail_freight_short_graphics_both_draw64;\n')
  output_nml.write('}\n')






  # -----------------------------------------------------------------------------------------------------------------------------------------------
  # front drawing ---------------------------------------------------------------------------------------------------------------------------------

  # count switches
  for i in range(1, 65):
    output_nml.write('switch(FEAT_TRAINS, SELF, switch_rail_freight_short_graphics_front_draw' + str(i) + ', position_in_consist){\n')
    for n in range(0, i*2):
      default_spritesheet = '  switch_rail_freight_short_vehid_wagons_self;\n'
      if (n%2)==0:
        spritesheet = 'sprite_INVISIBLE;\n'
      else:
        spritesheet = 'switch_rail_freight_short_vehid_front;\n'
      output_nml.write('  ' + str(n) + ': ' + spritesheet)
    output_nml.write(default_spritesheet)
    output_nml.write('}\n')
  
  # switch for front drawing
  output_nml.write('switch(FEAT_TRAINS, PARENT, switch_rail_freight_short_graphics_front,\n')
  output_nml.write('  count_veh_id(7) + // rail EARLY 01\n')
  output_nml.write('  count_veh_id(8) +\n')
  output_nml.write('  count_veh_id(9) + // rail EARLY 03\n')
  output_nml.write('  count_veh_id(11) + // railstrong1\n')
  output_nml.write('  count_veh_id(13) +\n')
  output_nml.write('  count_veh_id(15) + //railstrong3\n')
  output_nml.write('  count_veh_id(31) + //railmedium1\n')
  output_nml.write('  count_veh_id(33) +\n')
  output_nml.write('  count_veh_id(35) + //raiilmedium3\n')
  output_nml.write('  count_veh_id(51) + //railfast1\n')
  output_nml.write('  count_veh_id(53) +\n')
  output_nml.write('  count_veh_id(55) //railfast3\n')
  output_nml.write('  ){\n')
  for i in range(0,64):
    start = i*4+1
    end = i*4+4
    if i == 0:
      start = 0
    output_nml.write('  ' + str(start) + '..' + str(end) + ': switch_rail_freight_short_graphics_front_draw' + str(i+1) + ';\n')
  output_nml.write('  switch_rail_freight_short_graphics_front_draw64;\n')
  output_nml.write('}\n')
  