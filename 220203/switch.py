switch = int(input())

switch_list = list(map(int,input().split()))
switch_list = [0] + switch_list

students = int(input())
gender_list = list()
num_list = list()

for student in range(1,students+1):
    gender, num = list(map(int,input().split()))
    gender_list.append(gender)
    num_list.append(num)

for student in range(students):
    if(gender_list[student] == 1):
        for index in range(num_list[student],switch+1):
            if index%(num_list[student])==0:
                if switch_list[index]==0:
                    switch_list[index]=1
                else:
                    switch_list[index]=0

    if(gender_list[student] == 2):
        index = 0
        while num_list[student]-index>0 and num_list[student]+index<switch+1:
            if (switch_list[num_list[student]-index]!=switch_list[num_list[student]+index]):
                break
            else:
                if switch_list[num_list[student]-index]==0:
                    switch_list[num_list[student]-index]=1
                    switch_list[num_list[student]+index]=1
                    index += 1
                else:
                    switch_list[num_list[student]-index]=0
                    switch_list[num_list[student]+index]=0
                    index += 1

cnt = 0
for i in range(1,len(switch_list)):
    print(switch_list[i], end="")

    if cnt==20:
        print("")
        cnt=0
    else:
        print("", end=" ")
        cnt += 1