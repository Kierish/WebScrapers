import requests
from bs4 import BeautifulSoup
import json
import re
import os

main_url = "https://www.kunst-archive.net/en/wvz/samuel_bak/works?v=grid&start=0&q=&group=type&filter=all&hpp=100&medium=&categories="
script_dir = os.path.dirname(__file__)

response = requests.get(main_url)
soup = BeautifulSoup(response.text, 'html.parser')

data = []
hrefs = []

div_tag = soup.find('div', class_='abschnitt')

if div_tag:  
    for li_tag in div_tag.find_all('li'):
        a_tag = li_tag.find('a', href=True)
        if a_tag:
            hrefs.append(a_tag['href'])

for link in hrefs:
    response = requests.get(f"https://www.kunst-archive.net{link}")
    soup = BeautifulSoup(response.text, 'html.parser')
    
    painting = soup.find('div', class_='cut')
    if painting:
        painting_info = {}

        painting_info['name_of_artist'] = "Samuel Bak"

        title = painting.find('h2')
        if title:
            painting_info['title'] = title.text.strip()

    artwork_details = soup.find('ul', class_='right_col')
    if artwork_details:

        date = artwork_details.find_all('li')[0]
        if date:
            date_text = date.text.strip()
            match_range_with_provenance = re.match(r'(\d{4})-(\d{4}),\s*in\s*(.*)', date_text)
            if match_range_with_provenance:
                painting_info['date'] = f"{match_range_with_provenance.group(1)}-{match_range_with_provenance.group(2)}"
                painting_info['provenance'] = match_range_with_provenance.group(3).strip()
            else:
                match_single_with_provenance = re.match(r'(\d{4}),\s*in\s*(.*)', date_text)
                if match_single_with_provenance:
                    painting_info['date'] = match_single_with_provenance.group(1)
                    painting_info['provenance'] = match_single_with_provenance.group(2).strip()
                else:
                    match_range = re.match(r'(\d{4})-(\d{4})', date_text)
                    if match_range:
                        painting_info['date'] = date_text
                        painting_info['provenance'] = None
                    else:
                        match_single = re.match(r'(\d{4})', date_text)
                        if match_single:
                            painting_info['date'] = date_text
                            painting_info['provenance'] = None
                        else:
                            painting_info['date'] = None
                            painting_info['provenance'] = None
        else:
            painting_info['date'] = None
            painting_info['provenance'] = None

        technique = artwork_details.find_all('li')[1]  
        painting_info['technique'] = technique.text.strip() if technique else None

        dimensions_cm = artwork_details.find_all('li')[2].find('span', class_='size2')
        if dimensions_cm:
            dimensions_text = dimensions_cm.text.strip()
            dimensions_text = dimensions_text.replace('(', '').replace(')', '').strip()
            painting_info['dimensions'] = dimensions_text
        else:
            dimensions_inch = artwork_details.find_all('li')[2].find('span')
            if dimensions_inch:
                inch_text_parts = [] 
            
                for child in dimensions_inch.children: 
                    if child.name == 'sup' or child.name == 'sub': 
                       inch_text_parts.append(child.text)
                    elif child.name is None: 
                        inch_text_parts.append(str(child).strip())

                painting_info['dimensions'] = " ".join(inch_text_parts).strip()         
            else:
                painting_info['dimensions'] = None 

        signature = artwork_details.find_all('li')[3]
        if signature:

            br_element = signature.find('br')
            if br_element:
                br_element.extract()
            
            signature_text = signature.text.strip()
            if "Signed" in signature_text or "signed" in signature_text:
                painting_info['signature'] = signature_text
            else:
                painting_info['signature'] = None 
        else:
            painting_info['signature'] = None 
    
    exhibitions_section = soup.find('div', attrs={"data-hint": "9"})
    if exhibitions_section:
        exhibitions = []
        paragraphs = exhibitions_section.find_all('p')
        for p in paragraphs:
            a_tag = p.find('a', class_='werk')
            if a_tag:
                title_span = a_tag.find('span', class_='title')
                details_span = a_tag.find('span', class_='details')

                title = title_span.text.strip() 
                details = details_span.text.strip() 

                exhibition_info = f"{details}, {title}"
                exhibitions.append(exhibition_info)
        painting_info['exhibitions'] = exhibitions
    else:
        painting_info['exhibitions'] = None

    bibliography_section = soup.find('div', attrs={"data-hint": "10"})
    if bibliography_section:
        bibliographies = []
        paragraphs = bibliography_section.find_all('p')
        for p in paragraphs:
            a_tag = p.find('a', class_='werk')
            if a_tag:
                title_span = a_tag.find('span', class_='title')
                details_spans = a_tag.find_all('span', class_='details')
                
                title = title_span.text.strip()
                details_texts = [span.text.strip() for span in details_spans]
                details = ", ".join(details_texts) 

                bibliography_info = f"{title}, {details}"
                bibliographies.append(bibliography_info)
        
        painting_info['bibliography'] = bibliographies
    else:
        painting_info['bibliography'] = None
    
    images_dir = os.path.join(script_dir, "images")
    os.makedirs(images_dir, exist_ok=True)
    image_section = soup.find('section', class_='werk_details')
    if image_section:
        image_tag = image_section.find('img', id='bigImage')
        if image_tag:
            image_url = image_tag.get('src')
            image_url = f"https://www.kunst-archive.net{image_url}"
            painting_info['image_url'] = image_url

            image_response = requests.get(image_url, stream=True)
            image_response.raise_for_status()  
            image_name = f"{painting_info['title'].replace(' ', '_').replace('/', '_')}.jpg"
            image_path = os.path.join(images_dir, image_name)
            with open(image_path, 'wb') as img_file:
                for chunk in image_response.iter_content(chunk_size=8192):
                    img_file.write(chunk)
                
        else:
            painting_info['image_url'] = None
    else:
        painting_info['image_url'] = None
    data.append(painting_info)

json_file_path = os.path.join(script_dir, "Samuel.json")
with open(json_file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
        

