#include <iostream>
using namespace std;

int main()
{
    int x;
    cout << "Enter an Odd Number :";
    cin >> x;
    int y = (x + 1) / 2;
    for (int i = 1; i <= x; i++)
    {
        for (int j = 1; j <= x; j++)
        {
            if (i == y)
            {
                cout << "* ";
            }
            else
            {
                if (j != y)
                {
                    cout << "  ";
                }
                else
                {
                    cout << "*";
                }
            }
        }
        cout << endl;
    }
}
// https://codeshare.io/7JB6ZY