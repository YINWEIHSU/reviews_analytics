data = []
count = 0
x = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		len(data[count])
		x = x + len(data[count])
		count += 1
print('留言的平均長度是', x/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('總共有', len(new), '筆資料小於100')
