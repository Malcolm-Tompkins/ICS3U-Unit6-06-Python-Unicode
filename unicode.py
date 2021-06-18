#!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on June 14, 2021
# Converts any input into Unicode

import hex_dict


def split(user_input):
    return [char for char in user_input]


def convert_to_hex(char_list):
    final_list = []
    length = len(char_list)
    loop_counter = 0
    for loop_counter in range(length):
        if char_list[loop_counter] in hex_dict.dictionary.keys():
            final_list.append(hex_dict.dictionary[char_list[loop_counter]])
    return final_list


def main():
    char_list = []
    user_input = (input("Enter your string to be converted to hex: "))
    char_list = split(user_input)
    convert_to_hex(char_list)
    string_in_hex = convert_to_hex(char_list)
    print("{0} in hex is: {1}".format(user_input, string_in_hex))
    print("Done.")


if __name__ == "__main__":
    main()
