#include <cstdlib>
#include <iostream>

#include "example.h"

int main(int argc, char** argv)
{
    projectx::Example example{};
    std::cout << "Example.getValue() => " << example.getValue() << std::endl;

    return EXIT_SUCCESS;
}
