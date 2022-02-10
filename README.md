# RaySAR_Python

=========== USED LIBRARIES =============

os

sys

json

pprint

numpy

imageio

matplotlib

cv2


============ TERMINAL USAGE =============

Terminal usage with current folder structure:

Set current direcotry to main git folder.

Add parameters to para.json file in the folder,

that is automaticly opened when runned.

Run main.py with python3

Tell name of wanted parametrs

"py main.py T62-17"

"py main.py CAR"

"py main.py PLANE"





============ PARA FILE INFO ==============

Filename is name of parameter set that is given as arg

az min is left limit of created image
az max is right limit of created image
az spacing affects how many horizontal pixels image has

ra min is up limit of created image
ra max is down limit of created image
ra spacing affects how many vertical pixels image has

dBmin sets lowest possible amplitude to whole image
dBmax sets highest possible amplitude to whole image
dBrng allows dB limits to fluctuate within set percent value

noise allows measured complex amplitude vectors randomly rotate with given angle limit

trace level is maximum bounce number for rays

response th is minimum percent value of amplitude from global maximum that gets this effect
respsonse decay changes how fastly effect gets smaller

visual data plots informative images
image rescale changes output images true pixel size
upside down flips image vertically

path is relative path within main git folder to wanted data folder.




=========== QUICK START ============

Models are usually in middle, but range can change from scene to scene.
Visual data plots data-coordinate images that can be used to locate object.

Pixel spacing changes resolution. Smaller is higher. Changin this may produce aliasing
that is depended on used resolution in the POV-Ray. 
Good values that don't produce aliasing are:
2 * az spacing = POV-Ray az spacing 
tan(90-incicent) * ra spacing = POV-Ray ra spacing 

dB limits affect the color scaling of the image. 
Visual data plots dB and 8-bit histogram, that can be used as help
to obtain good image.

Response function simulates limited frequency range of SAR system by greating star liked shapes.
It is replicated as steep exponential function and thus the larger pixel amplitude means larger effect.
Th limits the number of points that get the effect as percent value from global maximum amplitude.
Decay affects to decreasing phase of the function. Smaller is faster.

Path is reltive path to data folder inside of the main git folder.
Application iterates all .txt files (Conributions) in that folder 
and saves them to same location.

