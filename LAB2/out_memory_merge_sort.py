import random
import tempfile
import os

def file_len(path):
    lines=0
    with open(path, 'r') as f:
        for line in f:
            lines+=1
    return lines

def by_index(path, index):
    res=0
    with open(path,'r') as f:
        for i in range(index+1):
            res=int(f.readline())
    return res

def replace(path, index, num):
    with tempfile.NamedTemporaryFile(mode='w', delete=False,suffix='.txt') as temp_f_write:
        with open(path,'r') as f:
            for line in f:
                temp_f_write.write(line)
        temp_path = temp_f_write.name
    with open(temp_path, 'r') as temp_f_read:
        with open(path, 'w') as f:
            for i in range(file_len(temp_path)):
                if i == index:
                    f.write(str(num) + '\n')
                else:
                    f.write(temp_f_read.readline())
    os.remove(temp_path)

def slice_to_end(target_path, source_path, index):
    with open(source_path,'r') as source_f:
        with open(target_path,'w') as target_f:
            for i in range(index):
                target_f.write(source_f.readline())

def slice_from_begin(target_path, source_path, index):
    with open(source_path,'r') as source_f:
        with open(target_path,'w') as target_f:
            for i in range(index):
                source_f.readline()
            for i in range(file_len(source_path) - index):
                target_f.write(source_f.readline())

def merge_sort(path):
    if file_len(path) > 1:
        center = random.randint(0,file_len(path)-1)
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as left:
            with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as right:
                slice_to_end(left.name,path,center)
                slice_from_begin(right.name,path,center)
                merge_sort(left.name)
                merge_sort(right.name)
                i = 0
                j = 0
                k = 0
                while i < file_len(left.name) and j < file_len(right.name):
                    if by_index(left.name,i) < by_index(right.name,j):
                        replace(path,k,by_index(left.name,i))
                        i += 1
                    else:
                        replace(path, k, by_index(right.name, j))
                        j += 1
                    k += 1

                while i < file_len(left.name):
                    replace(path,k,by_index(left.name,i))
                    i += 1
                    k += 1

                while j < file_len(right.name):
                    replace(path, k, by_index(right.name, j))
                    j += 1
                    k += 1
        os.remove(left.name)
        os.remove(right.name)

def create(file_name, count, rad):
    with open(file_name, 'w') as f:
        f.writelines('{}\n'.format(random.randint(-rad, rad)) for _ in range(count))