	
"""	input=Will O’Rourke 
	output=Will (-)
	output=Ill  (-)
	output=our   (-)(+)
	output=ke     (+)
	output='       (-) (+)
	output=Rour     (-)(+)"""
	
	
	
j="Will O’Rourke"
print (j[-13:-9:1])
print("dont have capatal I in given data")
print("by using (-)(+) slicing ", j[-5:-2:1],j[8:11:1])

print("by using (-)(+) slicing ",j[11::1],j[-2::1])
print("by using (-)(+) slicing ",j[-7:-8:-1],j[6:7:1])
print("by using (-)(+) slicing ",j[-6:-2:1],j[7:11:1])