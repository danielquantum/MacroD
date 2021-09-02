import subprocess

files_list = ['8e_500.xyz', '8e_1000.xyz', '8e_1500.xyz', '8e_2000.xyz', '8e_2500.xyz', '8e_3000.xyz', '8e_3500.xyz', '8e_4000.xyz', '8e_4500.xyz', '8e_5000.xyz']


for item in files_list:
	#input
	file_in = open('8e.g16','r') 
	file_in_lines = file_in.readlines()

	#out
	item2 = item.split('.')           # split string of filename into list, separated by '.'
	item3 = item2[0] + '.g16'         # slicing of first member in the list and join it with '.g16'
	file_out = open(item3, 'w+')      # !!! Change filename

	for line in file_in_lines:
		if 'Here' in line:
			file_in2 = open(item,'r')
			file_in_lines2 = file_in2.readlines()
			for count, line2 in enumerate(file_in_lines2):
				if count == 0 or count == 1:                 # skip the first two lines of XYZ input
					print(line2)
				else:
					file_out.write(line2)
		else:
			file_out.write(line)
	print(item3)
	file_out.close()
	file_in.close()
	file_in2.close()

	### Running Gaussian
	subprocess.run(["grun", item3])                  # running gaussian
