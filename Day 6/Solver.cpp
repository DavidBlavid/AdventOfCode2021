#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <regex>

int main()
{
    std::ifstream myfile ("dummy.txt"); 
    std::string mystring;

    if ( myfile.is_open() ) { 

        myfile >> mystring;

    }

    mystring.erase (std::remove(mystring.begin(), mystring.end(), ','), mystring.end());

    std::cout << mystring << std::endl;

    char n_char;
    char n_char_dec;

    for (size_t i = 0; i < 256; i++){

        for (size_t n = '0'; n < '9'; n++){

            std::replace(mystring.begin(), mystring.end(), n, n-1);

        }

        mystring = std::regex_replace(mystring, std::regex("\\/"), "68"); 

        std::cout << std::to_string(i) << std::endl;

    }

    

    std::cout << mystring.length() << std::endl;
}