#!/usr/bin/env python3

# Created by: Izza khalid
# Created on: september 2019
# This program adds two numbers toghether
#   with user input


def main():
    # this function adds two numbers toghether

    # input
    firstnumber = int(input("Enter the first number :"))
    secondnumber = int(input("Enter the second number :"))

    # process
    total = firstnumber+secondnumber

    # output
    print("")
    print("{0} + {1} = {2}".format(firstnumber, secondnumber, total))


if __name__ == "__main__":
    main()
