
#ifndef UTIL_H
#define UTIL_H
#include <assert.h>
#include <stdint.h>
#include <string>

/*----------------------------------[standard]--------------------------------*/
#define TRUE  1
#define FALSE 0
using namespace std;
class Utility
{



    private:
       string m_fileName;
    public:
        Utility();
        Utility(string fileName);
        ~Utility();
        int fileToHex(char* outputStr);
};

#endif // UTIL_H
