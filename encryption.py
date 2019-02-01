import helpers
import numpy
import random


class Encryptor:

    @staticmethod
    def group_split(string):
        """The idea for this one is that the if spaces are used as placeholders, an actual random number (ie not based
        on a given password/seed) can be used to split groups of characters. When decrypting, groups of spaces numbering
        x or more are simply removed, resulting in the original string before this method was used on it.
        The string result from this function can be shuffled/shifted to obscure the result."""

        str_list = list(string)
        l = len(str_list)
        """generate numbers between 2-4 and append 5 spaces after that number of characters after the last set."""
        start = 0
        loop = 0
        while True:
            n = random.randint(2, 3)
            if start + n + loop > len(str_list):
                break
            str_list.insert(start + n + loop, ' ' * 5)
            start += n
            loop += 1
        return ''.join(str_list)

    @staticmethod
    def end_pad(string, pad_size):
        """Pads the message with random characters.
        The result is the message string, followed by 5 spaces, followed by the random characters.
        The length of the full result will equal the given pad_size, unless the given pad is shorter than the given
        string, in which case it will equal the next multiple of 20 larger than the length of the string."""
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
    def char_shift(string, list_seed, msg_seed):
        """Shifts each individual character to another position in the given char set. The new position is determined by
        a random number generated from the a seed.
        list_seed > determines the result of the shuffled char set.
        msg_seed > determines the amount of shift for each character in the given string."""
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
    def char_shuffle(string, seed):
        """Shuffles an entire string so that each character is at a different index in the result.
        The shuffle positions are determined by the seed."""
        res = list(string)
        random.Random(seed).shuffle(res)
        res2 = ''.join(res)

        return res2

    @staticmethod
    def encrypt1(message, seed):
        """Encrypt a given message string with a given password.
        Each encryption of the same message will be different, aside from the shuffled/shifted characters of the
        original string.
        So, if the original string had 20 chars, then the encrypted result chars from that string will all be present in
        each full encryption result.
        This would present an opening to cryptographers if the same message was sent too many times with their
        knowledge. But only to the encrypted characters."""
        x = helpers.seed_generator(str(seed), n=3)
        res = Encryptor.end_pad(message, pad_size=1000)
        res2 = Encryptor.char_shift(string=res, list_seed=x[0], msg_seed=x[1])
        res3 = Encryptor.char_shuffle(string=res2, seed=x[2])

        return res3

    @staticmethod
    def encrypt2(message, seed):
        """Encrypt a given message string with a given password.
        Each encryption of the same message will be different, aside from the shuffled/shifted characters of the
        original string.
        So, if the original string had 20 chars, then the encrypted result chars from that string will all be present in
        each full encryption result.
        This would present an opening to cryptographers if the same message was sent too many times with their
        knowledge. But only to the encrypted characters."""
        x = helpers.seed_generator(str(seed), n=5)
        res = Encryptor.group_split(message)
        res2 = Encryptor.char_shift(res, x[0], x[1])
        res3 = Encryptor.end_pad(res2, pad_size=1000)
        res4 = Encryptor.char_shift(string=res3, list_seed=x[2], msg_seed=x[3])
        res5 = Encryptor.char_shuffle(string=res4, seed=x[4])

        return res5
