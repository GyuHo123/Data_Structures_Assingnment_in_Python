import numpy as np
import time

def insertion_sort(data):
    for stand in range(len(data) - 1):
        for num in range(stand + 1, 0, -1):
            if data[num] < data[num - 1]:
                data[num], data[num - 1] = data[num - 1], data[num]
            else:
                break

def selection_sort(data):
    for stand in range(len(data) - 1):
        lowest = stand
        for index in range(stand, len(data)):
            if data[lowest] > data[index]:
                lowest = index
        data[stand], data[lowest] = data[lowest], data[stand]
    return data

def heap_sort(data):
    n = len(data)
    for i in range(n):
        c = i
        while c != 0:
            r = (c - 1) // 2
            if (data[r] < data[c]):
                data[r], data[c] = data[c], data[r]
            c = r
    for j in range(n - 1, -1, -1):
        data[0], data[j] = data[j], data[0]
        r = 0
        c = 1
        while c < j:
            c = 2 * r + 1
            if (c < j - 1) and (data[c] < data[c + 1]):
                c += 1
            if (c < j) and (data[r] < data[c]):
                data[r], data[c] = data[c], data[r]
            r = c

def merge_sort(data):
    if len(data) < 2:
        return data

    mid = len(data) // 2
    low_data = merge_sort(data[:mid])
    high_data = merge_sort(data[mid:])

    merged_data = []
    l = h = 0
    while l < len(low_data) and h < len(high_data):
        if low_data[l] < high_data[h]:
            merged_data.append(low_data[l])
            l += 1
        else:
            merged_data.append(high_data[h])
            h += 1
    merged_data += low_data[l:]
    merged_data += high_data[h:]
    return merged_data

def quick_sort(data):
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]
    lesser_data, equal_data, greater_data = [], [], []
    for num in data:
        if num < pivot:
            lesser_data.append(num)
        elif num > pivot:
            greater_data.append(num)
        else:
            equal_data.append(num)
    return quick_sort(lesser_data) + equal_data + quick_sort(greater_data)


def built_in_sort(data):
    data.sort()

if __name__ == "__main__":

    data_num = ['500', '1K', '5K', '10K', '100K']
    print("%14s" % '', end = '')
    for i in range(5):
        if(i == 0):
            print(data_num[i], end = '')
        else:
            print("%10s" % '', data_num[i], end = '')
        if(i == 4):
            print(end = '\n')

    data_files = ['test1.dat', 'test2.dat', 'test3.dat', 'test4.dat', 'test5.dat']
    result = list(); result1 = list(); result2 = list(); result3 = list(); result4 = list(); result5 = list()

    for f in data_files:
        data_file = open("/workspaces/Data_Structures_Assingnment_in_Python/dataset/{0}".format(f), 'r')
        data = data_file.readlines()
        start_time = time.time() * 1000
        selection_sort(data)
        end_time = time.time() * 1000
        result.append(round(end_time - start_time, 2))
        temp = np.array(result)
    print("selection     ", end='')
    for i in range(5):
        print("{0:>2}".format(temp[i]), "ms", '%-4.8s' % '', end = '')
        if (i == 4):
            print(end='\n')

    for f in data_files:
        data_file = open("/workspaces/Data_Structures_Assingnment_in_Python/dataset/{0}".format(f), 'r')
        data = data_file.readlines()
        start_time = time.time() * 1000
        heap_sort(data)
        end_time = time.time() * 1000
        result1.append(round(end_time - start_time, 2))
        temp1 = np.array(result1)
    print("     heap     ", end='')
    for i in range(5):
        print("{0:>2}".format(temp1[i]), 'ms', '%-5.9s' % '' ,end = '')
        if (i == 4):
            print(end='\n')

    for f in data_files:
        data_file = open("/workspaces/Data_Structures_Assingnment_in_Python/dataset/{0}".format(f), 'r')
        data = data_file.readlines()
        start_time = time.time() * 1000
        insertion_sort(data)
        end_time = time.time() * 1000
        result2.append(round(end_time - start_time, 2))
        temp2 = np.array(result2)
    print("insertion     ", end='')
    for i in range(5):
        print("{0:>2}".format(temp2[i]), "ms", '%-4.8s' % '', end = '')
        if (i == 4):
            print(end='\n')

    for f in data_files:
        data_file = open("/workspaces/Data_Structures_Assingnment_in_Python/dataset/{0}".format(f), 'r')
        data = data_file.readlines()
        start_time = time.time() * 1000
        quick_sort(data)
        end_time = time.time() * 1000
        result3.append(round(end_time - start_time, 2))
        temp3 = np.array(result3)
    print("    quick     ", end='')
    for i in range(5):
        print("{0:>2}".format(temp3[i]), 'ms', '%-6.5s' % '', end = '')
        if (i == 4):
            print(end='\n')

    for f in data_files:
        data_file = open("/workspaces/Data_Structures_Assingnment_in_Python/dataset/{0}".format(f), 'r')
        data = data_file.readlines()
        start_time = time.time() * 1000
        merge_sort(data)
        end_time = time.time() * 1000
        result4.append(round(end_time - start_time,2))
        temp4 = np.array(result4)
    print("    merge     ", end='')
    for i in range(5):
        print("{0:>2}".format(temp4[i]), 'ms', '%-6.5s' % '', end = '')
        if (i == 4):
            print(end='\n')

    for f in data_files:
        data_file = open("/workspaces/Data_Structures_Assingnment_in_Python/dataset/{0}".format(f), 'r')
        data = data_file.readlines()
        start_time = time.time() * 1000
        built_in_sort(data)
        end_time = time.time() * 1000
        result5.append(round(end_time - start_time, 2))
        temp5 = np.array(result5)
    print("   python     ", end="")
    for i in range(5):
        print("{0:>2}".format(temp5[i]), 'ms', '%-7.5s' % ' ', end='')
        if (i == 4):
            print(end='\n')

    data_file.close()
