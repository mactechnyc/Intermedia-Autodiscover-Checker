import os
import sys

def main():
    if len(sys.argv) == 2:
        fileWork(sys.argv[1])
    else:
        nofileWork()

def fileWork(filename):
    with open(filename) as sites:
        for address in sites:
            print("Checking autodiscover address for: {}".format(address[0:-1]))
            output = os.popen("dig +nocmd autodiscover.{} any +multiline +noall +answer;".format(address[0:-1])).read()
            parsedata(output)

def nofileWork():
    answer = raw_input("Enter an address to check or enter Q to quit: ")
    if answer.lower() == "q":
        cont = False
    else:
        cont = True
    while cont == True:
        address = answer
        try:
            output = os.popen("dig +nocmd autodiscover."+address+" any +multiline +noall +answer;").read()
        except(error):
            print("No such address")
        parsedata(output)
        answer = raw_input("Press enter to check an autodiscover address or Q to quit: ")
        if answer == "":
            cont = True
        if answer.lower() == "q":
            cont = False
        else:
            cont = True

def parsedata(output):
    if "CNAME" in output:
        print(output)
        if ".exch025" not in output:
            print("\t!!! This client is using the wrong autodiscover address !!!\n")
        else:
            print("\tTHIS CLIENT HAS THE CORRECT ADDRESS\n")
    else:
        print(output)
        print("\t!!! No CNAME detected. This client is not using intermedia !!!\n")

main()
