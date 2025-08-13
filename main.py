import csv
import random

def randomgeneration(books: [], count: int):
    if len(books) < count:
        print(f"Please enter at least {count} books. ")
        return
    randomTBR = random.sample(books, count)
    print(f"You should read: {randomTBR}")
    regen = input("Would you like to generate another 2 books? ")
    if regen.lower().strip() == "yes":
        randomgeneration(books, count)
    elif regen.lower().strip() == "no":
        print("Have a nice day!")
        quit

# introductory statements
print("Hello! Welcome to the random TBR generator! TBR stands for 'to be read',")
print("This program will randomly select books from your TBR.")
print("If you have a Goodreads or StoryGraph account, you can upload the filepath to your exported tbr")
count = int(input("To start, how many books would you like to generate? "))
goodreads = input("Do you have a Goodreads or StoryGraph account? ")
books = []

if goodreads.lower() == 'yes':
    file = input("Please insert the filepath to your exported shelf as a .csv file. ")
    # from https://www.geeksforgeeks.org/python/how-to-read-from-a-file-in-python/#reading-csv-files-in-python
    with open(file, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            if 'Read Status' in row:
                if (row['Read Status'] == 'to-read' and row["Title"]):
                    books.append(row["Title"])
            elif 'Exclusive Shelf' in row:
                if (row["Exclusive Shelf"] == 'to-read' and row["Title"]):
                    books.append(row["Title"])
        randomgeneration(books, count)

if goodreads.lower() == 'no':
    manual_input = print(f"Please manually input your TBR? Once done, type ! to generate your next {count} reads.\n")
    title = input("Title: ")
    while title != "!":
        books.append(title)
        title = input("Title: ")
    randomgeneration(books, count)
