




# \texttt{}

if __name__=="__main__":
	W = 0.02046 # Joules
	dT = 25 # Kelvin
	kap = 1000 # The heat capacity 1000J/(K*kg)
	V = 63*(10**(-6)) # cm**3 volume of the putki
	density_of_air = 1.225 # kg/m**3
	# Now calculate the heat energy from the volume.
	heat_energy = (V*density_of_air)*kap*dT
	print("Here is the calculated heat energy: "+str(heat_energy))
	ratio = W/heat_energy
	print("Here is the ratio: "+str(ratio))
	exit(0)
