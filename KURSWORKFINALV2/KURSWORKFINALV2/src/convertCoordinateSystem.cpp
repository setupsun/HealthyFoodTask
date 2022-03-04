#include "convertCoordinateSystem.hpp"
#include "utils.hpp"
#include <cmath>

Matrix blhToxyz(double B, double L, double H)
{
	Matrix coord(3, 1);
	const double a = 6378137.0;
	const double f = 1 / 298.257223563;
	const double e2 = 2 * f - ft_pow2(f);
	const double N = a / sqrt(1 - e2 * ft_pow2(sin(B)));

	coord[0][0] = (N + H) * cos(B) * cos(L);
	coord[1][0] = (N + H) * cos(B) * sin(L);
	coord[2][0] = (N * (1 - e2) + H) * sin(B);
	return coord;
}

Matrix xyzToblh(double x, double y, double z)
{
	Matrix coord(3, 1);
	const double a = 6378137.0;
	const double f = 1 / 298.257223563;
	const double e2 = 2 * f - ft_pow2(f);
	const double b = a * (1 - f);
	const double ep2 = f * (2 - f) / ft_pow2(1 - f);
	const double r2 = ft_pow2(x) + ft_pow2(y);
	const double r = sqrt(r2);
	const double E2 = ft_pow2(a) - ft_pow2(b);
	const double F = 54 * ft_pow2(b) * ft_pow2(z);
	const double G = r2 + (1 - e2) * ft_pow2(z) - e2 * E2;
	const double c = (ft_pow2(e2) * F * r2) / (ft_pow2(G) * G);
	const double s = pow((1 + c + sqrt(ft_pow2(c) + 2 * c)), 1 / 3);
	const double P = F / (3 * ft_pow2(s + 1.0 / s + 1) * ft_pow2(G));
	const double Q = sqrt(1 + 2 * ft_pow2(e2) * P);
	const double ro = -(e2 * P * r) / (1 + Q) + sqrt((a * a / 2)
					* (1 + 1.0 / Q) - ((1 - e2) * P * ft_pow2(z)) / (Q * (1 + Q)) - P * r2 / 2);
	const double tmp = ft_pow2(r - e2 * ro);
	const double U = sqrt(tmp + ft_pow2(z));
	const double V = sqrt(tmp + (1 - e2) * ft_pow2(z));
	const double zo = (ft_pow2(b) * z) / (a * V);

	coord[0][0] = atan((z + ep2 * zo) / r);
	coord[1][0] = atan2(y, x);
	coord[2][0] = U * (1.0 - ft_pow2(b) / (a * V));
	return coord;
}

Matrix rotationMatrixOpticalStation(double theta1, double theta2)
{
	Matrix rot(3, 3);

	rot[0][0] = cos(theta2);
	rot[0][1] = -sin(theta2) * cos(theta1);
	rot[0][2] = sin(theta2) * sin(theta1);

	rot[1][0] = sin(theta2);
	rot[1][1] = cos(theta1) * cos(theta2);
	rot[1][2] = -cos(theta1) * sin(theta2);

	rot[2][0] = 0;
	rot[2][1] = sin(theta1);
	rot[2][2] = cos(theta1);

	return rot;
}

Matrix rotationMatrixConnectedSC(double psi, double v, double gamma)
{
	Matrix rot(3, 3);

	rot[0][0] = cos(psi) * cos(v);
	rot[0][1] = sin(gamma) * sin(psi) - cos(psi) * cos(gamma) * sin(v);
	rot[0][2] = cos(gamma) * sin(psi) + cos(psi) * sin(gamma) * sin(v);

	rot[1][0] = sin(v);
	rot[1][1] = cos(gamma) * cos(v);
	rot[1][2] = -sin(gamma) * cos(v);

	rot[2][0] = -sin(psi) * cos(v);
	rot[2][1] = sin(gamma) * cos(psi) + sin(psi) * sin(v) * cos(gamma);
	rot[2][2] = cos(gamma) * cos(psi) - sin(psi) * sin(v) * sin(gamma);

	return rot;
}

Matrix rotationMatrixRelEarth(double B, double L)
{
	Matrix rot(3, 3);

	rot[0][0] = -cos(L) * sin(L);
	rot[0][1] = cos(L) * cos(B);
	rot[0][2] = -sin(L);

	rot[1][0] = -sin(L) * sin(L);
	rot[1][1] = cos(B) * sin(L);
	rot[1][2] = cos(L);

	rot[2][0] = cos(B) * cos(L);
	rot[2][1] = sin(B);
	rot[2][2] = 0;

	return rot;
}
