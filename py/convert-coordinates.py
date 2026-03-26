"""
This is code to convert from a set of coordinates to another:
- cartesian to spherical
- spherical to cartesian
"""

r"""Paste in mermaid.live:
%% Intuition about coordinate conversion process
flowchart TD
    A([$$\lparen\rho,\phi,\theta\rparen;\;\dim=3$$])
    B([$$z\in R;\;\dim=1$$])
    C([$$\lparen r,\theta\rparen;\;\dim=2$$])
    D([$$x\in R;\;\dim=1$$])
    E([$$y\in R;\;\dim=1$$])

    A -.->|$$z=\rho\,\cos\phi$$| B
    A -.->|$$r=\rho\,\sin\phi$$| C
    C -.->|$$x=r\,\cos\theta$$| D
    C -.->|$$y=r\,\sin\theta$$| E
"""

from random import random, uniform
from math import pi, tau, sin, cos, atan2, sqrt, isclose

def point_repr(point):
	return (f'{coord:7.2f}' for coord in point)

def cart2sphr(x, y, z):
	r = sqrt(x**2 + y**2)
	rho = sqrt(r**2 + z**2)
	theta = atan2(y, x) + tau * (y < 0)
	phi = atan2(r, z)
	return rho, theta, phi

def sphr2cart(rho, theta, phi):
	r = rho * sin(phi)
	z = rho * cos(phi)
	y = r * sin(theta)
	x = r * cos(theta)
	return x, y, z

def new_point_cart():  # Return (x, y, z)
	return uniform(-999, 999), uniform(-999, 999), uniform(-999, 999)

def new_point_sphr():  # Return (rho, theta, phi)
	return 999 * random(), tau * random(), pi * random()

def points_equal(p, q):
	return all(isclose(pi, qi, rel_tol=1e-08) for pi, qi, in zip(p, q))

def test():
	for _ in range(1_000_000):
		point_cartesian = new_point_cart()
		point_cartesian2 = sphr2cart(*cart2sphr(*point_cartesian))
		assert points_equal(point_cartesian, point_cartesian2), f'\n{point_cartesian}\n{point_cartesian2}'

		point_spherical = new_point_sphr()
		point_spherical2 = cart2sphr(*sphr2cart(*point_spherical))
		assert points_equal(point_spherical, point_spherical2), f'\n{point_spherical}\n{point_spherical2}'

	print('Test passed')

if __name__ == '__main__':
	p_cart = new_point_cart()
	p_sphr = cart2sphr(*p_cart)
	q_sphr = new_point_sphr()
	q_cart = sphr2cart(*q_sphr)

	print('Example:')
	print('Cartesian --> Spherical:', *point_repr(p_cart), ' -->', *point_repr(p_sphr))
	print('Spherical --> Cartesian:', *point_repr(q_sphr), ' -->', *point_repr(q_cart))

	test()
