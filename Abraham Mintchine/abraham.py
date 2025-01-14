import requests
from bs4 import BeautifulSoup
import json
import re
import os
import signal
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

should_exit = False

def signal_handler(signal, frame):
    global should_exit
    should_exit = True

signal.signal(signal.SIGINT, signal_handler)

script_dir = os.path.dirname(__file__)
json_file_path = os.path.join(script_dir, "Abraham.json")
images_dir = os.path.join(script_dir, "images")
os.makedirs(images_dir, exist_ok=True)

main_url = "https://mintchinesociety.org/?page_id=1388"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu") 
chrome_options.add_argument("--no-sandbox") 
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920x1080") 
service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(main_url)

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
driver.quit()
response = requests.get(main_url)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')

data = []
image_counter = 0

if os.path.exists(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as f:
        loaded_data = json.load(f)
        if isinstance(loaded_data, list):
            data = loaded_data
            if data:
                image_counter = len(data)
        elif isinstance(loaded_data, dict) and 'progress' in loaded_data:
            data = loaded_data.get('paintings', [])
            image_counter = loaded_data.get('progress', 0)

for i in range(image_counter + 2, 302):
    
    if should_exit:
           break
    
    painting_class = f"row-{i}"

    painting = soup.find('table', id='tablepress-98').find('tr', class_=f'{painting_class}')    
    if painting:
        painting_info = {}

        painting_info['name_of_artist'] = "Abraham Mintchine"

        title = painting.find('td', class_='column-2')
        painting_info['title'] = title.text.strip() if title else None

        dimension = painting.find('td', class_='column-3')
        painting_info['dimensions'] = f"{dimension.text.strip()} cm" if dimension else None

        technique = painting.find('td', class_='column-4')
        painting_info['technique'] = technique.text.strip() if technique else None

        signature = painting.find('td', class_='column-5')
        painting_info['signature'] = signature.text.strip() if signature.text.strip() != "" else None

        date_text = painting.find('td', class_='column-6').text.strip()
        if date_text != "":
            match = re.search(r'\b\d{4}\b', date_text)
            painting_info['date'] = match.group() if match else None
        else:
            painting_info['date'] = None
        
        exhibition_section = painting.find('td', class_='column-7')
        if exhibition_section:
            paragraphs = exhibition_section.find_all('p')
            exhibitions = [p.text.strip() for p in paragraphs]
            painting_info['exhibitions'] = exhibitions if exhibitions else None

        bibliography_section = painting.find('td', class_='column-8')
        if bibliography_section:
            paragraphs = bibliography_section.find_all('p')
            bibliographies = [p.text.strip() for p in paragraphs]
            painting_info['bibliography'] = bibliographies if bibliographies else None

        provenance_section = painting.find('td', class_='column-9')
        if provenance_section:
            paragraphs = provenance_section.find_all('p')
            provenances = [p.text.strip() for p in paragraphs]
            painting_info['provenance'] = provenances if provenances else None

        image_section = painting.find('td', class_='column-1')
        if image_section:
            image_tag = image_section.find('img')
            if image_tag:
                image_url = image_tag.get('src')
                painting_info['image_url'] = image_url

                image_counter += 1
                image_response = requests.get(image_url, stream=True)
                image_response.raise_for_status()
                image_name = f"{image_counter}.jpg"
                image_path = os.path.join(images_dir, image_name)
                with open(image_path, 'wb') as img_file:
                    for chunk in image_response.iter_content(chunk_size=8192):
                        img_file.write(chunk)
    data.append(painting_info)


    with open(json_file_path, 'w', encoding='utf-8') as f:
        json.dump({'progress': image_counter, 'paintings': data}, f, indent=4, ensure_ascii=False)
            