# DSC510
# Week 9
# Programming Assignment - 9.1
# Author: Ganesh Kale
# Date: 02/14/2021
# The purpose of this program is to read file and write output to file.

import string
# import csv

# function to add word to dictionary and update count


def add_word(word, word_dict):
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1


# function to remove punctuations, space from the lines


def process_line(line, word_dict):
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.strip()
    line = line.lower()
    words = line.split()
    for word in words:
        add_word(word, word_dict)


# function to write the length of dictionary and word frequency in CSV file


# def process_file(word_dict,file_name):
#     file_name = file_name+'.csv'
#     with open(file_name,mode='w') as file:
#       writer = csv.writer(file,delimiter=',',quoting=csv.QUOTE_MINIMAL)
#       writer.writerow(['Length of the dictionary:',len(word_dict)])
#       writer.writerow(['Word','Count'])
#       for key, val in word_dict.items():
#         writer.writerow([key,val])


# function to write the length of dictionary and word frequency in text file


def process_file(word_dict,file_name):
    if '.' not in file_name:
        file_name = file_name+'.txt'   # w/o adding extension it creates text file, adding extension to be specific
    else:
        file_name = file_name
    word, count = 'Word', 'Count'
    with open(file_name,mode='w') as file:
        file.write(f'Length of the dictionary: {len(word_dict)}\n')
        file.write(f'\n{word:<20}{count}\n')
        file.write(f'-------------------------\n')
        for key, val in word_dict.items():
            file.write(f'{key:<20}{val}\n')


# function to open file


def main():
    word_dict = {}
    try:
        with open('Gettysburg.txt') as gba_file:
            for line in gba_file:
                process_line(line, word_dict)
        word_dict = dict(sorted(word_dict.items(), key=lambda x: x[1], reverse=True))   # sort the dictionary by count desc
        file_name = input('Please enter the file name to save result data in : \n')
        process_file(word_dict,file_name)
    except Exception as ex:
        print('Error Occurred while opening file: ', ex)


if __name__ == '__main__':
    main()
