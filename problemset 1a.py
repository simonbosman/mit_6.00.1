s = 'azcbobobegghakl'
vowels = 'aeiou'
cnt = 0

for char in s:
    if char in vowels:
        cnt += 1

print 'Number of vowels: ' + str(cnt)
