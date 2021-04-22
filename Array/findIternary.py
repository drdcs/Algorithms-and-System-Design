"""
"Chennai" -> "Banglore"
"Bombay" -> "Delhi"
"Goa"    -> "Chennai"
"Delhi"  -> "Goa"

Output: 
Bombay->Delhi, Delhi->Goa, Goa->Chennai, Chennai->Banglore,


"""

def findPath(iternary):

	# find the root
	# build a reverse dictionary and validate keys
	
	reverse_itenary = {}
	for key, value in iternary.items():
		reverse_itenary[value] = key
		
	sources = iternary.keys()
	for src in sources:
		if src in reverse_itenary:
			continue
		else:
			result = src
			
	# using the src iterate over the itenary
	
	while result is not None:
		print(result + ":" + str(iternary.get(result, None)))
		result = iternary.get(result, None)
		

	
if __name__ == '__main__':

	path = {
	"Chennai":"Banglore",
	"Bombay":"Delhi",
	"Goa":"Chennai",
	"Delhi":"Goa"
	}
	
	findPath(path)
	
	
