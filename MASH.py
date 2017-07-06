# *****************************************************************************

	# This program is free software: you can redistribute it and/or modify
	# it under the terms of the GNU General Public License as published by
	# the Free Software Foundation, either version 3 of the License, or
	# (at your option) any later version.

	# This program is distributed in the hope that it will be useful,
	# but WITHOUT ANY WARRANTY; without even the implied warranty of
	# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	# GNU General Public License for more details.

	# You should have received a copy of the GNU General Public License
	# along with this program.  If not, see <http://www.gnu.org/licenses/>.
	
# *****************************************************************************

import random

MASH = open('MASH.txt', 'r')
Gender = random.randrange(1, 3)
print("GENDER")
if Gender == 1:
        print(" Female")
elif Gender == 2:
        print(" Male")
for line in MASH:
	_Options = line.count(';')
	MASH_Prop = line.split(';')
	MASHOpt = random.randrange(1,_Options)
	print(MASH_Prop[MASHOpt])
        
	

	if MASH_Prop[MASHOpt] == "	Asian" and Gender == 1:
		NAMES = open('AsianF.txt', 'r')
		lines = NAMES.readlines()
		SURNAMES = open('SurAsian.txt', 'r')
		lines2 = SURNAMES.readlines()
		NameOpt = random.randrange(0,len(lines))
		SurNameOpt = random.randrange(0,len(lines2))
		print(lines[NameOpt], lines2[SurNameOpt])
	elif MASH_Prop[MASHOpt] == "	Asian" and Gender == 2:
		NAMES = open('AsianM.txt', 'r')
		lines = NAMES.readlines()
		SURNAMES = open('SurAsian.txt', 'r')
		lines2 = SURNAMES.readlines()
		NameOpt = random.randrange(0,len(lines))
		SurNameOpt = random.randrange(0,len(lines2))
		print(lines[NameOpt], lines2[SurNameOpt])
	elif MASH_Prop[MASHOpt] == "	Russian" and Gender == 1:
		NAMES = open('RussianF.txt', 'r')
		lines = NAMES.readlines()
		SURNAMES = open('SurRussian.txt', 'r')
		lines2 = SURNAMES.readlines()
		NameOpt = random.randrange(0,len(lines))
		SurNameOpt = random.randrange(0,len(lines2))
		print(lines[NameOpt], lines2[SurNameOpt])
	elif MASH_Prop[MASHOpt] == "	Russian" and Gender == 2:
		NAMES = open('RussianM.txt', 'r')
		lines = NAMES.readlines()
		SURNAMES = open('SurRussian.txt', 'r')
		lines2 = SURNAMES.readlines()
		NameOpt = random.randrange(0,len(lines))
		SurNameOpt = random.randrange(0,len(lines2))
		print(lines[NameOpt], lines2[SurNameOpt])
	elif MASH_Prop[MASHOpt] == "	English" and Gender == 1:
		NAMES = open('EnglishF.txt', 'r')
		lines = NAMES.readlines()
		SURNAMES = open('SurEnglish.txt', 'r')
		lines2 = SURNAMES.readlines()
		NameOpt = random.randrange(0,len(lines))
		SurNameOpt = random.randrange(0,len(lines2))
		print(lines[NameOpt], lines2[SurNameOpt])
	elif MASH_Prop[MASHOpt] == "	English" and Gender == 2:
		NAMES = open('EnglishM.txt', 'r')
		lines = NAMES.readlines()
		SURNAMES = open('SurEnglish.txt', 'r')
		lines2 = SURNAMES.readlines()
		NameOpt = random.randrange(0,len(lines))
		SurNameOpt = random.randrange(0,len(lines2))
		print(lines[NameOpt], lines2[SurNameOpt])
	elif MASH_Prop[MASHOpt] == "	German" and Gender == 1:
		NAMES = open('GermanF.txt', 'r')
		lines = NAMES.readlines()
		SURNAMES = open('SurGerman.txt', 'r')
		lines2 = SURNAMES.readlines()
		NameOpt = random.randrange(0,len(lines))
		SurNameOpt = random.randrange(0,len(lines2))
		print(lines[NameOpt], lines2[SurNameOpt])
	elif MASH_Prop[MASHOpt] == "	German" and Gender == 2:
		NAMES = open('GermanM.txt', 'r')
		lines = NAMES.readlines()
		SURNAMES = open('SurGerman.txt', 'r')
		lines2 = SURNAMES.readlines()
		NameOpt = random.randrange(0,len(lines))
		SurNameOpt = random.randrange(0,len(lines2))
		print(lines[NameOpt], lines2[SurNameOpt])
	elif MASH_Prop[MASHOpt] == "	Spanish" and Gender == 1:
		NAMES = open('SpanishF.txt', 'r')
		lines = NAMES.readlines()
		SURNAMES = open('SurSpanish.txt', 'r')
		lines2 = SURNAMES.readlines()
		NameOpt = random.randrange(0,len(lines))
		SurNameOpt = random.randrange(0,len(lines2))
		print(lines[NameOpt], lines2[SurNameOpt])
	elif MASH_Prop[MASHOpt] == "	Spanish" and Gender == 2:
		NAMES = open('SpanishM.txt', 'r')
		lines = NAMES.readlines()
		SURNAMES = open('SurSpanish.txt', 'r')
		lines2 = SURNAMES.readlines()
		NameOpt = random.randrange(0,len(lines))
		SurNameOpt = random.randrange(0,len(lines2))
		print(lines[NameOpt], lines2[SurNameOpt])
	elif MASH_Prop[MASHOpt] == "	African" and Gender == 1:
		NAMES = open('AfricanF.txt', 'r')
		lines = NAMES.readlines()
		SURNAMES = open('SurAfrican.txt', 'r')
		lines2 = SURNAMES.readlines()
		NameOpt = random.randrange(0,len(lines))
		SurNameOpt = random.randrange(0,len(lines2))
		print(lines[NameOpt], lines2[SurNameOpt])
	elif MASH_Prop[MASHOpt] == "	African" and Gender == 2:
		NAMES = open('AfricanM.txt', 'r')
		lines = NAMES.readlines()
		SURNAMES = open('SurAfrican.txt', 'r')
		lines2 = SURNAMES.readlines()
		NameOpt = random.randrange(0,len(lines))
		SurNameOpt = random.randrange(0,len(lines2))
		print(lines[NameOpt], lines2[SurNameOpt])
