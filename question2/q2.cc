#include<iostream>
using namespace std;
#include<limits>
#include<climits>
int main()

{
	cout<< "size of char:"<<sizeof(char)<<"byte"<<endl;
	cout<< "size of bool:"<<sizeof(bool)<<"byte"<<endl;
	cout<< "size of int:"<<sizeof(int)<<"byte"<<endl;
	cout<< "size of float"<<sizeof(float)<<"byte"<<endl;
	cout<< "Minimum value of int:"<<INT_MIN<<endl;
	cout<< "Maximum value of int:"<<INT_MAX<<endl;
	cout<<"The maximum value of float";
	std::cout<<std::numeric_limits<float>::max();
	cout<<endl;
	
        cout<<"The minimum value of float";
        std::cout<<std::numeric_limits<float>::min();
        cout<<endl;
	cout<<"The maximum value of long int";
	std::cout<<std::numeric_limits<long int>::max()<<endl;
	cout<<"The minimum value of long int";
	std::cout<<std::numeric_limits<long int>::min()<<endl;
        



	return 0;
}
