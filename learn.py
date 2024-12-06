'''x = int(input())
f = []
get = input()
f = list(map(int, get.split()))
sum = 0

for y in range(len(f)) :
    sum += f[y]

print(abs(sum))'''

# x = int(input())
# f = []
# get = input()
# f = list(map(int, get.split()))
# find = int(input())
# if find in f :
#     print(f.index(find))
# else : 
#     print(-1)




# task2
# def con(x) :
#     if int(x) >0 :
#     # return str( (int(x) )*-1)+" "
#        return "1 "
#     elif int(x) <0 :
#        return "2 "
#     else :
#        return "0 "

# x = input()
# f = list(map(con,input().split()))
# if f :
#    f[-1].strip()
# for y in range(len(f)) :
#     print(f[y])
#     if y == len(f)-1 :
#         break
#     print(" ")
# res = "".join(f)
# print(res)



x = input()
arr = list(map(int,input().split()))

res = list(filter(lambda x : x<=10 , arr))

for i , v in enumerate(arr) :
    if v in res :
        print(f"A[{i}] = {v}".strip())


#what about enumerate emplemntaion
# def my_enumerate(iterable, start=0):
#     # 'start' will be the index at which we begin counting.
#     index = start
#     for item in iterable:
#         yield index, item  # Yield the index and the value from the iterable
#         index += 1  # Increment the index for the next iteration
