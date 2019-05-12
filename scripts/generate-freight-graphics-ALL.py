import sys
import math
import os

def generate_above_switches(args):
  print('wtf')

def generate_draw_switches_short_alternating(args):
  veh_name = args[0]
  veh_id   = args[1]
  outcome_front   = args[2]
  outcome_back    = args[3]
  outcome_wagon   = args[4]
  outcome_overlay_active = 'sprite_attach_4_active'
  outcome_overlay_inactive = 'sprite_attach_4_inactive'
  outcome_invisible = 'sprite_INVISIBLE'

  outcome_switch_front   = outcome_front #veh_name + '_switch_outcome_switch_front'
  outcome_switch_back    = outcome_back #veh_name + '_switch_outcome_switch_end'
  outcome_switch_wagon   = veh_name + '_switch_outcome_switch_wagon'
  outcome_switch_overlay = veh_name + '_switch_outcome_switch_overlay'

  script_path = os.path.realpath(__file__)
  script_folder = os.path.dirname(script_path)
  output_folder = os.path.join(script_folder, '..', 'src-generated')
  output_filename = veh_name + '_graphics.nml'
  output_filepath = os.path.join(output_folder, output_filename)
  output_folder_path = os.path.normpath(output_folder)
  #print('SYS PATH', sys.path) check python version
  if os.path.isdir(output_folder_path) == False:
    os.makedirs(output_folder_path)

  with open(output_filepath, 'w') as output_nml:
    # switch for active/inactive overlay
    output_nml.write('//' + '-'*128 + '\n')
    output_nml.write('// active/inactive overlay')
    output_nml.write('\nswitch (FEAT_TRAINS,SELF, ' + outcome_switch_overlay + ', position_in_articulated_veh){')
    output_nml.write('\n  0: ' + outcome_overlay_active + ';')
    output_nml.write('\n  ' + outcome_overlay_inactive + ';')
    output_nml.write('\n}')
    output_nml.write('\n')
    
    # drawing results & layers
    # back outcome switch
    output_nml.write('//' + '-'*128 + '\n')
    output_nml.write('// wagon drawing')
    output_nml.write('\nswitch (FEAT_TRAINS,SELF, ' + outcome_switch_wagon + '_layers' + ', [')
    output_nml.write('\n  STORE_TEMP((getbits(extra_callback_info1, 8, 8) < 4 ? CB_FLAG_MORE_SPRITES  : 0) + PALETTE_USE_DEFAULT, 0x100),')
    output_nml.write('\n  getbits(extra_callback_info1, 8, 8)')
    output_nml.write('\n  ]){')
    output_nml.write('\n  0: ' + outcome_wagon + ';')
    output_nml.write('\n  1: ' + outcome_switch_overlay + ';')
    output_nml.write('\n}')
    output_nml.write('\nswitch(FEAT_TRAINS, PARENT, ' + outcome_switch_wagon + ', vehicle_is_stopped + vehicle_is_in_depot){')
    output_nml.write('\n  2: ' + outcome_switch_wagon + '_layers' + ';')
    output_nml.write('\n  '+ outcome_wagon + ';')
    output_nml.write('\n}')
  


    # separator
    output_nml.write('\n')
    output_nml.write('//' + '-'*128 + '\n')
    output_nml.write('//' + '-'*128 + '\n')
    output_nml.write('//' + '-'*128 + '\n')
    output_nml.write('//' + '-'*128 + '\n')
    output_nml.write('//' + '-'*128 + '\n')
    output_nml.write('//' + '-'*128 + '\n')
    output_nml.write('//' + '-'*128 + '\n')
    output_nml.write('//' + '-'*128 + '\n')
    output_nml.write('//' + '-'*128 + '\n')



    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # the many drawing switches ---------------------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    for i in range(1, 65):

      # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      # dual headed drawing ---------------------------------------------------------------------------------------------------------------------------
      # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      # write _end version
      # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      if i>1:
        # write switch header
        output_nml.write('switch(FEAT_TRAINS, SELF, ' + veh_name + '_draw' + str(i) + '_both' + '_end, position_in_consist_from_end){\n')
        # do stuff with i
        i_half = float(i)/2
        i_test = math.floor(i_half)#floor for _end
        i_range = int(i_test-1)
        # define i_text, change it if i == 0
        i_text = '..' + str(i_range)
        if i_range == 0:
          i_text = ''
        
        # define which spritesheet is to be used
        spritesheet = outcome_switch_back + ';\n'
        default_spritesheet = '  ' + outcome_switch_wagon + ';\n'
        
        for n in range(0, int(i_test*2)):
          if (n%4)==0:
            spritesheet = outcome_invisible + ';\n'
          elif (n%4)==1:
            spritesheet = outcome_switch_back + ';\n'
          elif (n%4)==2:
            spritesheet = outcome_switch_front + ';\n'
          elif (n%4)==3:
            spritesheet = outcome_invisible + ';\n'
          output_nml.write('  ' + str(n) + ': ' + spritesheet)
        output_nml.write(default_spritesheet)
        output_nml.write('}\n')
        
      # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      # write no _end version
      # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      # write switch header
      output_nml.write('switch(FEAT_TRAINS, SELF, ' + veh_name + '_draw' + str(i) + '_both' + ', position_in_consist){\n')
      # do stuff with i
      i_half = float(i)/2
      i_test = math.ceil(i_half)#floor for _end
      i_range = int(i_test-1)
      # define i_text, change it if i == 0
      i_text = '..' + str(i_range)
      if i_range == 0:
        i_text = ''
      
      spritesheet = outcome_switch_front + ';\n'
      default_spritesheet = '  ' + veh_name + '_draw' + str(i) + '_both' + '_end;\n'
      if i == 1:
        default_spritesheet = '  ' + outcome_switch_wagon +';\n'

      for n in range(0, int(i_test*2)):
        if (n%4)==0:
          spritesheet = outcome_invisible + ';\n'
        elif (n%4)==1:
          spritesheet = outcome_switch_front + ';\n'
        elif (n%4)==2:
          spritesheet = outcome_switch_back + ';\n'
        elif (n%4)==3:
          spritesheet = outcome_invisible + ';\n'
        output_nml.write('  ' + str(n) + ': ' + spritesheet)

      output_nml.write(default_spritesheet)
      output_nml.write('}\n')

      # -----------------------------------------------------------------------------------------------------------------------------------------------
      # front drawing ---------------------------------------------------------------------------------------------------------------------------------
      output_nml.write('switch(FEAT_TRAINS, SELF, ' + veh_name + '_draw' + str(i) + '_front' + ', position_in_consist){\n')
      for n in range(0, i*2):
        default_spritesheet = '  ' + outcome_switch_wagon + ';\n'
        if (n%4)==0:
          spritesheet = outcome_invisible + ';\n'
        elif (n%4)==1:
          spritesheet = outcome_switch_front + ';\n'
        elif (n%4)==2:
          spritesheet = outcome_switch_back + ';\n'
        elif (n%4)==3:
          spritesheet = outcome_invisible + ';\n'
        output_nml.write('  ' + str(n) + ': ' + spritesheet)
      output_nml.write(default_spritesheet)
      output_nml.write('}\n')

      # -----------------------------------------------------------------------------------------------------------------------------------------------
      # draw method switch
      output_nml.write('switch(FEAT_TRAINS, PARENT, ' + veh_name + '_draw' + str(i) + ', [')
      output_nml.write('\n  STORE_TEMP(position_in_consist_from_end, 0x10F), var[0x61, 0, 0xFFFF, 0xC6]')
      output_nml.write('\n  ]){')
      output_nml.write('\n  ' + str(veh_id) + ': ' + 'switch_mglv_freight_short_graphics_both_draw' + str(i) + ';')
      output_nml.write('\n  ' + 'switch_mglv_freight_short_graphics_front_draw' + str(i) + ';')
      output_nml.write('\n  }\n')
      
      # separator
      output_nml.write('//' + '-'*128 + '\n')
      output_nml.write('//' + '-'*128 + '\n')
      output_nml.write('//' + '-'*128 + '\n')

    # count_veh_id decider
    output_nml.write('switch(FEAT_TRAINS, PARENT, ' + veh_name + '_graphics' + ',')
    output_nml.write('\n  count_veh_id(' + str(veh_id) + ') ' + '){')
    for i in range(0,64):
      start = i*4+1
      end = i*4+4
      if i == 0:
        start = 0
      output_nml.write('\n  ' + str(start) + '..' + str(end) + ': ' + veh_name + '_draw'  + str(i+1) + ';')
    output_nml.write('\n  ' + veh_name + '_draw' + str(i+1) + ';')
    output_nml.write('\n}')
    


    





freight_short_normal_list = [
  # veh_name      veh_id     output      output_end       wagon output
  ('rail_early1', 7),
  ('rail_early2', 8),
  ('rail_early3', 9),

  ('rail_strong1', 11),
  ('rail_strong2', 13),
  ('rail_strong3', 15),
  
  ('rail_medium1', 31),
  ('rail_medium2', 33),
  ('rail_medium3', 35),
  
  ('rail_fast1', 51),
  ('rail_fast2', 53),
  ('rail_fast3', 55)
]
freight_short_alternating_list = [
  # veh_name      veh_id
  ('mglv_medium1', 211, 'spriteset_train_magstrong1', 'spriteset_train_magstrong1_end', 'maglevuniversal_switch'),
  ('mglv_medium2', 213, 'spriteset_train_magstrong2', 'spriteset_train_magstrong2_end', 'maglevuniversal_switch'),
  ('mglv_medium3', 215, 'spriteset_train_magstrong3', 'spriteset_train_magstrong3_end', 'maglevuniversal_switch'),
  ('mglv_medium4', 217, 'spriteset_train_magstrong4', 'spriteset_train_magstrong4_end', 'maglevuniversal_switch'),

  ('mglv_fast1', 251, 'spriteset_train_magfast1', 'spriteset_train_magfast1_end', 'maglevuniversal_switch'),
  ('mglv_fast2', 253, 'spriteset_train_magfast2', 'spriteset_train_magfast2_end', 'maglevuniversal_switch'),
  ('mglv_fast3', 255, 'spriteset_train_magfast3', 'spriteset_train_magfast3_end', 'maglevuniversal_switch'),
  ('mglv_fast4', 257, 'spriteset_train_magfast4', 'spriteset_train_magfast4_end', 'maglevuniversal_switch')
]
freight_long_normal_list = [
  'rail_strong4',
  'rail_strong5',
  'rail_strong6',
  'rail_strong7',
  'rail_strong8',
  'rail_strong9',

  'rail_medium4',
  'rail_medium5',
  'rail_medium6',
  'rail_medium7',
  'rail_medium8',
  'rail_medium9',

  'rail_fast4',
  'rail_fast5',
  'rail_fast6',
  'rail_fast7',
  'rail_fast8',
  'rail_fast9',
]
freight_long_alternating_list = [
  'mono_wtf1',
  'mono_wtf2',
  'mono_wtf3',
  'mono_wtf4',
  
  'mono_medium1',
  'mono_medium2',
  'mono_medium3',
  'mono_medium4',
  
  'mono_fast1',
  'mono_fast2',
  'mono_fast3',
  'mono_fast4',
]

y = 0
generate_draw_switches_short_alternating(
    [
      freight_short_alternating_list[y][0],
      freight_short_alternating_list[y][1],
      freight_short_alternating_list[y][2],
      freight_short_alternating_list[y][3],
      freight_short_alternating_list[y][4]
    ]
  )