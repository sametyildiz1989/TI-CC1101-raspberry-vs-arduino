#include "Utility.h"
#include <stdio.h>
#include <iostream>
#include <typeinfo>
using namespace std;
//----------------------------[CC1100 reset function]--------------------------

Utility::Utility(){

}

Utility::Utility(string fileName){

      m_fileName = fileName;

}

Utility::~Utility(){

}

int Utility::fileToHex(char* outputStr)
{

  FILE* f = fopen(m_fileName.c_str(), "rb");
  unsigned char c;
  int i=0;
  while(!feof(f)) {
      if(fread(&c, 1, 1, f) == 0) break;
      outputStr[i]=(int)c;
      i++;
  }
  outputStr[i]='\0';
  fclose(f);
  return i;
}
