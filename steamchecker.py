import requests
from bs4 import BeautifulSoup


def main():

    # init headers
    headers = {'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'GET', 'Access-Control-Allow-Headers': 'Content-Type', 'Access-Control-Max-Age': '3600', 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

    url = "https://steamcommunity.com/id/"

    # open config.txt and find input file and output file
    config = open("config.txt", "r")
    inputfile = str(config.readline())
    outputfile = str(config.readline())
    config.close()

    # remove \n in the strings if present
    inputfile = inputfile.replace("\n", "")
    outputfile = outputfile.replace("\n", "")

    # add .txt to the end of filenames if not present
    if (".txt" not in inputfile):
        inputfile += ".txt"

    if (".txt" not in outputfile):
        outputfile += ".txt"

    # open the input file to read from, open output file to write to
    f = open(inputfile, "r")
    p = open(outputfile, "w")
    for x in f:
        # replace \n in line read
        x = x.replace("\n", "")
        
        if len(x) <= 2 or x == "":
            continue
        
        newurl = url + x
        req = requests.get(newurl, headers)
        soup = BeautifulSoup(req.content, 'html.parser')
        
        # if string is found in page, print as available and write to file
        if(soup.body.findAll(text="The specified profile could not be found.") != []):
            print("/id/" + x + " is available!")
            p.write(x + "\n")

    # close both files
    f.close()
    p.close()

if __name__ == "__main__":
    main()
