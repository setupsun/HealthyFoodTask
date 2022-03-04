#include "utils.hpp"
#include <iostream>
#include "calc.hpp"
#include "readFile.hpp"

int main()
{
	Data data;
	Matrix aircraftCoord_geo;
	
	try
	{
		data = readFile("data.txt");
		aircraftCoord_geo = calc(data);

		std::cout << "B: " << radToDeg(aircraftCoord_geo[0][0]) << std::endl
			<< "L: " << radToDeg(aircraftCoord_geo[1][0]) << std::endl
			<< "H: " << aircraftCoord_geo[2][0] << std::endl;
	}
	catch(const std::exception& e)
	{
		std::cerr << e.what() << '\n';
	}
	return 0;
}
