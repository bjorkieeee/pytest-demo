import pytest
import os

def change_title_by_language(language: str):
    f = open("my_website.txt", 'w')
    if language == "en":
        f.write("Hello World")
    elif language == "fr":
        f.write("Bonjour le monde") 
    elif language == "es":
        f.write("Hola Mundo") 
    f.close()

    
@pytest.fixture(params=["en", "fr", "es"])
def title_by_language(request):
    # Set up the language based on the parameter value
    lang = request.param
    change_title_by_language(lang)
    yield lang
    os.remove("my_website.txt")

