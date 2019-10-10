#!/bin/python3
import urllib.request
import permutations
import multiprocessing as mp
import csv
from bs4 import BeautifulSoup
from threading import Thread
from collections import deque

done = False

def write_file(filepath, q):
    f = open(filepath):
        while(!done):
            if(len(q) > 0):
                f.write(q.pop_left())


q = deque()
def parse_url(path):
    url = "https://beav.es/{}".format(path)
    title = ""
    result_url = ""
    # print("{}: ".format(path), end="")
    try:
        response = urllib.request.urlopen(url)
        soup = BeautifulSoup(response, "lxml")
        title = soup.title.string
        result_url = response.geturl()
    except:
        pass
    print("{}`{}`{}".format(path, title, result_url))

if __name__ == '__main__':
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']

    perms = permutations.permute(2,letters)
    perms = list(map(lambda s: 'Z' + s, perms))
    # print("Parsing {} URLs.".format(len(perms)))
 
    tr = Thread(write_file, args=("beaves_out.csv", q)) 
    tr.start()

    pool = mp.Pool(mp.cpu_count())

    pool.map(parse_url, [path for path in perms])

    pool.close()
    done = True
    tr.join()


    # print("Done! wrote output to beaves_out.csv")
