#!/usr/bin/env python3
import prandom
#import logging
#from secret import config 


def getseed():
    seed = ''
    for i in range(9):
        x = prandom.v8random()
        logging.info(x[:-1])
        seed += str(x[-1])[2:]
    return int(seed)

def get_key(seed):
    lcg = prandom.LCG(seed)
    #for i in range(7):
    #    logging.info(lcg.next())
    key = lcg.next()
    return key

def flag_to_str(flag):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_{}'
    flag_int = [chars.index(i) for i in flag]
    flag_int = ['0'*(2-len(str(i)))+str(i) for i in flag_int]
    return ''.join(flag_int)

def xor(flag, key):
    flag = flag_to_str(flag)
    n1, n2 = len(flag), len(key)
    n = max(n1, n2)
    key1, flag1 = '', ''
    for i in range(n):
        key1 += key[i%n2]
        flag1 += flag[i%n1]
    return int(key1)^int(flag1)


def main():
    #logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s')
    #seed = getseed()
    seed = 87330119579350931862914191409508298456165858477767023615567092714295712681283818679274630368249883328161236230265577893701355572435322043006049888
    key = get_key(seed)
    print(key)
    #encrypted_flag = xor(config.flag, str(key))
    #with open('encrypted_flag.txt', 'w') as f:
    #    f.write(str(encrypted_flag))

if __name__=='__main__':
    main()