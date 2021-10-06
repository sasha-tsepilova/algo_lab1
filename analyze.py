from sortings import *
from copy import copy
from random import choices
import json
import timeit

def generator_1(size: int):
    arr = choices(range(-100000,100000),k=size)
    return arr

def generator_2(size: int):
    return sorted(generator_1(size))

def generator_3(size: int):
    return sorted(generator_1(size),reverse=True)

def generator_4(size: int):
    arr = choices(range(1,3),k=size)
    return arr


timeit.template = """
def inner(_it, _timer{init}):
    {setup}
    _t0 = _timer()
    for _i in _it:
        retval = {stmt}
    _t1 = _timer()
    return _t1 - _t0, retval
"""

def gen_result (generator, repeats: int):
    gen_res = {}
    sortings = [selection_sort, insertion_sort, merge_sort, shell_sort]
    for i in range(repeats):
                    
        arr = generator(size)
        for sorting in sortings:
            arr_c = copy(arr)
            timer = timeit.timeit("sorting(arr_c)[1]" ,globals= {"sorting":sorting, "arr_c":arr_c}, number=1)
            time_used = timer[0]
            comp = timer[1]
            if sorting.__name__ in gen_res:
                gen_res[sorting.__name__]['comparisons'] += comp
                gen_res[sorting.__name__]['time'] += time_used
            else:
                gen_res[sorting.__name__] = {}
                gen_res[sorting.__name__]['comparisons'] = comp
                gen_res[sorting.__name__]['time'] = time_used
    for sorting in sortings:
        gen_res[sorting.__name__]['comparisons'] /= repeats
        gen_res[sorting.__name__]['time'] /= repeats
    return gen_res

if __name__ == "__main__":
    generators = [generator_1, generator_2, generator_3, generator_4]
    results = {}
    size = 2**7
    while size<=2**15:
        res_size = {}
        for generator in generators:
            gen_res = {}
            if generator.__name__ == 'generator_1':
                gen_res = gen_result(generator, 5)
            elif generator.__name__ == 'generator_4':
                gen_res = gen_result(generator, 3)
            else:
                gen_res = gen_result(generator, 1)
            res_size[generator.__name__] = gen_res
        results[size] = res_size
        print(res_size)
        size *= 2
    print(results)
    with open('res.json','w') as fout:
        fout.write(json.dumps(results))
