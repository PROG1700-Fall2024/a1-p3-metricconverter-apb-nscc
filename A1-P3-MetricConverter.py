#Program 3 – Imperial to Metric Conversion
#Write a console program that converts a weight given in tons (imperial), stones, pounds, and ounces 
# to the metric equivalent in metric tons, kilograms, and grams.

#Written by Alex Barr W0487099

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #This is the Imperial to Metric Conversion code

    #Display the Program description
    print("Imperial To Metric Conversion\n")

    #Get the user to input the number of tons
    tons = int(input("Enter the number of tons: "))

    #Get the user to input the number of stones
    stone = int(input("Enter the number of stone: "))

    #Get the user to input the number of pounds
    pounds = int(input("Enter the number of pounds: "))

    #get the user to input the number of ounces
    ounces = int(input("Enter the number of ounces: "))

    #Calculate the weight in metric
    total_ounces = 35840 * tons + 224 * stone + 16 * pounds + ounces
    total_kilos = total_ounces/35.274
    metric_tons = int(total_kilos/1000)
    remaining_kilos = int(total_kilos) - (metric_tons * 1000) #Get the int of total kilos and subtract metric tons * 1000 which will result in a number smaller than 100. This is the remaining kilos
    decimal_of_total_kilos_only = total_kilos % 1 #get the decimal values after the decimal point.
    grams = decimal_of_total_kilos_only * 1000 # times the value above by 1000 to make it a whole number that we can adjust in code later in the final print statement.

    ##### OKAY so this must be noted here because I think I did this in a way that wasn't intended but it works (and I'm so excited, I feel like I discovered fire haha)
    #Once I had the total ounces and total kilos that was all I needed. I discovered this when debugging. The float value of total kilos contains all
    #the values I need. After total kilos is calculated I do what is commented above to get the appropriate values out of total kilos. The tons, kilos and grams are all in total_kilos
    #Display the weight in metric
    print("The metric weight is {0} metric tons, {1} kilos, and {2:.1f} grams.".format(metric_tons,remaining_kilos,grams))


    # YOUR CODE ENDS HERE

main()