import helpers
import numpy
import random


class Encryptor:

    @staticmethod
    def pad(string, pad_size):
        pad_length = (pad_size - 5) - (len(string) % pad_size)
        init_pad = ' ' * 5

        pad = []
        for i in range(pad_length):
            pad.append(helpers.rand_char())

        pad_string = ''.join(pad)
        string += init_pad
        string += pad_string

        return string

    @staticmethod
    def shift(string, list_seed, msg_seed):
        chars_list = helpers.string_shuffler(list_seed)

        numpy.random.seed(msg_seed)

        shift_vals = []
        for i in range(len(string)):
            # shift values are within the range of the chars_list length
            shift_vals.append(numpy.random.randint(len(chars_list)))

        encrypted_message = ''
        index = 0
        for char in string:
            master_chars_pos = chars_list.index(char)
            shift = master_chars_pos + shift_vals[index]
            encrypted_message += chars_list[shift % len(chars_list)]
            index += 1

        return encrypted_message

    @staticmethod
    def shuffle(string, seed):
        res = list(string)
        random.Random(seed).shuffle(res)
        res2 = ''.join(res)

        return res2

    @staticmethod
    def encrypt(message, seed):
        """Encrypt a given message string with a given password string (seed)."""
        x = helpers.seed_generator(seed, n=3)
        res = Encryptor.pad(message, pad_size=1000)
        res2 = Encryptor.shift(string=res, list_seed=x[0], msg_seed=x[1])
        res3 = Encryptor.shuffle(string=res2, seed=x[2])

        return res3
