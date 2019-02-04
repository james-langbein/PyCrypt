import random
import numpy
import secrets


CHARS_LIST = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=~`{}[]|:;<>?/ .,'"


def string_shuffler(seed):
    res = list(CHARS_LIST)
    random.Random(seed).shuffle(res)
    return res


def seed_generator(inp, n):

    def seed_preprocessor(arg):
        if type(arg) == str:
            chars = string_shuffler(6835525)
            arg_num_list = []
            for char in arg:
                if char == '"':
                    ch = '/'
                    num = chars.index(ch)
                    arg_num_list.append(str(num))
                elif char == '\\':
                    ch = '/'
                    num = chars.index(ch)
                    arg_num_list.append(str(num))
                else:
                    num = chars.index(char)
                    arg_num_list.append(str(num))
            pre_num = ''.join(arg_num_list)  # returns a string of digits from arg
            pre_num = int(pre_num)
        elif type(arg) == int:  # shuffle chars_list based on arg and take first 16 chars
            chars = string_shuffler(arg)
            f16 = chars[:15]
            arg_num_list = []
            for char in f16:
                if char == '"':
                    ch = '/'
                    num = CHARS_LIST.index(ch)
                    arg_num_list.append(str(num))
                elif char == '\\':
                    ch = '/'
                    num = CHARS_LIST.index(ch)
                    arg_num_list.append(str(num))
                else:
                    num = CHARS_LIST.index(char)
                    arg_num_list.append(str(num))
            pre_num = ''.join(arg_num_list)  # returns a string of digits from arg
            pre_num = int(pre_num)

        # scale final_num down... using random.seed
        random.seed(pre_num)
        final_num = random.randint(0, 999999999)
        return final_num

    numpy.random.seed(seed_preprocessor(inp))
    res = []
    for i in range(n):
        res.append(numpy.random.randint(0, 999999999))
    return res


def rand_char():
    return secrets.choice(CHARS_LIST)


def delimiter(delim_seed, delim_size=10):
    numpy.random.seed(delim_seed)

    nums = []
    for k in range(delim_size):
        nums.append(numpy.random.randint(len(CHARS_LIST)))

    chars = []
    for j in nums:
        chars.append(CHARS_LIST[j])

    return ''.join(chars)
