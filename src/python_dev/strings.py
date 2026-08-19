msg = 'This is a basic example of string manipulation in Python.'
msg1 = msg[:4]+' '+msg[10:15]+msg[26:33]+msg[4:7] + \
    msg[15:23]+msg[15]+msg[1]+msg[-2]+msg[-7]
print(msg1.title())
print(msg1[::-1].title())

name = 'IGRIS'
color = 'Blue'
msg = '[' + name + '] loves the color ' + color.lower() + '!'
msg1 = f'[{name.capitalize()}] loves the color {color.lower()}!'
print(msg)
print(msg1)
