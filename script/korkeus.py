
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
	positions = []
	times = []
	for line in datalines:
		if line[0] not in "01234567890,":
			continue
		#print(line)
		tok = line.split("	")
		t = float(tok[0].replace(",", ".")) # First element is the time
		p = float(tok[2].replace(",", ".")) # Position is the third element 
		times.append(t)
		positions.append(p)
	assert len(times) == len(positions)
	# Now graph.

	plt.figure(figsize=(8, 5))
	# plt.plot(volumes, pressures, marker='o', linestyle='-', color='b', label='PV Curve')
	plt.scatter(times, positions, color='b', label='PV Data', alpha=0.7)
	# Labels and title
	plt.xlabel('Time (s)')
	plt.ylabel('Position (m)')
	plt.title('Time-Position Diagram')
	plt.grid(True)
	plt.legend()

	# Show the plot
	plt.show()
