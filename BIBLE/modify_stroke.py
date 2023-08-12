import os
import shutil 
import xml.etree.ElementTree as ET

orig_folder = '528_SVGs/' 
new_folder = 'updated_svgs'
stroke_width = 0.25

# Create new folder if doesn't exist
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

# Process SVG files    
for filename in os.listdir(orig_folder):
    if filename.endswith('.svg'):

        # Parse original SVG file
        orig_path = os.path.join(orig_folder, filename)
        tree = ET.parse(orig_path)
        root = tree.getroot()

        # Modify SVG
        for path in root.findall('.//{http://www.w3.org/2000/svg}path'):
            if 'fill' in path.keys():
                del path.attrib['fill'] 
            if 'stroke-width' in path.keys():
                path.attrib['stroke-width'] = str(stroke_width)

        # Write updated SVG to new folder 
        new_path = os.path.join(new_folder, filename)
        tree.write(new_path)

# Copy original SVGs to new folder
for filename in os.listdir(orig_folder):
    orig_path = os.path.join(orig_folder, filename)
    shutil.copy(orig_path, new_folder)