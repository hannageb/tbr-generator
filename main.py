import csv
import random

def randomgeneration(books: [], count: int):
    if len(books) < count:
        print(f"Please enter at least {count} books. ")
        return
    randomTBR = random.sample(books, count)
    print(f"You should read: {randomTBR}")

# introductory statements
print("Hello! Welcome to the random TBR generator! TBR stands for 'to be read',")
print("This program will randomly select books from your TBR.")
print("If you have a Goodreads account, you can upload the filepath to your exported tbr")
count = int(input("To start, how many books would you like to generate? "))
goodreads = input("Do you have a Goodreads account? ")
books = []

if goodreads.lower() == 'yes':
    file = input("Please insert the filepath to exported Goodreads shelf as a .csv file. ")
    # from https://www.geeksforgeeks.org/python/how-to-read-from-a-file-in-python/#reading-csv-files-in-python
    with open(file, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if (row[18] == 'to-read' and row[1]):
                books.append(row[1])
        randomgeneration(books, count)

if goodreads.lower() == 'no':
    manual_input = print(f"Please manually input your TBR? Once done, type ! to generate your next {count} reads.\n")
    title = input("Title: ")
    while title != "!":
        books.append(title)
        title = input("Title: ")
    randomgeneration(books, count)