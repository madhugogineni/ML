#list comprehension is an easier way to create lists with much less syntax problem.
listData = [number for number in range(10) ];
print(listData);
listData1 = [number for number in range(10) if(number % 2 == 0)];
print(listData1)