uso_cpu = [
    [20, 25, 40, 50, 45, 60, 55, 35, 70, 65],
    [30, 35, 50, 60, 40, 55, 60, 45, 50, 55],
    [15, 20, 30, 25, 35, 40, 45, 50, 55, 60],
    [10, 15, 25, 35, 45, 50, 55, 60, 65, 70],
]


colunasKayque= [f"hora_{i+1}" for i in range(10)]

linhasKayque = ["us-east-1", "us-west-2", "eu-central-1", "sa-east-1"]


df = pd.DataFrame(uso_cpu, index=linhasKayque, columns=colunasKayque)

print(df)