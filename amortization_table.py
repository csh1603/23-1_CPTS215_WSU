##############################################
# Title: Participation Activity - Sequence Data Types
# Author: Seunghyun Cho
# Version: 3.10.6
# Date: Jan 27th, 2023
#
# Description: This program derives a loan payment schedule numerically.
##############################################
import csv
import pandas as pd

class Loan:
    # includes P, R, N variables
    # includes regular_schedule, accelerated_schedule functions

    # initialization functions when the class is made
    def __init__(self, P, R, N):
        # P is for original principal amount on the laon
        self.P = P
        # R is for monthly interest rate of the loan
        self.R = R
        # N is for the number of total months on the loan
        self.N = N

    def regular_schedule(self):
        # this function makes the list of tuples that contains all information
        # list for containing tuples
        reg_list = list()
        # monthly payments
        mpymt = (self.R * self.P) / (1 - pow(1+self.R, -self.N))
        # the head part of excel file
        str = ("Month\tStarting_Balance\tMonthly_Payment\tPrincipal_Payment\tInterest_Payment\tEnding_Balance")
        # split str by tab
        sch_tuple = str.split("\t")
        # appending tuple into reg_ist
        reg_list.append(sch_tuple)
        # calculate remaining principal payment (p), interest payment(i), ending balance(self.P)
        for j in range(self.N):
            start_P = self.P
            i = self.R * self.P
            p = mpymt - i
            self.P = self.P - p
            if self.P <= 0:
                self.P = 0
            # make new tuple, sch_tuple that contains all the information calculated above
            data = ("{0}\t ${1:.2f}\t ${2:.2f}\t ${3:.2f}\t ${4:.2f}\t ${5:.2f}".format(j, start_P, mpymt, p, i, self.P))
            j += 1
            sch_tuple = data.split("\t ")
            reg_list.append(sch_tuple)
        return reg_list

    def accelerated_schedule(self, amount):
        # this function makes the list of tuples that contains all information
        # list for containing tuples
        acc_list = list()
        # monthly payments, pay more amount of money that user entered
        mpymt = (self.R * self.P) / (1 - pow(1+self.R, -self.N)) + amount
        # the head part of excel file
        head = ("Month\tStarting_Balance\tMonthly_Payment\tPrincipal_Payment\tInterest_Payment\tEnding_Balance")
        # split str by tab
        sch_tuple = head.split("\t")
        # appending tuple into acc_ist
        acc_list.append(sch_tuple)
        j = 1
        # continue until there is no payment left
        while(True):
            start_P = self.P
            i = self.R * self.P
            p = mpymt - i
            self.P = self.P - p
            # make new tuple, sch_tuple that contains all the information calculated above
            data = ("{0}\t ${1:.2f}\t ${2:.2f}\t ${3:.2f}\t ${4:.2f}\t ${5:.2f}".format(j, start_P, mpymt, p, i, self.P))
            j += 1
            sch_tuple = data.split("\t ")
            acc_list.append(sch_tuple)
            if self.P <= 0:
                return acc_list
        return acc_list

def main():
    # get information from the user
    loan_for = input("What is this loan for? ")
    loan_P = float(input("Please enter the principal amount for the loan: "))
    loan_R = float(input("Please enter the yearly interest rate (as a percent) for the loan: "))
    loan_N = int(input("Please enter the number of years for the loan: "))
    loan_A = int(input("Additional monthly amount towards accelerated payment: "))

    # calculate the variables and make loan class
    loan = Loan(loan_P, loan_R/1200, loan_N * 12)
    reg = loan.regular_schedule()
    with open('regular_schedule.csv', 'w', newline = '') as f:
        writer = csv.writer(f)
        writer.writerows(reg)

    loan = Loan(loan_P, loan_R/1200, loan_N * 12)
    acc = loan.accelerated_schedule(loan_A)
    with open('accelerated_schedule.csv', 'w', newline = '') as f:
        writer = csv.writer(f)
        writer.writerows(acc)

if __name__ == "__main__":
    main()