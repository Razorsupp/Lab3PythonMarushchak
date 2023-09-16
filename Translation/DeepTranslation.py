from deep_translator import GoogleTranslator as Translator
from langdetect import detect

LANGUAGES = {
    'af': 'Afrikaans',
    'sq': 'Albanian',
    'am': 'Amharic',
    'ar': 'Arabic',
    'hy': 'Armenian',
    'az': 'Azerbaijani',
    'eu': 'Basque',
    'be': 'Belarusian',
    'bn': 'Bengali',
    'bs': 'Bosnian',
    'bg': 'Bulgarian',
    'ca': 'Catalan',
    'ceb': 'Cebuano',
    'ny': 'Chichewa',
}

def TransLate(text: str, src: str, dest: str) -> str:
    try:
        translated_text = Translator(source=src, target=dest).translate(text)
        return translated_text
    except Exception as e:
        return str(e)

def LangDetect(text: str, set: str = "all") -> str:
    try:
        detected_lang = detect(text)
        if set == "lang":
            return detected_lang
        elif set == "confidence":
            return "Не підтримується в langdetect"
        else:
            return f"Мова: {detected_lang}, Точність: Не підтримується в langdetect"
    except Exception as e:
        return str(e)

def CodeLang(lang: str) -> str:
    if lang in LANGUAGES:
        return LANGUAGES[lang]  # Повертаємо назву мови, якщо передано код мови
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
            filename = "langDeep.txt"
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