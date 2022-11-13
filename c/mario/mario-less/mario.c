#include <cs50.h>
#include <stdio.h>

void build(int n);

int main(void)
{
    int h; // h is for height

    // Get height
    do
    {
        h = get_int("Height: ");
    }
    while (h < 1 || h > 8);

    // Call build function to build the wall
    build(h);
}

void build(int n)
{
    // For each row
    for (int i = 1; i < (n + 1); i++)
    {
        // For each brick
        for (int j = 1; j < (n + 1); j++)
        {
            if (j <= (n - i))
            {
                //Print blank spaces
                printf(" ");
            }
            else
            {
                // Print the brick
                printf("#");
            }
        }

        // Go to next line
        printf("\n");
    }
}