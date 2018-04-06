# Apr, 5th, 9:03PM @ dorm 602 , Rain
# BMP 图像恢复
# 输入是字符串形式的16进制代码，类似这样：
# 424D36483F00000000003600000
# 要将它转成字节流，才能生成BMP图片

new = b''
dir = 'E:\Allbackup\Snadisk16GB-backup\\bmp\\2.txt'
f = open(dir,'r')
content = f.read()
new += bytes.fromhex(content)
print(new)
file = open('E:\Allbackup\Snadisk16GB-backup\\bmp\\2.bmp','wb')
file.write(new)
file.close()
print('succeed!')
