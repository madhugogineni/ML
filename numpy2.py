import numpy as np;
r = np.arange(36);
r.resize((6,6));
# print(r[:2,:-1]);
# print(r[r > 10]);# returns all the values that satisify the condition
r_copy = r.copy();# this wont change the original array
r_Copy1 = r[:2];#whem changes are done to r_copy1 that will also affect r array.
test = np.random.randint(0,10,(4,3));# this will create an array of size 4,3 consisting of values ranging from 0-10.
print(test.size);
test1 = test**2;
for i,row in enumerate(test):
	print("row "+str(i)+" is "+str(row));
# enumerate provides the means to get both the row index and the row itself
for i,j in zip(test,test1):
	print(i,'+',j,"=",i+j);
temp = lambda x : x+1;
print(temp(10));



