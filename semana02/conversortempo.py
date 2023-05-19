segundos = int(input('Por favor, entre com o número de segundos que deseja converter: '))

dias = segundos // 86400
diasResto = segundos % 86400
horas = diasResto // 3600
segundosRestantes = segundos % 3600
minutos = segundosRestantes // 60
segundosRestantesFinal = segundosRestantes % 60


print(f'{dias} dias, {horas} horas, {minutos} minutos e {segundosRestantesFinal} segundos.')