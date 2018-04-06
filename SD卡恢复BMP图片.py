# Apr, 6th, 3:16PM @ dorm 602 , Sun
# 没有文件系统的SD卡，从中恢复BMP图片

BMPsize = 4147254
BMPgap = 259232
BMPstartADDR = 1309824

disk = open('\\\\.\\PhysicalDrive1', 'rb')
# 7200646656+BMPsize
# read的参数太大会报错 OSError
data = disk.read(720064665)

for i in range(0,168):
    file = open('E:/Allbackup/Snadisk16GB-backup/allbmp/{}.bmp'.format(i), 'wb')
    file.write(data[(BMPstartADDR+BMPgap*i)*16:(BMPstartADDR+BMPgap*i)*16+BMPsize])
    file.close()