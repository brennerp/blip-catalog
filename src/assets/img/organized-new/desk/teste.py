import glob
import sys
import re
import ntpath

path='all/*.svg'
svgFiles = glob.glob(path)

defs = open("defs.svg", "w")

defs.write('<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">\n')
defs.write('\t<defs>\n')

for svgFile in svgFiles:
  with open(svgFile) as svg:
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
