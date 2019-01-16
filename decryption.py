import helpers
import numpy
import random


class Decryptor:

    @staticmethod
    def de_shuffle(string, seed):
        stringlist = list(string)

        order = list(range(len(string)))

        random.Random(seed).shuffle(order)

        originallist = [0] * len(string)
        for index, originalindex in enumerate(order):
            originallist[originalindex] = stringlist[index]

        originalstring = ''.join(originallist)

        return originalstring

    @staticmethod
    def de_shift(string, list_seed, msg_seed):

        chars_list = helpers.string_shuffler(list_seed)

        numpy.random.seed(msg_seed)
        shift_vals = []
        for i in range(len(string)):
            shift_vals.append(numpy.random.randint(len(chars_list)))

        original_message = ''
        index = 0
        for char in string:

            master_chars_pos = chars_list.index(char)
            shift_to = master_chars_pos - shift_vals[index]
            if shift_to < 0:
                shift = len(chars_list) - shift_vals[index] + master_chars_pos
                original_message += chars_list[shift]

            else:
                original_message += chars_list[shift_to % len(chars_list)]
            index += 1

        return original_message

    @staticmethod
    def de_pad(string):
        sep = '     '
        remaining = string.split(sep, 1)[0]

        return remaining

    @staticmethod
    def decrypt(message, seed):
        """Decrypt a given message string with a given password string (seed)."""
        x = helpers.seed_generator(seed, 3)
        res = Decryptor.de_shuffle(message, x[2])
        res2 = Decryptor.de_shift(res, x[0], x[1])
        res3 = Decryptor.de_pad(res2)

        return res3

