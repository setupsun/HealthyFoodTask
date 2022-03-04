#include <sstream>
#include <fstream>
#include "utils.hpp"
#include "readFile.hpp"
#include <iostream>

// #define DEBUG

static void convertDataToRad(Data& data)
{
	data.theta_1 = degToRad(data.theta_1);
	data.theta_2 = degToRad(data.theta_2);
	data.B_target = degToRad(data.B_target);
	data.L_target = degToRad(data.L_target);
	data.psi = degToRad(data.psi);
	data.v = degToRad(data.v);
	data.gamma = degToRad(data.gamma);
}

Data readFile(const std::string& filename)
{
	Data data;
	std::string buf;
	std::ifstream f(filename);

	if (!f.is_open())
		throw FileNotOpenException();

	// skip header
	std::getline(f, buf);
	// ---end----

	std::getline(f, buf);
	std::istringstream iss(buf);

	iss >> data.B_target;
	iss >> data.L_target;
	iss >> data.H_target;
	iss >> data.distToTarget;
	iss >> data.psi;
	iss >> data.v;
	iss >> data.gamma;
	iss >> data.theta_1;
	iss >> data.theta_2;
	convertDataToRad(data);
	#ifdef DEBUG
		std::cout << "-----------------init--------------------------" << std::endl;
		std::cout << data.B_target << std::endl
			<< data.L_target << std::endl
			<< data.H_target << std::endl
			<< data.distToTarget << std::endl
			<< data.psi << std::endl
			<< data.v << std::endl
			<< data.gamma << std::endl
			<< data.theta_1 << std::endl
			<< data.theta_2 << std::endl;
		std::cout << "-----------------end init--------------------------" << std::endl;
	#endif
	return data;
}
