f = open('results')
date = '' # TODO: Might use this in the future but not now
data = {}
for line in f:
	if line.strip() == "***":
		date = f.next()
	else:
		try:
			address = line.strip().split(' ')[4]
		except IndexError:
			# If we got here, we didn't get scan results.  Go back
			# and keep trying until we find some valid results.
			continue
		try:
			ssid = f.next().split('"')[1].strip()
		except IndexError:
			# SSIDs are quoted unless the SSID isn't found, in
			# which case it's the unquoted string "unknown".
			# Since we're string breaking on quotes for simplicity
			# we need to special case in unknown SSIDs.
			ssid = "unknown"
		f.next() # Skip the mode/channel line
		f.next() # Skip the signal/quality line
		encryption = f.next()[22:].strip()
		f.next() # Blank line between cells
		data[address] = {'ssid': ssid, 'encryption': encryption}

for address in data.keys():
	print address.ljust(20), data[address]['ssid'].ljust(34), data[address]['encryption']
