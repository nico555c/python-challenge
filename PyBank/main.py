#Your task is to create a Python script that analyzes the records to calculate each of the following:

#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The changes in "Profit/Losses" over the entire period, and then the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period

import csv
import os



csv_path = os.path.join("Resources", "budget_data.csv")

# define list and variables
i= 1
total_month = 0
total_amount = 0
list = []
ch_list =[]
change = 0
total_change = 0
max_change = 0
min_change = 0
prev_amount = 0
max_date = ""
min_date = ""


with open(csv_path, encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next (csvreader)

   

#loop through each row in csv file to count the months, calculate total amount and create a list to track changes
    for each_row in csvreader:
        total_month = total_month +1
        amount= int(each_row[1])
        total_amount = total_amount + amount
        change = amount - prev_amount     
        list.append({"Date": each_row[0], "PL": each_row[1], "Change": change})
        prev_amount=amount
        
    
    #create a list of changes:
    for each in list:
        ch_list.append(each["Change"])
        

    #calculate total changes excluding 1st row:
    for i in range(len(ch_list)):
        if i >= 1:
            total_change = total_change + ch_list[i]
    
    
    
    #calculate average of total changes
    avg_change = round(total_change / (total_month-1),2)

    #min/max of changes and their dates
    for each_row in list:
        if min_change > each_row["Change"]:
            min_change = int(each_row["Change"])
            min_date = each_row["Date"]
        else:
            min_change = min_change
            min_date = min_date
    
    for each_row in list:
        if max_change < each_row["Change"]:
            max_change = int(each_row["Change"])
            max_date = each_row["Date"]
        else:
            max_change = max_change
            max_date = max_date


          
        
    print("Financial Analysis")
    print("--------------------------")  
    print(f"Total Months: {str(total_month)}")
    print(f"Total: $ {str(total_amount)}")
    print(f"Average Change: $ {str(avg_change)}")
    print (f"The greatest increase in profits: {str(max_date)} (${str(max_change)})")
    print (f"The greatest increase in profits: {str(min_date)} (${str(min_change)})")


   # print analysis

newfile_path = os.path.join('Analysis','analysis.txt')

with open(newfile_path,'w') as newfile:

    newfile.write("Financial Analysis \n")
    newfile.write("-------------------------- \n")
    newfile.write("Total Months: %s \n" % (total_month))
    newfile.write("Total: $ %s \n" % (total_amount))
    newfile.write("Average Change: $ %s \n" % (avg_change))
    newfile.write(f"The greatest increase in profits: {(max_date)} (${(max_change)}) \n")
    newfile.write(f"The greatest decrease in profits: {(min_date)} (${(min_change)}) \n")








