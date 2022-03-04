#pragma once

double ft_pow2(const double a);
bool isEqual(const double a, const double b, const double precision = 0.0001);

double degToRad(double angle);
double radToDeg(double angle);

const double alpha = 1 / 298.257223563;
const double e2 = 2 * alpha - alpha * alpha;
const double a = 6378137; // a – большая полуось эллипсоида
