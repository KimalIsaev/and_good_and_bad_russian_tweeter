
# Table of Contents

1.  [Программа для определения хороший или плохой твит](#org0856443)
    1.  [0 - плохой](#org09995bb)
    2.  [1 - хороший](#org82c1b71)
    3.  [Как пользоваться](#orge25b157)
    4.  [Плечи гигантов](#org353261f)
        1.  [Проект rusvectores (borrowed<sub>model</sub>/rusvectores<sub>180.zip</sub>)](#orgb285c78)
        2.  [Проект Юлии Рубцовой (initial<sub>dataset</sub>)](#org4176145)
        3.  [Проект Emoji2Vec (borrowed<sub>model</sub>/emoji2vec.bin)](#org87aa4b3)
        4.  [Книга Natural Language Processing in Action](#org199d25d)


<a id="org0856443"></a>

# Программа для определения хороший или плохой твит


<a id="org09995bb"></a>

## 0 - плохой


<a id="org82c1b71"></a>

## 1 - хороший


<a id="orge25b157"></a>

## Как пользоваться

1. Запустить в командной строке result.py
2. Немного подождать
3. Писать русскими буквами в командную строку, программа будет отвечать числом от 0 до 1.(останавливается Ctr-C)Программа поддерживает и смайлики с помощью пунктуации/символов и эмоджи.

Точность сотставляет 97,5%, но мне не стоит обольщаться так как почти в кажом твите содержится "(" или ")", и нейронка придаёт самое большее значение им.
Точность без смайликов 69,83% (скоро выложу эту модель) 

<a id="org353261f"></a>

## Плечи гигантов


<a id="orgb285c78"></a>

### Проект [rusvectores](https://rusvectores.org/ru/) (borrowed_model/rusvectores_180.zip)

И соответствующий [скрипт](https://github.com/akutuzov/webvectors/blob/master/preprocessing/rus_preprocessing_udpipe.py) (rusvectores_script/rus_preprocessing_udpipe.py) Татьяны Шавриной


<a id="org4176145"></a>

### Проект [Юлии Рубцовой](https://study.mokoron.com/) (initial_dataset)

по собиранию и классифицированию русских твитов 
<https://elibrary.ru/item.asp?id=20399632>


<a id="org87aa4b3"></a>

### Проект[ Emoji2Vec](https://github.com/uclmr/emoji2vec) (borrowed_model/emoji2vec.bin)


<a id="org199d25d"></a>

### Книга [Natural Language Processing in Action](https://github.com/totalgood/nlpia)

