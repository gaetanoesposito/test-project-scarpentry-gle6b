import sys

sum = 0.0
n=0.0

# Sum input values
# It's tough to read your English
for num in sys.stdin:
	sum += float(num)
	n+=1

print sum / n
