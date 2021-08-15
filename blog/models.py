'''
тут прописываются модели,
 чтобы пользователь мог взаимодействовать с сайтом.
у нас есть три поля ввода: заголовок, описание, дата.
Чтобы зарегистрировать модель - мы переходим в файл этого же приложения admin.py
 и пишем то, что там расположено на 4 строке, не забывая импортировать эту модель.
Вот, теперь у нас есть готовая модель, и в админке мы моежт ввести в эти поля инфу,
 чтобы она внеслась в базу данных и могла использоваться и не теряться в дальнейшем.
Далее, во views.py этого приложения мы вытягиваем всю инфу из БД, чтобы на html-странице её показать.
'''

from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title