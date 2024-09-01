// C++ program for
// the above approach
#include <bits/stdc++.h>
using namespace std;


void sub_mat_even(int N)
{
// Counter to initialize
// the values in 2-D array
int K = 1;

// To create a 2-D array
// from to 1 to N*2
int A[N][N];

for(int i = 0; i < N; i++)
{
for(int j = 0; j < N; j++)
{
A[i][j] = K;
K++;
}
}


// If found even we reverse
// the alternate row elements
// to get all diagonal elements
// as all even or all odd
if(N % 2 == 0)
{
for(int i = 0; i < N; i++)
{
if(i % 2 == 1)
{
int s = 0;
int l = N - 1;

// Reverse the row
while(s < l)
{
swap(A[i][s],
A[i][l]);
s++;
l--;
}
}
}
}


// Print the formed array
for(int i = 0; i < N; i++)
{
for(int j = 0; j < N; j++)
{
cout << A[i][j] << " ";
}
cout << endl;
}
}


// Driver code
int main()
{
int N = 4;

// Function call
sub_mat_even(N);
}


// This code is contributed by mishrapriyanshu557