

class TestWebsiteLanguage:
    
    title_mappings = {
        "en": "Hello World",
        "fr": "Bonjour le monde",
        "es": "Hola Mundo"
    }

    
    def test_title_language(self, title_by_language, request):
        print(request)
        f = open("my_website.txt", "r")
        current_title = f.read()
        expected_title = self.title_mappings[title_by_language]
        assert current_title == expected_title

    

