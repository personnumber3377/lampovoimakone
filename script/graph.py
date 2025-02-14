
import sys
import matplotlib.pyplot as plt
# Time	Pressure	Position	Velocity	Acceleration	Volume

# 8.25*10**(-6) - (-2.4*(10**(-6)))
# abs(0.446 - 1.078)

if __name__=="__main__":
	if len(sys.argv) != 2:
		print("Please pass input filename")
		exit(1)
	fh = open(sys.argv[1], "r")
	datalines = fh.readlines()
	fh.close()
	pressures = []
	volumes = []
	for line in datalines:
		if line[0] not in "01234567890,":
			continue
		#print(line)
		tok = line.split("	")
		p = float(tok[1].replace(",", ".")) # Second element is the pressure
		V = float(tok[-1].replace(",", ".")) # Last element is the volume
		pressures.append(p)
		volumes.append(V)
	print(pressures[1])
	print(volumes[1])
	assert len(pressures) == len(volumes)
	# Now graph.

	plt.figure(figsize=(8, 5))
	# plt.plot(volumes, pressures, marker='o', linestyle='-', color='b', label='PV Curve')
	plt.scatter(volumes, pressures, color='b', label='PV Data', alpha=0.7)
	# Labels and title
	plt.xlabel('Volume (m³)')
	plt.ylabel('Pressure (kPa)')
	plt.title('Pressure-Volume Diagram')
	plt.grid(True)
	plt.legend()

	# Show the plot
	plt.show()
