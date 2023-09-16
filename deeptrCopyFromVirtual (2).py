from Translation.GoogleTrans import TransLate, LangDetect, CodeLang, LanguageList
def main():
    translated_text = TransLate("Hello, world!", src="en", dest="fr")
    print("Функція - Translate")
    print(translated_text)

    print("\nФункція - LangDetect")
    text = "Привіт"
    lang = LangDetect(text, set="lang")
    confidence = LangDetect(text, set="confidence")
    both = LangDetect(text)
    print("Мова:", lang)
    print("Точність:", confidence)
    print(both)

    print("\nФункція - CodeLang")
    language_name = "English"
    language_code = "fr"

    code_from_name = CodeLang(language_name)
    name_from_code = CodeLang(language_code)

    print(f"Код мови за назвою '{language_name}': {code_from_name}")
    print(f"Назва мови за кодом '{language_code}': {name_from_code}")

    print("\nФункція - LanguageList")
    LanguageList("screen", "Добрий день")
if __name__ == "__main__":
    main()