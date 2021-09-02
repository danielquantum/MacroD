#----------------------------
#NMR Chemical Shitfs
# CHCl3
#	   NH(I)  NH(II)  NH(III)
# 8a:	59	    60	    61		MC, QM
#  		55		22	 	18		MD, QM
#
# 8b: 	60      61     	62		MC, QM
#		55		22	   	18		MD, QM		
#
# 8c:	57 		58		59		MC, QM
#		55		22		18		MD, QM
#
# 8d: 	55		56		57		MC, QM
#		55		22		18		MD, QM
#
# DMSO
# 8a:	59		60		61		MC, QM
#		55		22		18		MD, QM
#
# 8b: 	60		61 		62		MC, QM
#		55		22		18		MD, QM
#
# 8c: 	57		58		59		MC, QM
#		55		22		18		MD, QM
#
# 8d:	55		56		57		MC, QM
#		55		22		18		MD, QM
#
# 8e: 	54		55		56		MC, QM
#		55		22		18		MD, QM
#
#----------------------------
import math

ip1 = '55'
ip2 = '22'
ip3 = '18'
ref = 31.8821
#CHCl3
#T8n = 'Exp.,6.22,6.28,5.10' #8a 
#T8n = 'Exp.,5.64,6.27,5.03' #8b
#T8n = 'Exp.,4.88,6.28,5.05' #8c
#T8n = 'Exp.,8.15,6.43,5.06' #8d
#T8n = 'Exp.,5.91,6.89,4.96' #8e
#DMSO
#T8n = 'Exp.,8.50,6.42,7.32' #8a
#T8n = 'Exp.,8.56,6.63,7.32' #8b
#T8n = 'Exp.,8.31,6.63,7.20' #8c
#T8n = 'Exp.,8.32,6.88,7.17' #8d
T8n = 'Exp.,8.79,7.31,7.27' #8e
LT8n = T8n.split(',')

files_list = ['8e_500.g16_14692381.log', '8e_1000.g16_14692382.log', '8e_1500.g16_14692383.log', '8e_2000.g16_14692384.log', '8e_2500.g16_14692385.log', '8e_3000.g16_14692386.log', '8e_3500.g16_14692387.log', '8e_4000.g16_14692388.log', '8e_4500.g16_14692389.log', '8e_5000.g16_14692390.log']

#----------------------------------
#import glob
#----------------------------------
# Creating a list of files (*.log)
#files_list = (glob.glob("*.log"))
#files_list.sort()
#print(files_list)
#----------------------------------

#Searching minimum Energy
Emin = 0.00
for item in files_list:
	#input
	file_in = open(item,'r') 
	file_in_lines = file_in.readlines()

	for line in (file_in_lines):
		if 'SCF Done' in line:
			linesplit = line.split() 		# a list
			Energy = float(linesplit[4]) 
			if Energy < Emin:
				Emin = Energy
#print(Emin)


#Tabulating Data
pList = []
for item in files_list:
	#input
	file_in = open(item,'r') 
	file_in_lines = file_in.readlines()

	#Compound Name
	item2  = item.split('.')
	#item2 = item.split('-')				# MC

	#itemA = item2[1].split('.')
	#itemA = item2[3].split('.')			# MC

	item3 = item2[0] #+ '-' + itemA[0]				
	#item3 = item2[0] + '-' + item2[2] + itemA[0] #MC
	#print(item3)

	#output file .csv
	item4 = item3.split('_')
	#item4 = item3.split('-') 			#MC
	item5 = item4[0]

	# Creating Proton list
	list_of_chemical_shifts = []
	
	for line in (file_in_lines):
		if 'SCF Done' in line:
			linesplit = line.split() 		# a list
			Energy = float(linesplit[4])
			REnergy = (Energy - Emin)*627.509
		if "Isotropic" in line:
			linesplit = line.split() 		# a list
			#print(linesplit)
			if linesplit[0] == ip1:
				#list_of_chemical_shifts.append(item3) 		# MC
				pI = float(linesplit[4])	# NH(I)  order 3
				pI = ref - pI
				list_of_chemical_shifts.append(pI)
				#Differences
				DpI = pI - float(LT8n[1])
				list_of_chemical_shifts.append(DpI)
				DpII = pII - float(LT8n[2])
				list_of_chemical_shifts.append(DpII)
				DpIII = pIII - float(LT8n[3])
				list_of_chemical_shifts.append(DpIII)
				#RMSE
				RMSE = math.sqrt((DpI**2 + DpII**2 + DpIII**2)/3)
				list_of_chemical_shifts.append(RMSE)
				#Energy in Hartree
				list_of_chemical_shifts.append(Energy)
				#Relative Energy
				list_of_chemical_shifts.append(REnergy)


			if linesplit[0] == ip2:
				pII = float(linesplit[4])	# NH(II)  order 2
				pII = ref - pII
				list_of_chemical_shifts.append(pII) 
			if linesplit[0] == ip3:
				list_of_chemical_shifts.append(item3)		# MD
				pIII = float(linesplit[4])	# NH(III) order 1
				pIII = ref - pIII
				list_of_chemical_shifts.append(pIII)
	file_in.close()
	pList.append(list_of_chemical_shifts)
	#print(pList)

# Write to csv
#print('Final pList is: ', pList)
file_out = open(item5+'.csv', 'w+')
file_out.write('Name,NH(I),NH(II),NH(III),D-NH(I),D-NH(II),D-NH(III),RMSE,Energy(H),Rel.Energy\n')
for item in pList:
	#print(item)
	file_out.write(str(item[0]) + ',' + str(item[3]) + ',' + str(item[2]) + ',' + str(item[1]) + ',' + str(item[4]) + ',' + str(item[5]) + ',' + str(item[6]) + ',' + str(item[7]) + ',' + str(item[8]) + ',' + str(item[9]))
	#file_out.write(str(item[0]) + ',' + str(item[1]) + ',' + str(item[2]) + ',' + str(item[3]))			# MC
	file_out.write('\n')
file_out.write(T8n)
file_out.close()

