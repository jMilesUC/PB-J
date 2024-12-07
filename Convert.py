import os
import xml.etree.ElementTree as ET

def convert_xml_to_yolo(xml_folder, output_folder, class_names):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for xml_file in os.listdir(xml_folder):
        if xml_file.endswith('.xml'):
            tree = ET.parse(os.path.join(xml_folder, xml_file))
            root = tree.getroot()

            # Open corresponding YOLO label file
            yolo_file = os.path.splitext(xml_file)[0] + '.txt'
            with open(os.path.join(output_folder, yolo_file), 'w') as f:
                for obj in root.iter('object'):
                    class_name = obj.find('name').text
                    if class_name in class_names:
                        class_id = class_names.index(class_name)
                        bbox = obj.find('bndbox')
                        x_min = float(bbox.find('xmin').text)
                        y_min = float(bbox.find('ymin').text)
                        x_max = float(bbox.find('xmax').text)
                        y_max = float(bbox.find('ymax').text)

                        # Convert to YOLO format
                        x_center = (x_min + x_max) / 2
                        y_center = (y_min + y_max) / 2
                        width = x_max - x_min
                        height = y_max - y_min

                        # Normalize values by image width and height
                        img_width = float(root.find('size/width').text)
                        img_height = float(root.find('size/height').text)

                        x_center /= img_width
                        y_center /= img_height
                        width /= img_width
                        height /= img_height

                        # Write to YOLO format file
                        f.write(f"{class_id} {x_center} {y_center} {width} {height}\n")

# Define paths
xml_folder = r"C:\Users\Parker Manson\Desktop\Senior Desgin\Yolo_data\Labels\Val"  # Path to XML files
output_folder = r"C:\Users\Parker Manson\Desktop\Senior Desgin\Yolo_data\Labels\Val"  # Output folder for YOLO files
class_names = ['dumbbell_bench', 'person', 'Treadmill']  # Update class names as needed

convert_xml_to_yolo(xml_folder, output_folder, class_names)
