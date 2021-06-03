from PIL import Image
Image.MAX_IMAGE_PIXELS = None
import argparse

def run():
    a_tuple = eval(options['a_values'])
    b_tuple = eval(options['b_values'])

    input_image = Image.open(options['input'])
    output_image = input_image.copy()
    for y in range(0, input_image.height):
        for x in range(0, input_image.width):
            pix = input_image.getpixel((x,y))
            if pix in a_tuple:
                result_tuple_index = a_tuple.index(pix)
                output_image.putpixel((x,y), b_tuple[result_tuple_index])

    input_image.close()
    output_image.save(options['output'])
    print('Saved', options['output'])
    output_image.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Process some arguments.')
    parser.add_argument('-a', '--a_values',
                        help = 'Indexes to replace from.',
                        type = str,
                        required = True)
    parser.add_argument('-b', '--b_values',
                        help = 'Indexes to replace to.',
                        type = str,
                        required = True)
    parser.add_argument('-i', '--input',
                        help = 'Input image path.',
                        type = str,
                        required = True)
    parser.add_argument('-o', '--output',
                        help = 'Output image path.',
                        type = str,
                        required = True)
    
    options = vars(parser.parse_args())
    default_values = [
        ('a_values' , ''),
        ('b_values' , ''),
        ('input'    , ''),
        ('output'   , '')
    ]
    for name, def_value in default_values:
        if not options[name]:
            options[name] = def_value

    run()