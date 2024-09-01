// C++ Program to design the
// above pattern of K using alphabets
#include<bits/stdc++.h>
using namespace std;


// Function to print
// the above Pattern
void display(int n)
{
int v = n;


// This loop is used
// for rows and prints
// the alphabets in
// decreasing order
while (v >= 0)
{
int c = 65;


// This loop is used
// for columns
for(int j = 0; j < v + 1; j++)
{
// chr() function converts the
// number to alphabet
cout << char(c + j) << " ";
}


v--;
cout << endl;
}


// This loop is again used
// to rows and prints the
// half remaining pattern in
// increasing order
for(int i = 0; i < n + 1; i++)
{
int c = 65;


for(int j = 0; j < i + 1; j++)
{
cout << char(c + j) << " ";
}
cout << endl;
}
}


// Driver code
int main()
{
int n = 5;
display(n);
return 0;
}


// This code is contributed by divyeshrabadiya07