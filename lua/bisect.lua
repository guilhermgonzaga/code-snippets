--[[
This uses the bisection method to find a root on the interval specified
optionally in command-line arguments, or in the standard input.
There are two implementations, one recursive and one iterative.
Currently, it only works if there is a single root on the interval.
--]]

-- Example function
function f(x)
	return 5 * x^2 - 20
end

function same_sign(a, b)
	return a * b > 0
end

function bisect(x1, x2)
	local x = (x1 + x2) / 2

	if math.abs(f(x)) <= EPSILON then
		return x
	end

	if same_sign(f(x1), f(x)) then
		return bisect(x, x2)
	else
		return bisect(x1, x)
	end
end

EPSILON = 1e-12

local x1 = arg[1] or io.read('*number')
local x2 = arg[2] or io.read('*number')
local root_rec = not same_sign(f(x1), f(x2)) and bisect(x1, x2)
local root_loop = nil

if not same_sign(f(x1), f(x2)) then
	repeat
		root_loop = (x1 + x2) / 2
		if same_sign(f(x1), f(root_loop)) then
			x1 = root_loop
		else
			x2 = root_loop
		end
	until math.abs(f(root_loop)) <= EPSILON
end

print('Recursion yielded '..(root_rec or 'nothing.'))
print('Loop yielded '..(root_loop or 'nothing.'))
