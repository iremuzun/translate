from googletrans import Translator


translator = Translator()


result = translator.translate('aceleración de una partícula')

'''src: The source language
dest: Destination language
origin: Original text, that
text: Translated text, that will be 
pronunciation: Pronunciation of the translated text'''


print(result.src)
print(result.dest)
print(result.origin)
print(result.text)
print(result.pronunciation)

result = translator.translate('aceleración de una partícula', src='es', dest='tr')
 

print(result.src)
print(result.dest)
print(result.text)

sentences = ['movimiento circular uniforme', 'aceleración centrípeta', 'velocidad angular']

result = translator.translate(sentences, src='es' , dest = 'tr')

for trans in result:
    print(f'{trans.origin} -> {trans.text}')
