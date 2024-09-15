from collections import Counter
a='hello, i am manas'
b='aaaabbbbcc'
my_counter= Counter(a)
my_counter1= Counter(b)
print(my_counter)
print(my_counter1)
print(my_counter.most_common(1)[0][1])

