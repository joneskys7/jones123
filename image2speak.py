#sudo apt-get install espeak 
#sudo apt-get install tesseract-ocr
#sudo rasp-config
#then advance settings on 3.5 output
#image.jpg in pi folder
#imagetext.txt will be auto created

import shlex, subprocess
cmd_line= "tesseract /home/pi/image.jpg /home/pi/imagetext"  
args = shlex.split(cmd_line)
p = subprocess.Popen(args)
tf = "/home/pi/imagetext.txt"
fo = open(tf)
jp =  fo.read()
print jp
text_line= "espeak -ven -s150 " + "' "  +  jp + "' "
pg = shlex.split(text_line)
print pg
lo = subprocess.Popen(pg)
