
# Kriti Shah and Matthew Toro
#hello

def encode(password) #Encoder function, returns encoded password
    z = []
    j = ''
    #Returns j

    for i in range(len(password)):
        z.append(int(password[i]+3)) #Appends encoded character into the list

    for i in z:
        j += str(i) #Changes list into string

    return j #Returns encoded string


def decoder(password):  # Encoder function, adding three
    decoded_password = ''

    for digit in password:  # all the digit in password

        if digit.isdigit():  # if the digits are a digit
            number = int(digit)  # the digit makes it into an integer = number
            decode = number - 3  # make the encode by adding three to the digits
            decoded_password += str(decode)  # turn each decoded digit to a string and add to the new password str

    return decoded_password  # return the new string



if __name__ == '__main__': #Main
    main()


