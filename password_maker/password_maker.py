#-------------------------------------------------------------------------------
# Name:        password_maker
# Purpose:
#
# Author:      Carlos Cesar Caballero Díaz
#
# Created:     14/10/2012
# Copyright:   (c) Carlos Cesar Caballero Díaz 2012
# Licence:     GPLv3
#-------------------------------------------------------------------------------
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import random
import re

SUB_DICT = {" ":["-","_"],"o":["0"],"l":["1"],"i":["1"],"e":["3"],"s":["5"],"g":["9"],"t":["7"],"z":["2"],"b":["6"],
                "0":["o"],"1":["l"],"3":["E"],"5":["s"],"9":["g"],"7":["t"],"2":["z"],"6":["b"],"8":["&"]}
NO_EXTRAIN_CHAR_REGEXP = "[0-9a-zA-Z]"

len_strenght = 0.2
upper_case_strenght = 0.2
lower_case_strenght = 0.15
numeric_strenght = 0.2
extrin_char_strenght = 0.2
entropy_strenght = 0.05

total_len = 9
total_upper_case = 1
total_lower_case = 1
total_numeric = 1
total_extrain_char = 1
total_entropy = 3


def main():
    try:
        word = sys.argv[1]
    except:
        print "No password"
        sys.exit(1)
    print encode_word(word)

def encode_word(word):
    encoded = ""
    for let in word:
        encoded += change_let(let)
    return encoded

def change_let(let):
    upp = random.choice([True,False])
    try:
	    if upp:
	        let = SUB_DICT[let][random.randint(0,len(SUB_DICT[let])-1)]
    except:
        pass
    upp = random.choice([True,False])
    if upp:
        let = let.upper()
    return let

def how_secure(code):
    u"""return how secure is a str chain in porcent 100/100"""
    security_porcent = 0
    length = len(code)
#    if length == 0:
#        return 0.0
    upper_case = 0
    lower_case = 0
    numeric = 0
    extrain_char = 0

    entropy = {"upper_case":0,"lower_case":0,"numeric":0,"extrain_char":0}
    entropy_last = ""

    for let in code:
        if let.isupper():
            upper_case += 1
            if entropy_last == "upper_case" or entropy_last == "":
                entropy["upper_case"] +=1
                entropy["lower_case"] =0
                entropy["numeric"] =0
                entropy["extrain_char"] =0
        if let.islower():
            lower_case += 1
            if entropy_last == "lower_case" or entropy_last == "":
                entropy["lower_case"] +=1
                entropy["upper_case"] =0
                entropy["numeric"] =0
                entropy["extrain_char"] =0
        if let.isdigit():
            numeric += 1
            if entropy_last == "numeric" or entropy_last == "":
                entropy["numeric"] +=1
                entropy["upper_case"] =0
                entropy["lower_case"] =0
                entropy["extrain_char"] =0
        if not re.match(NO_EXTRAIN_CHAR_REGEXP,let):
            extrain_char += 1

    max_entropy = 0
    for key in entropy:
        if entropy[key] > max_entropy:
            max_entropy = entropy[key]
    max_entropy -= 1

    #print "------------------------------------"
    #print total_entropy
    len_porcent_part = _get_porcent(length,len_strenght,total_len)
    upper_case_porcent_part = _get_porcent(upper_case,upper_case_strenght,total_upper_case)
    lower_case_porcent_part = _get_porcent(lower_case,lower_case_strenght,total_lower_case)
    numeric_porcent_part = _get_porcent(numeric,numeric_strenght,total_numeric)
    extrain_char_porcent_part = _get_porcent(extrain_char,extrin_char_strenght,total_extrain_char)
    #entropy_porcent_part = _get_porcent(max_entropy,entropy_strenght,total_entropy)
    if max_entropy >= total_entropy:
        entropy_porcent_part = 0.0
    else:
        entropy_porcent_part = entropy_strenght * 100
    #print "ent str "+str(entropy_strenght)
    #print "ent porc "+str(entropy_porcent_part)
    #entropy_porcent_part = entropy_strenght * 100 - entropy_porcent_part
    #print "len "+str(len_porcent_part)
    #print "upper "+str(upper_case_porcent_part)
    #print "lower "+str(lower_case_porcent_part)
    #print "numeric "+str(numeric_porcent_part)
    #print "extrein "+str(extrain_char_porcent_part)
    #print "entropy "+str(entropy_porcent_part)
    return (len_porcent_part + upper_case_porcent_part + lower_case_porcent_part +
            numeric_porcent_part + extrain_char_porcent_part +entropy_porcent_part)

def _get_porcent(count,strenght,total):
    porcent_part = count * 100 / total
    if porcent_part > 100:
        porcent_part = 100
    porcent_part = porcent_part * strenght
    return porcent_part


if __name__ == '__main__':
    main()
