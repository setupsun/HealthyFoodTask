#include "calc.hpp"
#include "convertCoordinateSystem.hpp"

Matrix calc(Data& data)
{
	Matrix M1(rotationMatrixOpticalStation(data.theta_1, data.theta_2));
	Matrix M2(rotationMatrixConnectedSC(data.psi, data.v, data.gamma));
	Matrix M3(rotationMatrixRelEarth(data.B_target, data.L_target));
	Matrix targetPos;
	Matrix geodeticAircraftPos;
	Matrix aircraftPos;
	Matrix D(3, 1);

	targetPos = blhToxyz(data.B_target, data.L_target, data.H_target);
	D[0][0] = data.distToTarget;
	D = M1 * D;
	D = M2 * D;
	D = M3 * D;
	aircraftPos = targetPos + D;
	geodeticAircraftPos = xyzToblh(aircraftPos[0][0], aircraftPos[1][0], aircraftPos[2][0]);
	return geodeticAircraftPos;
}
