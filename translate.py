import xml.etree.ElementTree as ET
import deepl

def translate_xml(xml_file, target_language, deepl_api_key):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Initialize the DeepL translator
    translator = deepl.Translator(deepl_api_key)

    # Iterate through all elements in the XML tree
    for elem in root.iter():
        # If the element has text, translate it
        if elem.text and elem.text.strip():
            translation = translator.translate_text(elem.text, target_lang=target_language)
            elem.text = translation.text

    # Save the translated XML to a new file
    with open('output.xml', 'wb') as f:
        f.write(ET.tostring(root, encoding='utf-8'))

# Replace 'your-deepl-api-key' with your actual DeepL API key
# Replace 'input.xml' with the path to your XML file
# Replace 'ru' with the target language code for Russian
translate_xml('input.xml', 'ru', 'your-deepl-api-key')
