#include "utils.hpp"
#include <cmath>
#include <corecrt_math_defines.h>

double ft_pow2(const double a)
{
	return (a * a);
}

double degToRad(double angle)
{
	return angle * M_PI / 180;
}

double radToDeg(double angle)
{
	return angle * 180 / M_PI;
}
