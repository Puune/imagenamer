import sys, glob, os, re

#for arg in sys.argv:                             #help
# print (arg)      

matcher = sys.argv[1]
images = glob.glob(matcher)
old_name = (images[0].split("\\")[::-1])[0]     #extract filename from pathname
new_name = ""
regex = "[0-9]"
for char in old_name:
  if re.match(regex, char):
    break
  else:
    new_name = new_name + char

try:
  for number, image in enumerate(images, 1):
    concat_name = ((new_name + "{0}").format(number)) + ".JPG"  # name img with enumerator
    with_path = (image.split("\\")[::-1])                       
    with_path[0] = concat_name
    with_path = "\\".join((with_path[::-1]))                    # re-create full pahtname                    
    print(concat_name, with_path, image)                        
    os.rename(image, with_path)
except Exception as e:
  print("failure", e.__class__, e.with_traceback)
