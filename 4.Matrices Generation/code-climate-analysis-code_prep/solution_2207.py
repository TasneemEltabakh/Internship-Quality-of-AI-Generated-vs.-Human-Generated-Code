// C++ implementation to Count the
// number of groups having the largest
// size where groups are according
// to the sum of its digits
#include <bits/stdc++.h>
using namespace std;


// function to return sum of digits of i
int sumDigits(int n){
int sum = 0;
while(n)
{
sum += n%10;
n /= 10;
}


return sum;
}


// Create the dictionary of unique sum
map<int,int> constDict(int n){

// dictionary that contain
// unique sum count
map<int,int> d;


for(int i = 1; i < n + 1; ++i){
// calculate the sum of its digits
int sum1 = sumDigits(i);


if(d.find(sum1) == d.end())
d[sum1] = 1;
else
d[sum1] += 1;
}


return d;
}


// function to find the
// largest size of group
int countLargest(int n){

map<int,int> d = constDict(n);

int size = 0;


// count of largest size group
int count = 0;


for(auto it = d.begin(); it != d.end(); ++it){
int k = it->first;
int val = it->second;


if(val > size){
size = val;
count = 1;
}
else if(val == size)
count += 1;
}


return count;
}

// Driver code
int main()
{
int n = 13;


int group = countLargest(n);


cout << group << endl;


return 0;
}