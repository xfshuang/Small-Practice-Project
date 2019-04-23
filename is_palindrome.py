#!/usr/local/bin/python3 
# Name: Shirley Huang
# File: wk3_ex.py
# Desc: Write a function named is_palindrome() that returns boolean True or False
# Date: 04-21-2019


def is_palindrome(string):
    import re
    #'\W'= Not a word character
    #sub() == replace "\W" with an empty space in a string all lower case
    word = re.sub('\W', '', string.lower())
    rev_work = word[::-1] # [::-1]reverse of word
    if word == rev_work:
        return True
    else:
        return False


valid_palindromes = ["Dennis, Nell, Edna, Leon, Nedra, Anita, Rolf, Nora, Alice, Carol, Leo, Jane, Reed, Dena, Dale, Basil, Rae, Penny, Lana, Dave, Denny, Lena, Ida, Bernadette, Ben, Ray, Lila, Nina, Jo, Ira, Mara, Sara, Mario, Jan, Ina, Lily, Arne, Bette, Dan, Reba, Diane, Lynn, Ed, Eva, Dana, Lynne, Pearl, Isabel, Ada, Ned, Dee, Rena, Joel, Lora, Cecil, Aaron, Flora, Tina, Arden, Noel, and Ellen sinned.",
                     "Depardieu, go razz a rogue I draped.",
                     "Desserts I stressed.",
                     "Detartrated.",
                     "Devo met a Mr., eh, DNA and her mate moved.",
                     "Di as dad said.",
                     "Did I draw Della too tall, Edward? I did?",
                     "Dior droid.",
                     "DNA-land.",
                     "Do geese see god?",
                     "Do good? I? No. Evil anon I deliver. I maim nine more hero-men in Saginaw, sanitary sword a-tuck, Carol, I. Lo! Rack, cut a drowsy rat in Aswan. I gas nine more hero-men in Miami. Reviled, I (Nona) live on. I do, O God.",
                     '"Do nine men interpret?" "Nine men," I nod.']

invalid_palindromes =  ["abracadabra!",
"Mister, mister, on a see-saw with your sister.",
"Almost every sentence is NOT a palindrome! How unfair!"]

for valid in valid_palindromes:
    print(is_palindrome(valid))

for invalid in invalid_palindromes:
    print(is_palindrome(invalid))
