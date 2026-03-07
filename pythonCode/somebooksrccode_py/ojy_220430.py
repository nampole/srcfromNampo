Python 3.9.12 (tags/v3.9.12:b28265d, Mar 23 2022, 23:52:46) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print(0)
0
>>> games=['noodle', 'soccer', 'math', 'basketball']
>>> foods=['ramen', 'chicken']
>>> favorites=games+foods
>>> print(favorites)
['noodle', 'soccer', 'math', 'basketball', 'ramen', 'chicken']
>>> print(25*3+40*2)
155
>>> roof=25*3
>>> tunnel=40*2
>>> total=roof+tunnel
>>> print(total)
155
>>> name='joonyoung'
>>> family name='OH'
SyntaxError: invalid syntax
>>> family_name='OH'
>>> print('''Hi there, %s %s !''' %(name, family_name))
Hi there, joonyoung OH !
>>> print('''Hi there, aren't you here ~~ %s %s !''' %(name, family_name))
Hi there, aren't you here ~~ joonyoung OH !
>>> print('''Hi there, %s ^^^ %s !''' %(name, family_name))
Hi there, joonyoung ^^^ OH !
>>> ㅇ
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    ㅇ
NameError: name 'ᄋ' is not defined
>>> 