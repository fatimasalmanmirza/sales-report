"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""

# salespeople = []  #creating an empty list of names of salespeople
# melons_sold = []  #empty list of melons quantity

# f = open("sales-report.txt") #opening the file with text
# for line in f: #looping through each line in text
#     line = line.rstrip() #removing the spaces
#     entries = line.split("|") #spliting the lines into enteries
#     salesperson = entries[0]   #entry at index 0 would be the name of salesperson
#     melons = int(entries[2]) #for getting the quantities it took enteries @ index 2

#     if salesperson in salespeople:
#         position = salespeople.index(salesperson)
#         melons_sold[position] += melons
#     else:
#         salespeople.append(salesperson) #if sslesperson not in list then appending it to list
#         melons_sold.append(melons) #append quantities to the melons sold list


# for i in range(len(salespeople)):
#     print("{} sold {} melons".format(salespeople[i], melons_sold[i]))

def selling_melons(file):
    melons_dict = {}
    open_file = open(file)
    for line in open_file:
        line =line.rstrip()
        words = line.split("|")
        for word in words:
            names = words[0]
            melons_sold = words[2]
            melons_dict[names] = melons_sold
          
            
            if melons_dict[names] in melons_dict:
                melons_sold[names] = melons_sold[names] + melons_sold
            else:
                melons_dict["names"] = melons_sold 
    # print(melons_dict)
    for keys,values in melons_dict.items():
                    
        print("{} sold {} melons".format(keys,values))
    #     key_names = words[index]   
    #     values_quantity = words[index +1]
    # melons_dict["key_names"] = melons_dict[values_quantity] 
    # print(melons_dict)  
selling_melons("sales-report.txt") 


