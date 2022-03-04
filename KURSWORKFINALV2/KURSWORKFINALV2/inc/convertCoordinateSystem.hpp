#pragma once

#include "matrix.hpp"

Matrix blhToxyz(double B, double L, double H);
Matrix xyzToblh(double x, double y, double z);
Matrix rotationMatrixOpticalStation(double theta1, double theta2);
Matrix rotationMatrixConnectedSC(double psi, double v, double gamma);
Matrix rotationMatrixRelEarth(double B, double L);
