# Прототип проекта

Мой продукт помогает увлечённым ценителям парфюмерии и коллекционерам решать проблему неэффективного поиска и "слепых" покупок, когда требуется найти новый парфюм по уже известным любимым нотам и стилям, либо же наоборот присмотреть что-нибудь абсолютно новое.
Для этого используется рекомендательная система на основе нейронных сетей, которая анализирует вкусовые предпочтения пользователя. Таким образом, пользователи будут получать качественные рекомендации, а ad-based бизнес-модель с кастомизированной рекламой поможет получить выгоду и в дальнейшем выйти непосредственно на рынок ритейла.

## ЦА

В первую очередь, целевой аудиторией являются парфюмерные энтузиасты, которые много времени проводят онлайн в тематических сообществах и хотят расширить свои коллекции.
Обычно у таких людей есть чёткие предпочтения ("обожаю вишню, ненавижу пачули, могу жить с розой"), но при этом их не интересуют ароматы, копирующие те, которые уже есть у них в коллекции; этот сегмент, скорее, будет искать что-нибудь в том же стиле.
Также для этой группы пользователей характерно желание исследовать новые ароматы, часто от нишевых или инди-брендов, поэтому это также будет учитываться в выдаче модели. 

Кроме того, я ожидаю пользователей, которые наоборот не слишком разбираются в парфюмерии и либо ищут рекомендации для покупки приятных и универсальных ароматов, либо подбирают подарок.
Несмотря на то, что идейно это совершенно другая категория, с точки зрения алгоритма эти пользователи не сильно отличаются от энтузиастов, просто их поле поиска смещено к более "попсовым" ароматам.

## Взаимодействие пользователя с продуктом

Доступ к системе будет осуществляться через веб-интерфейс. Для начала работы пользователю требуется заполнить небольшой опросник: 

1. Давайте подберём аромат! Какой парфюм вы ищете?
* Для себя
* В подарок
* На особый случай
* Пока не знаю, просто смотрю

2. Есть ли у вас любимые ароматы? Выберите из списка или пропустите.

3. Какие ноты или стили вам ближе? 

Благодаря этому опроснику, можно легко дифференциировать пользователей и далее использовать паттерны, характерные для каждой группы.

## Продуктовые метрики

| Метрика               | Что показывает                                              | Почему важна                                                |
|-----------------------|-------------------------------------------------------------|-------------------------------------------------------------|
| **Recommendation CTR** | Насколько пользователи кликают на предложенные ароматы     | Показывает, цепляет ли выдача, насколько релевантен результат |
| **Retention D1/D7**   | Возвращаются ли пользователи спустя 1 и 7 дней              | Отражает интерес к продукту и потенциал LTV                 |
| **Recall@K**          | Доля "релевантных" ароматов в топ-K рекомендациях           | Объективная метрика качества модели, особенно для A/B тестов |

## Привлечение пользователей

Для привлечения пользователей есть много возможностей: "сарафанное радио" в парфюмерном сообществе работает замечательно.
Например, парфблоггеры разных масштабов (у популярных больше охват, к начинающим больше доверия), тематические сообщества на Reddit/twitter, местные оффлайн-сообщества. 
Несмотря на то, что это очень крупная индустрия, существует всего два больших информационных ресурса, посвящённых парфюмерии (fragrantica и parfumo), но они служат, скорее, как база данных с отзывами, а рекомендательная часть не развита и работает плохо. 
Поэтому запрос на подобную вещь среди энтузиастов присутствует.

## Бизнес-модель

Бизнес-модель основана на получении выгоды с контекстной рекламы: парфюм порекомендован — показываем ссылки, где можно его купить. Не раздражает пользователя и даже полезно!
