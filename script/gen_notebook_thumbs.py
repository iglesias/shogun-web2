import os
import sys

def main():
  NOTEBOOK_DIR = os.path.dirname(os.path.realpath(__file__)) + "/../static/notebooks"

  if len(sys.argv) < 2:
    print "enter the notebook name"

  notebook_name = sys.argv[1]
  notebook = NOTEBOOK_DIR + "/" + notebook_name

  image = get_notebook_image(notebook)
  f = open(notebook[:-5]+".png", "wb")
  f.write(image.decode('base64'))
  f.close()

  # all notebooks - possibly dangerous if some have manual thumbs
  #NOTEBOOK_DIR = os.path.dirname(os.path.realpath(__file__)) + "/../static/notebooks"
  #notebooks=[ '%s/%s' % (NOTEBOOK_DIR, f) for f in os.listdir(NOTEBOOK_DIR) if f.endswith('.html') ]
  #for notebook in notebooks:
  #  image = get_notebook_image(notebook)
  #  f = open(notebook[:-5]+".png", "wb")
  #  f.write(image.decode('base64'))
  #  f.close()

def get_notebook_image(notebook):
  image=None
  for line in open(notebook).readlines():
    if image is not None:
      if line.startswith('">'):
        return ''.join(image)
      else:
        image.append(line[:-1])
    else:
      if line.startswith('<img'):
        image=[]
        image.append(line[line.find(','):-1])

if __name__ == '__main__':
  main()
