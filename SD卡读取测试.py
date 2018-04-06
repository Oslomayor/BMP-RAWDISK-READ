# Apr, 6th, 2:09PM @ dorm 602 , Sun
# 没有文件系统的SD卡读取测试

file = open('E:/Allbackup/Snadisk16GB-backup/allbmp/data.bmp','wb')
disk = open('\\\\.\\PhysicalDrive1', 'rb')
data = disk.read(40910133)
file.write(data[1309824*16:1309824*16+4147254])
file.close()

