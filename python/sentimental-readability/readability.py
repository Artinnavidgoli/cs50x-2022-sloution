# I'm using the input metode but you can use "from cs50 import get_string"

while True:
    str = input('Text: ')  # for that metode you need to say here (get_string('text: '))
    index = 0
    i = 0
    alphabets = 0
    digits = 0
    special = 0
    words = 1
    sentences = 0
    if (str):
        for i in range(len(str)):  # cheking the input for alphabets , digits , ... .
            if (str[i].isalpha()):
                alphabets += 1
            elif (str[i].isnumeric()):
                digits += 1
            elif (str[i] == ' ' and str[i + 1]):
                words += 1
            elif (str[i] == '?' or str[i] == '!' or str[i] == '.'):
                sentences += 1
            else:
                special += 1
        # Get L - the average number of letters per 100 words in the text
        L = float(alphabets / words * 100)

        # Get S - the average number of sentences per 100 words in the text
        S = float(sentences / words * 100)

        # calculating the output (index)  (Coleman-Liau algoritem)
        index = round((float)(0.0588 * L - 0.296 * S - 15.8))

        # Output
        if (index >= 16):  # printing the grade upper than 16
            print('Grade 16+')
        elif (index < 1):  # printing the grade lower than 1
            print('Before Grade 1')
        else:
            print('Grade ', index)

        break