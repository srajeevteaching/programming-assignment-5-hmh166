# Hannah Hodges
# CS151, Dr. Rajeev
# Programming Assignment 5
# 11/20/2021


import math


def file(name):
    try:
        with open(name, "r") as file:
            for line in file:
                main.append(list)
    except:
        print("cannot open file, check file name and try again")


# function to get cash average
def cash_average():
    count = 0
    sum = 0
    if input == "Cash":
        sum += float()
        count += 1
        avg = sum / count
        return cash_average()
    
    
# function to get the average of creditcard charges
def credit_average():
    count = 0
    sum = 0
    if input == "Credit":
        sum += float()
        count += 1
        avg = sum / count
    return credit_average()


# function if user decides to find trips by date
def date(date):
    count = 0
    if date.startswith():
        count += 1
        return count

# distance function
def distance(lat1, lon1, lat2, lon2):
        distance = arccos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2)) * 3,959
        return distance


# main function to run the program
def main():
    file(input("Enter file name: "))
    while True:
        print("Cash for cash payments or card for Credit payments")
        print("Dates for travels at a certain date")
        print("Distance for the travels near a point ")
        option = input("Enter one option")

        if option == "Credit":
            print("avg card payments of the months is : $", credit_average())

        if option == "Cash":
            print("avg cash payments of the months is : $", cash_average())

        if option == "Date":
            date = input("Enter a date: ")
            print("Total travels on this date is: ", date(date))

        if option == "Distance":
            lati = float(input("Latitude: "))
            if lati > 90 or lati < -90:
                print("out of range error")
                continue

            longi = float(input("Longitude: "))
            if longi > 180 or longi < -180:
                print("Range error")
                continue

            try:

                distance = int(input("Distance: "))
            except:
                print("Distance = integer")
                continue
            if distance < 0:
                print("Range error")
                continue

        else:
            break

main()
