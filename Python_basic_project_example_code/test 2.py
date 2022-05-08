import sys

##변수 선언 부분##
size_int, size_float, size_bool, size_str, size_list, size_tuple, size_dict, size_set = [None]*8

##메인 코드 부분##

if __name__ == "__main__":

    size_int = 0  
    size_float = 0.0  
    size_bool = False 
    size_str = ''
    size_list = []
    size_tuple = ()
    size_dict = {}
    size_set = set()

    ## 2018038025 정하용 ##

    print('int형 기본 크기 -->', sys.getsizeof(size_int))
    print('float형 기본 크기 -->', sys.getsizeof(size_float))
    print('bool형 기본 크기 -->', sys.getsizeof(size_bool))
    print('str형 기본 크기 -->', sys.getsizeof(size_str))
    print('list형 기본 크기 -->', sys.getsizeof(size_list))
    print('tuple형 기본 크기 -->', sys.getsizeof(size_tuple))
    print('dictionary형 기본 크기 -->', sys.getsizeof(size_dict))
    print('set형 기본 크기 -->', sys.getsizeof(size_set))
    
