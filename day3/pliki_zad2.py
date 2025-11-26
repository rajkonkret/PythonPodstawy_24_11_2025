import chardet

#  pip install chardet - instalacja biliotek

# musimy wczytac binarnie - wymaganie chardet
with open('test.log', "rb") as fh:
    raw_data = fh.read()

print(raw_data)
# b'Parametr1\r\nParametr2\r\nParametr3\r\nParametr4\r\nDodane\r\nDodane2\r\nDodane3\r\nD\xc5\x9bodane4\r\n'

result = chardet.detect(raw_data)
print(result)
# {'encoding': 'Windows-1252', 'confidence': 0.73, 'language': ''}
# po dodaniu większej ilości ilości polskich liter:
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
encoding = result['encoding']
confidence = result['confidence']

print("Kodowanie znaków:", encoding)
print(f"Trafność: {confidence * 100} %")
# Kodowanie znaków: utf-8
# Trafność: 99.0 %
print(raw_data.decode(encoding=encoding))
# Parametr1
# Parametr2
# Parametr3
# Parametr4
# Dodane
# Dodane2
# Dodane3
# Dśążźćodane4
