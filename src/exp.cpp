#include <iostream>
#include <windows.h>
using namespace std;
int regDm()
{
  // HMODULE hDll = LoadLibrary("c:/test_game/RegDll.dll");
  // if(hDll == NULL)
  // {
  //   int err = GetLastError();
  //   cout<<err<<endl;
  //   return 0;
  //
  // }
  // int (*DllRegisterServer)() = (decltype(DllRegisterServer))GetProcAddress(hDll,"DllRegisterServer");
  // int a = DllRegisterServer();
  // cout<<a<<endl;
  CoInitialize(NULL);
  CLSID clsid;
	CLSIDFromProgID(OLESTR("dm.dmsoft"), &clsid);
	// Idmsoft* dme;
	// CoCreateInstance(clsid, NULL, CLSCTX_INPROC_SERVER,__uuidof(Idmsoft), (LPVOID*)&dme);
}
int main()
{
  regDm();
}
