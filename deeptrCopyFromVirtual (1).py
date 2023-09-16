from Translation.DeepTranslation import TransLate, LangDetect, CodeLang,LanguageList

def main():
    print("\nФункція - TransLate")
    translated_text = TransLate("Hello, world!", src="en", dest="fr")
    print(translated_text)

    print("\nФункція - LangDetect")
    text = "Привіт ДІП"
    lang = LangDetect(text, set="lang")
    confidence = LangDetect(text, set="confidence")
    both = LangDetect(text)

    print("Мова:", lang)
    print("Точність:", confidence)
    print(both)

    print("\nФункція - CodeLang")
    language_name = "Afrikaans"
    language_code = "bg"

    translated_name = CodeLang(language_name)
    translated_code = CodeLang(language_code)

    print(f"Переклад назви мови '{language_name}': {translated_name}")
    print(f"Переклад коду мови '{language_code}': {translated_code}")

    LanguageList("screen", "Привіт ДІП")
if __name__ == "__main__":
    main()
