#include <stdio.h>
#include <cs50.h>
#include <math.h>

// MASTERCARD: 16 digits, Start with 51/52/53/54/55
// VISA: 13/16 digits, Start with 4
// AMEX: 15 digits, Start with 34/37

// Luhn's Algorithm:
// 1. Multiply every other digit by 2, starting with the second number to the last
// 2. Add the sum of those digits
// 3. Add the sum of the other digits that were not multiplied
// 4. If the total sum ends with 0, it is valid.


// Gets credit card number and checks whether it's valid
int main(void)
{
    long long credit_card , number ;
    do
    {
        credit_card = get_long("Enter credit card number: ");
    }
    while (credit_card < 0);

    number = credit_card;

    // Calculate total number of digits
    int count = (number == 0) ? 1  : (log10(number) + 1);

    int sum = 0;

    // Reiterate through each pair of digits. First digit adds to sum, second digit * 2 and add sum of digits.
    while (number != 0)
    {
        int d1 = number % 10;
        sum += d1;
        int d2 = 2 * ((number / 10) % 10);
        int r1 = (d2 % 10) + floor((d2 / 10) % 10);
        sum += r1;
        number /= 100;
    }

    string card;
    // Identify which card type
    int test = credit_card / pow(10, count - 2);
    if ((count == 13 || count == 16) && test / 10 == 4)
    {
        card = "VISA";
    }
    else if (count == 16  && test >= 51 && test <= 55)
    {
        card = "MASTERCARD";
    }
    else if (count == 15 && (test == 34 || test == 37))
    {
        card = "AMEX";
    }
    else
    {
        card = "INVALID";
    }

    // Final verification
    if (sum % 10 == 0)
    {
        printf("%s\n", card);
    }
    else
    {
        printf("INVALID\n");
    }

}