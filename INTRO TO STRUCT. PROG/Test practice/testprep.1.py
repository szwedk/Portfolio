while True:
    tempF = float(input("Enter Fahenheit: "))
    tempC = 5.00/2.0 * (tempF - 32)
    print("temp in celcius is", tempC)
    print("Temp in F is", tempF)
    ans = input("Do Again? (Y/N): ")
    if not(ans == 'F') or not(ans == 'f'):
        break

print ("end of job")
