#pragma once

#include "matrix.hpp"
#include <string>
#include <exception>

class FileNotOpenException : public std::exception
{
	public:
		const char* what() const noexcept override
		{
			return "Data.txt not open";
		}
};

struct Data
{
	double B_target;
	double L_target;
	double H_target;
	double distToTarget;
	double psi; // рысканье
	double v; // тангаж
	double gamma; // крен
	double theta_1;
	double theta_2;
};


Data readFile(const std::string& filename);
