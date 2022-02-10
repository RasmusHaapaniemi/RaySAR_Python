'''
Created on 13 Dec 2021

@author: rasmus
'''




import sys
import json
import pprint
from application import Application


def main(argv):
        
    app = Application()
    
    if len(argv) != 2:
        print("\nArgiments are not correct!!!\nExiting program...\n\n")
  
    with open('para.json') as json_file:
        data = json.load(json_file)
        
    for settings in data:
        if settings['fileName'] ==  argv[1]:
            print("\nParameters from:\n" + settings['fileName'] + " selected\n")
            pprint.pprint(settings)
            
            app.set_azimuth_min(settings['azimuthMin'])
            app.set_azimuth_max(settings['azimuthMax'])
            app.set_azimuth_spacing(settings['azimuthSpacing'])
            app.set_range_min(settings['rangeMin'])
            app.set_range_max(settings['rangeMax'])
            app.set_range_spacing(settings['rangeSpacing'])
            app.set_dB_min(settings['dBmin'])
            app.set_dB_max(settings['dBmax'])
            app.set_dB_rng(settings['dBrng'])
            app.set_noise_level(settings['noise'])
            app.set_trace_level(settings['traceLevel'])
            app.set_system_response_th(settings['responseTh'])
            app.set_system_response_decay(settings['responseDecey'])
            app.set_visual_data(settings['visualData'])
            app.set_sar_image_rescale(settings['imageRescale'])
            app.set_folder_path(settings['path'])
            app.run()
         
    print("\n\nAll selected data is processed\nExiting program...")
    
    
    
if __name__ == '__main__':
    main(sys.argv)
    
    
    
    
    
    