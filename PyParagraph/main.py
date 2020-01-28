# Dependencies
import os
import csv
import re

# Path to txt
paragraph_txt = os.path.join('Resources', 'paragraph.txt')
paragraph_txt_output = os.path.join('Resources', 'paragraph_output.txt')

paragraph = ''
letter_count = []
word_per_sentence = []

# Openning csv
with open(paragraph_txt) as txtfile:
    paragraph = txtfile.read().replace('\n', ' ')
    # Approximate word count
    word_split = paragraph.split(' ')
    word_count = len(word_split)
    # Approximate sentence count
    for word in word_split:
        letter_count.append(len(word))
    # Average letter count (per word)
    average_letter_count = sum(letter_count) / float(len(letter_count))
    # Average sentence length (in words)
    sentence_split = re.split("(?<=[.!?]) +", paragraph)
    sentence_count = len(sentence_split)
    for sentence in sentence_split:
        word_per_sentence.append(len(sentence.split(' ')))
    average_sentence_length = sum(word_per_sentence) / float(len(word_per_sentence))

paragraph_output = (f"\nParagraph Analysis\n"
                    f"---------------------\n"
                    f"Approximate Word Count: {word_count}\n"
                    f"Approximate Sentence Count: {sentence_count}\n"
                    f"Average Letter Count: {average_letter_count}\n"
                    f"Average Sentence Length: {average_sentence_length}\n")

with open(paragraph_txt_output, 'a') as txt_file:
    txt_file.write(paragraph_output)
    