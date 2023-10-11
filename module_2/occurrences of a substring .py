s1 = 'jaydipahir'
s2 = 'ahir'
count = 0
sub_len = len(s2)
for i in range(len(s1)):
    if s1[i:i+sub_len] == s2:
     count+=1
print(count)

