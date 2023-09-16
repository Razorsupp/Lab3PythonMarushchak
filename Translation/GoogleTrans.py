
from googletrans import Translator, LANGUAGES

def TransLate(text: str, src: str, dest: str) -> str:
    translator = Translator()
    try:
        translated_text = translator.translate(text, src=src, dest=dest).text
        return translated_text
    except Exception as e:
        return str(e)

def LangDetect(text: str, set: str = "all") -> str:
    translator = Translator()
    try:
        detected = translator.detect(text)
        if set == "lang":
            return detected.lang
        elif set == "confidence":
            return str(detected.confidence)
        else:
            return f"Мова: {detected.lang}, Точність: {detected.confidence}"
    except Exception as e:
        return str(e)

def CodeLang(lang: str) -> str:
    LANGUAGES = {
        "en": "English",
        "fr": "French",
        "es": "Spanish"
    }

    if lang in LANGUAGES:
        return LANGUAGES[lang]
    else:
        for code, name in LANGUAGES.items():
            if name == lang:
                return code
        return "Мова не знайдена"

def LanguageList(out: str = "screen", text: str = None) -> str:
    try:
        if out == "screen":
            print("N\tМова\tISO-639 код\tТекст")
            print("-" * 48)
            for i, (code, lang) in enumerate(LANGUAGES.items(), start=1):
                if text:
                    translation = TransLate(text, 'auto', code)
                    print(f"{i}\t{lang}\t{code}\t{translation}")
                else:
                    print(f"{i}\t{lang}\t{code}\t")
            return "Ok"
        elif out == "file":
            filename = "langGoogle.txt"
            with open(filename, "w", encoding="utf-8") as file:
                file.write("N\tLanguage\tISO-639 code\tText\n")
                file.write("-" * 48 + "\n")
                for i, (code, lang) in enumerate(LANGUAGES.items(), start=1):
                    if text:
                        translation = TransLate(text, 'auto', code)
                        file.write(f"{i}\t{lang}\t{code}\t{translation}\n")
                    else:
                        file.write(f"{i}\t{lang}\t{code}\t\n")
            return f"Таблиця збережена в: {filename}"
        else:
            return "Помилка 'out' параметру"
    except Exception as e:
        return str(e)