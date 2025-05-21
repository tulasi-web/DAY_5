"""input=Akash Deep
	output=Aka (-)(+)
	output=ash   (+) (-)
	output=Deep   (-)(+)
	output=pe s   (-)(+)
	output=eeD     (-)(+)
	output=peeD hsakA  (-) (+)
	"""
k="Akash Deep"
print("by using (-)(+) slicing ",k[0:3:1],k[-10:-7:1])
print("by using (-)(+) slicing ",k[2:5:1],k[-8:-5:1])
print("by using (-)(+) slicing ",k[6::1],k[-4::1])
print("by using (-)(+) slicing ",k[-1:-8:-2],k[9:2:-2])
print("by using (-)(+) slicing ",k[-2:-5:-1],k[8:5:-1])
print("by using (-)(+) slicing ",k[-1::-1],k[9::-1])