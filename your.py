from random import choice
from string import ascii_letters

print(''.join(choice(ascii_letters) for i in range(12))) #генерация случайной строки из 12 символов