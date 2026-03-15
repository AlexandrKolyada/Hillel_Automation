import  os
import xml
import logging
import xml.etree.ElementTree as ET
from re import findall
from xml.etree.ElementTree import ElementTree

logging.basicConfig(filename='json__kolyada.log',level=logging.INFO, format='%(levelname)s - %(message)s')

def func_find(file_path, search_number):
    tree = ET.parse(file_path)
    root = tree.getroot()

    for element in root.findall('group'):
        current_num = element.find('number').text
        if current_num == str(search_number):
            result = element.find('timingExbytes/incoming').text
            logging.info(f" Found value {result}")
            return result