import subprocess

files_list = ['8e_500.g16', '8e_1000.g16', '8e_1500.g16', '8e_2000.g16', '8e_2500.g16', '8e_3000.g16', '8e_3500.g16', '8e_4000.g16', '8e_4500.g16', '8e_5000.g16']


for item in files_list:
	#input
	file_in = open(item,'r')
	file_in_lines = file_in.readlines()

	#out
	item2 = item.split('.')
	item3 = item2[0] + '-opt.g16'
	file_out = open(item3, 'w+')      # !!! Change filename

	for line in file_in_lines:
		if 'B3LYP' in line:
			file_out.write('#P M062X/6-31+G(d,p) scf=tight Int=Ultrafine scrf(Solvent=DiMethylSulfoxide) Opt Freq \n')
		else:
			file_out.write(line)
	print(item3)
	file_out.close()
	file_in.close()

	### Running Gaussian
	subprocess.run(["grun", item3])                # running gaussian
	subprocess.run(["rm", item])                   # removing previous file
    