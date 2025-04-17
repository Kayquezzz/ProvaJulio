def grouper(iterable, n, fillvalue=None):
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


uso_cpu = [
20, 25, 40, 50, 45, 60, 55, 35, 70, 65,
30, 35, 50, 60, 40, 55, 60, 45, 50, 55,
15, 20, 30, 25, 35, 40, 45, 50, 55, 60,
10, 15, 25, 35, 45, 50, 55, 60, 65, 70]



for grupo in grouper(uso_cpu, n=10):
    # Remove os `None` do último grupo
    grupo = [num for num in grupo if num is not None]

    media = sum(grupo) / len(grupo)

    print(f"Grupo: {grupo!r}")
    print(f"- Média: {media}")