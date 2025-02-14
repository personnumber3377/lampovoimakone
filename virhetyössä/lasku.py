

if __name__=="__main__":
	# Here we use the equation dW = g*delta_h*dm + m*g*d_delta_h
	g = 9.81 # Gravitational accel m/s**2
	delta_h = 0.010 - (- 0.003) # Difference in meters
	dm = 0.03*10**(-3) #  0.03 grams = 0.00003 kg
	d_delta_h = 1*10**(-3) # 1mm to meters
	m = 50*10**(-3) # 50g = 0.05kg
	dW = g*delta_h*dm + m*g*d_delta_h
	print("Value for dW (virhe): "+str(dW))
	exit(0)