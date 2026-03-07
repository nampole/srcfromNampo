Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pickle
>>> game_data = {
	'player-position' : 'N23 E45',
	'pockets' : ['keys', 'pocket knife', 'polished stone'],
	'backpack' : ['rope', 'hammer', 'apple'],
	'money' : 158.50
	}
>>> save_file = open('save.dat', 'wb')
>>> pickle.dump(game_data, save_file)
>>> save_file.close
<built-in method close of _io.BufferedWriter object at 0x0000025E602FF460>
>>> save_file.close()
>>> print(save_file)
<_io.BufferedWriter name='save.dat'>
>>> load_file = open('save_dat', 'rb')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    load_file = open('save_dat', 'rb')
FileNotFoundError: [Errno 2] No such file or directory: 'save_dat'
>>> load_file = open('save.dat', 'rb')
>>> loaded_game_data = pickle.load(load_file)
>>> load_file.close()
>>> print(loaded_game_data)
{'player-position': 'N23 E45', 'pockets': ['keys', 'pocket knife', 'polished stone'], 'backpack': ['rope', 'hammer', 'apple'], 'money': 158.5}
>>> 