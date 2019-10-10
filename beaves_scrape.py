#!/bin/python3
import urllib.request
import permutations
import multiprocessing as mp
import csv
from bs4 import BeautifulSoup
from threading import Thread
from collections import deque

done = False

q = deque()
def write_file():
    with open("beaves_out.csv", "w") as f:
        while(not done):
            if(q):
                f.write(q.popleft())
            

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
    line = "{}`{}`{}\n".format(path, title, result_url)
    q.append(line)
    print(line)
if __name__ == '__main__':
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']

    perms = permutations.permute(2,letters)
    perms = list(map(lambda s: 'Z' + s, perms))
    # print("Parsing {} URLs.".format(len(perms)))
 
    tr = Thread(target=write_file) 
    tr.start()

    pool = mp.Pool(mp.cpu_count()-1)

    pool.map(parse_url, [path for path in perms])

    pool.close()
    done = True
    tr.join()


    # print("Done! wrote output to beaves_out.csv")
