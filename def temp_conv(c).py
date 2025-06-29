def temp_conv(c):
    f = c * 1.8 + 32
    return f

c = float(input('输入温度摄氏度°C：'))
f = temp_conv(c)

print("转换为华氏温度为：" + str(f) + "°F")