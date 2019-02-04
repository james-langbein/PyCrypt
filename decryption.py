import helpers
import numpy
import random


class Decryptor:

    @staticmethod
    def de_split(string):
        return string.replace(' ' * 5, '')

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
    def de_pad(string, delim_seed):
        sep = helpers.delimiter(delim_seed)
        remaining = string.split(sep, 1)[0]

        return remaining

    @staticmethod
    def decrypt1(message, seed):
        """Decrypt a given message string with a given password string (seed)."""
        x = helpers.seed_generator(seed, 4)
        res = Decryptor.de_shuffle(message, x[3])
        res2 = Decryptor.de_shift(res, x[1], x[2])
        res3 = Decryptor.de_pad(res2, x[0])

        return res3

    @staticmethod
    def decrypt2(message, seed):
        """Decrypt a given message string with a given password string (seed)."""
        x = helpers.seed_generator(seed, n=6)
        res = Decryptor.de_shuffle(message, x[5])
        res2 = Decryptor.de_shift(res, x[3], x[4])
        res3 = Decryptor.de_pad(res2, x[2])
        res4 = Decryptor.de_shift(res3, x[0], x[1])
        res5 = Decryptor.de_split(res4)

        return res5

    @staticmethod
    def decrypt3(message, seed, rounds=5):
        d = Decryptor()

        seeds = helpers.seed_generator(str(seed), n=2)
        x1 = helpers.seed_generator(seeds[0], n=3)
        x2 = helpers.seed_generator(seeds[1], n=rounds)

        x2_reversed = x2[::-1]
        r_res = message
        for i in range(rounds):
            r_seed = helpers.seed_generator(x2_reversed[i], n=3)
            r_res = d.de_shuffle(string=r_res, seed=r_seed[2])
            r_res = d.de_shift(string=r_res, list_seed=r_seed[0], msg_seed=r_seed[1])

        res = d.de_pad(r_res, delim_seed=x1[2])
        res2 = d.de_shift(res, x1[0], x1[1])
        res3 = d.de_split(res2)

        return res3

    @staticmethod
    def decrypt4(message, seed, max_rounds=42):
        d = Decryptor()

        seeds = helpers.seed_generator(str(seed), n=2)
        x1 = helpers.seed_generator(seeds[0], n=3)
        x2 = helpers.seed_generator(seeds[1], n=max_rounds)

        delimiter = helpers.delimiter(x1[2])
        r_res = message
        for i in range(max_rounds):
            r_seed = helpers.seed_generator(x2[i], n=3)
            r_res = d.de_shuffle(string=r_res, seed=r_seed[2])
            r_res = d.de_shift(string=r_res, list_seed=r_seed[0], msg_seed=r_seed[1])
            if delimiter in r_res:
                break

        res = d.de_pad(r_res, delim_seed=x1[2])
        res2 = d.de_shift(res, x1[0], x1[1])
        res3 = d.de_split(res2)

        return res3
