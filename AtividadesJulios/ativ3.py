import pandas as pd
uso_cpu = [
    [20, 25, 30, 50, 45, 60, 55, 35, 70, 65],
    [30, 35, 50, 60, 40, 55, 60, 59, 50, 55],
    [15, 20, 30, 25, 35, 40, 45, 50, 55, 60],
    [10, 15, 25, 35, 45, 50, 55, 60, 65, 70],
]

limite = 85

def alerta_uso(uso_cpu):
    for linha in uso_cpu:
        for cpu_uso in linha:
            if cpu_uso >= limite:
                return True
    return False

resultado = alerta_uso(uso_cpu)
print(resultado)
