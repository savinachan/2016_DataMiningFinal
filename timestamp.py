import pytz
import datetime
import time
import pandas as pd
import numpy as np

url = 'test.csv'
data = pd.read_csv(url)

H8=[]
M8=[]
P8=[]
H9=[]
M9=[]
P9=[]
H10=[]
M10=[]
P10=[]
H11=[]
M11=[]
P11=[]
H12=[]
M12=[]
P12=[]

for num in data.values:
	#print num[0]

	#T = datetime.datetime.fromtimestamp(num[5]).strftime('%Y-%m-%d (%w) %H:%M')
	m = datetime.datetime.fromtimestamp(num[5]).strftime('%m')
	# d = datetime.datetime.fromtimestamp(num[5]).strftime('%d')
	# w = datetime.datetime.fromtimestamp(num[5]).strftime('%w')
	H = datetime.datetime.fromtimestamp(num[5]).strftime('%H')
	M = datetime.datetime.fromtimestamp(num[5]).strftime('%M')

	if int(m) == 8:
		H8.append(int(H))
		M8.append(int(M))
		P8.append(num[8])
	if int(m) == 9:
		H9.append(int(H))
		M9.append(int(M))
		P9.append(num[8])
	if int(m) == 10:
		H10.append(int(H))
		M10.append(int(M))
		P10.append(num[8])
	if int(m) == 11:
		H11.append(int(H))
		M11.append(int(M))
		P11.append(num[8])
	if int(m) == 12:
		H12.append(int(H))
		M12.append(int(M))
		P12.append(num[8])
	#print T
# w = 0 => 7

df8 = pd.DataFrame({ 'HOUR' : H8,
					'MINUTE': M8,
					'POLYLINE':P8})
df9 = pd.DataFrame({ 'HOUR' : H9,
					'MINUTE': M9,
					'POLYLINE':P9})
df10 = pd.DataFrame({ 'HOUR' : H10,
					'MINUTE': M10,
					'POLYLINE':P10})
df11 = pd.DataFrame({ 'HOUR' : H11,
					'MINUTE': M11,
					'POLYLINE':P11})
df12 = pd.DataFrame({ 'HOUR' : H12,
					'MINUTE': M12,
					'POLYLINE':P12})
df8.to_csv('test_8.csv',index=False)
df8.to_csv('test_9.csv',index=False)
df8.to_csv('test_10.csv',index=False)
df8.to_csv('test_11.csv',index=False)
df8.to_csv('test_12.csv',index=False)
#print df8

