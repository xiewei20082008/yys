#include <iostream>
#include <windows.h>
using namespace std;

int main()
{

  HMODULE hModule = GetModuleHandle("kernel32.dll");
  cout<<hModule<<endl;
}
