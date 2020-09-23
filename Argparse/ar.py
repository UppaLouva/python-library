# -*- coding: utf-8 -*-

import argparse 

parser = argparse.ArgumentParser()

parser.add_argument("-i")
parser.add_argument("-s")
parser.add_argument("-n",type=int)
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-isim")
parser.add_argument("-soyisim")
parser.add_argument("-no",type=int)

veri =parser.parse_args()  #Gelen argumanlar burada ayrılır

if veri.isim:
    print("isim:{}".format(veri.isim))
elif veri.soyisim:
    print("soyisim:{}".format(veri.soyisim))
elif veri.no:
    print("no:{}".format(veri.no))


