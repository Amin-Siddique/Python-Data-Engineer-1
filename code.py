import glob                         
import pandas as pd                 
import xml.etree.ElementTree as ET  
from datetime import datetime

#Download Source File:
!wget https://github.com/Amin-Siddique/Python-Data-Engineer-1/blob/main/source.zip

#Unzip Source File:
!unzip source.zip

#csv extraction function
def extract_from_csv(file_to_process):
  dataframe = pd.read_csv(file_to_process)  
  return dataframe

#json extraction function
def extract_from_json(file_to_process):
  dataframe = pd.read_json(file_to_process,lines=True)
  return dataframe

#xml extraction function
def extract_from_xml(file_to_process):
    dataframe = pd.DataFrame(columns=["name", "height", "weight"])
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for person in root:
        name = person.find("name").text
        height = float(person.find("height").text)
        weight = float(person.find("weight").text)
        dataframe = dataframe.append({"name":name, "height":height, "weight":weight}, ignore_index=True)
    return dataframe
  
  # EXTRACT FUNCTION:
  def extract():
    extracted_data = pd.DataFrame(columns=['name','height','weight'])   #Empty DF
    
    #process all csv files
    for csvfile in glob.glob("*.csv"):
        extracted_data = extracted_data.append(extract_from_csv(csvfile), ignore_index=True)
        
    #process all json files
    for jsonfile in glob.glob("*.json"):
        extracted_data = extracted_data.append(extract_from_json(jsonfile), ignore_index=True)
    
    #process all xml files
    for xmlfile in glob.glob("*.xml"):
        extracted_data = extracted_data.append(extract_from_xml(xmlfile), ignore_index=True)
        
    return extracted_data

  
  # Transformation:
  def transform(data):
        #Convert inches to meters and round off to two decimals(one inch is 0.0254 meters)
        data['height'] = round(data.height * 0.0254,2)

        #Convert pounds to kilograms and round off to two decimals(one pound is 0.45359237 kilograms)
        data['weight'] = round(data.weight * 0.45359237,2)
        return data
      
    # Load:
    
    def load(targetfile,data_to_load):
      data_to_load.to_csv(targetfile)  
    
    
    
    # Running as pipeline:
    targetfile = "transformed_data.csv" 
    
    extracted_data = extract()
    transformed_data = transform(extracted_data)
    load(targetfile,transformed_data)
    
