import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
from datetime import date
from pathlib import Path
from os.path import exists
import os

class Expense():

    def __init__(self, expense_input):
        self.expense_input = expense_input
        self.substring = ","
        self.count_list = None
        self.total = 0
    
    # Returns a list of all the types and prices
    def from_string(self):
        total_price = []
        type_list = []
        price_list = []
        sub = ":"
        i=0
        month_expense = []
        while self.substring in self.expense_input:
            index = self.expense_input.index(self.substring)
            single_expense = (self.expense_input[:index])
            month_expense.append(single_expense)
            self.expense_input = self.expense_input[index+1:]
        for i in range(len(month_expense)):
            if month_expense[i].find(sub):
                part = month_expense[i].split(sub)
                type = part[0]
                price = part[1]
                price_number = price.replace("$", "")          
                # total_price.append(price_number)
                type_list.append(type)
                price_list.append(price)
                i+=1
        return {"type_list": type_list, "price_list": price_list}
    
    # Gets the element of every expense of the month
    def count(self):
        self.count_list = self.expense_input.split(self.substring)
        return self.count_list
    
    # Gets the total of the expense of the month
    def total_amount(self):
        sign = '$'
        total_list = self.from_string()["price_list"]
        for i in range(len(total_list)):
            price_number = total_list[i].replace('$', '')
            self.total = self.total + float(price_number) 
        return self.total

expenses = input("Enter expenses here: ")

exp_1 = Expense(expenses)
print(f"count: {exp_1.count()}")
# print(f"from string: {exp_1.from_string()}")
print(f"total: {exp_1.total_amount()}$")

