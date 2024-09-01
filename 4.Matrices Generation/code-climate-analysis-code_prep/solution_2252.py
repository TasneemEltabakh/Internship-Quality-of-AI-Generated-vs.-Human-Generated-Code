// C++ program to print the pattern
// hollow square with plus inside it
// window pattern
#include <bits/stdc++.h>
using namespace std;

// Function to print pattern n means
// number of rows which we want
void window_pattern (int n)
{
int c, d;

// If n is odd then we will have
// only one middle element
if (n % 2 != 0)
{
c = (n / 2) + 1;
d = 0;
}

// If n is even then we will have two
// values
else
{
c = (n / 2) + 1;
d = n / 2 ;
}

for(int i = 1; i <= n; i++)
{
for(int j = 1; j <= n; j++)
{

// If i,j equals to corner row or
// column then "*"
if (i == 1 || j == 1 ||
i == n || j == n)
cout << "* ";

else
{

// If i,j equals to the middle
// row or column then "*"
if (i == c || j == c)
cout << "* ";

else if (i == d || j == d)
cout << "* ";

else
cout << " ";
}
}
cout << '\n';
}
}

// Driver Code
int main()
{
int n = 7;

window_pattern(n);
return 0;
}

// This code is contributed by himanshu77