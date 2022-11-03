import csv


#this function creates a new csv file 
def create_new_csv_file(filename, fieldnames):    
    with open(filename, mode="w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

    
#This function writes to our csv file
def write_to_csv_file(filename, data):
    with open(filename, mode="a") as csv_file:
        writer = csv.writer(csv_file,  delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(data)