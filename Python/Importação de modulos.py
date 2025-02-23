# Teste com importação de modulos em python

import math
import random
import datetime


# módulo matemático

resultado = math.sqrt(25)
print(resultado) # Aparecerá a raiz quadrada de 50


# módulo aleatorio

random_number = random.randint(1,15)
print(random_number) # Aparecerá um numero aleatório entre 1 e 15


# módulo de data

current_date = datetime.datetime.now()
print(current_date) # Aparecerá a data e o horário atual