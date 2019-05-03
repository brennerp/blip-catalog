import sys
import re
import ntpath
import os

path='all/'
defs = open("defs.svg", "w")

defs.write('<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">\n')
defs.write('\t<defs>\n')

for root, dirs, files in os.walk(path):
  for svgFile in files:
    print(svgFile)
    if svgFile.endswith(".svg"):
      svgFilePath = os.path.join(root, svgFile)
      with open(svgFilePath) as svg:
        fullSvg = svg.read()

        fileName = ntpath.basename(svgFile).split('.svg')[0]

        pathStart = fullSvg.find('>') + 1
        pathEnd = fullSvg.find('</svg>')

        svgPath = fullSvg[pathStart : pathEnd]

        path = ''.join(['\t\t<symbol id="', fileName, '" viewBox="0 0 24 24">', svgPath, '</symbol>\n'])
        defs.write(path)

defs.write('\t</defs>\n')
defs.write('</svg>\n')

defs.close()
