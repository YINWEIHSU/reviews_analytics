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
