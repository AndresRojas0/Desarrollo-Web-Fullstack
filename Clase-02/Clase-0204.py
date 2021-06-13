# 4. Escribe un programa en Python que muestre la hora actual con una suma de dos horas adicionales.

import datetime

horasdif = 2
miHora = datetime.datetime.now().hour
miMinuto = datetime.datetime.now().minute
print('Mi hora actual con suma de: ',horasdif,' horas es: ',miHora+horasdif,':',miMinuto)