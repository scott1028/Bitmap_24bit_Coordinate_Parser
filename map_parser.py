# coding:utf-8
# 解析 24bit 的 BMP檔案格式

import binascii,re

def cal_size(ldata):
	ss=0
	for i in range(0,len(ldata)):
		ss+=int(ldata[i],16)*(16**i)
	return ss

f=open('像素解析.bmp'.decode('utf-8'),'r')
r=f.read()
lRawData=re.findall('..',binascii.b2a_hex(r))				# 轉為兩兩一組

print len(lRawData)

# print lRawData[14:16]
print 'n Width:',cal_size(lRawData[18:22])					# 寬度
print 'n Height:',cal_size(lRawData[22:26])					# 高度
print 'n bits/per pixel:',cal_size(lRawData[28:30])			# 每一個 Pixel 的大小
print 'if compressed:',lRawData[32:34]						# 此圖是否壓縮
print 'rawData Size:',cal_size(lRawData[34:38])				# 點陣圖資料大小
# print lRawData[38:42]										# 水平解析度
# print lRawData[42:46]										# 垂直解析度
# print lRawData[46:50]										# 調色盤的顏色數
# print lRawData[50:54]										# 重要的顏色個數
print '\n'
print 'RawData Size Calculate 4*4*3=',4*4*3 				# 長寬各為4,每個像速點為3個Bytes
# print lRawData[54:]										# 資料部分

# 將資料轉入陣列
lRawData_reduce=[]
for i in xrange(cal_size(lRawData[22:26])):
	k=lRawData[54:][3*cal_size(lRawData[18:22])*i:3*cal_size(lRawData[18:22])*(i+1)]
	lRawData_reduce.append(k)

# 排序資料為人類接受的格式
lRawData_reduce.reverse()
print lRawData_reduce

print '\nPointer Coordinate...'
y=0
for cs in lRawData_reduce:
	x=0
	while x<len(cs):
		k=[cs[x],cs[x+1],cs[x+2]]==['00','00','00']
		print (x,y),'W' if k else 'B'						# 三元運算式
		x+=3
	y+=1

