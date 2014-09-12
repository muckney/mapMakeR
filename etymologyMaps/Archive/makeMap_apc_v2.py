#!/usr/bin/env python
#27/04/2013
#This script takes one argument: the name of a file organized in the following way:
# ara	?	grey
# aze	alman	yellow
# bel	nyametski	blue
# bos	njemacki	blue
# ...
#which is a list of languages, list of words, and corresponding color.
#It will look for the template map 'europe_template.svg' (which you need to have 
#present in the current directory) and replace the names and colors with what it
#reads from the list. The colors can be given as hexadecimal (#ff00cc), but this
#code also understands: green-blue-red-yellow-orange-pink-white-black.

import sys

#outputMap='europe_outputmap.svg' #put here whatever name pleases you
outputMap=sys.argv[1].replace('dictionary','map').replace('.txt','.svg')

#load the .svg map:
theMap = open('europe_template.svg',"r")
theMapSource = theMap.read()

#this is the list of languages and corresponding original colors in the template:
language,color=zip(*
(['abk', '168d4f'],
['ara', 'ffffb1'],
['aze', 'd45500'],
['bel', 'b5ff64'],
['bos', 'abc837'],
['bre', '178df0'],
['bul', '36ae22'],
['cat', '00ffff'],
['cau', 'd38d5f'],
['ces', '00cb60'],
['cor', 'c0003c'],
['cym', 'ff7f29'],
['dan', 'ff5555'],
['deu', 'd09999'],
['ell', 'ffff00'],
['eng', 'ffaaaa'],
['est', 'b7c8be'],
['eus', 'ffd42a'],
['fao', 'ff0000'],
['fin', '6f997a'],
['fra', '53bbb5'],
['fry', 'd66c74'],
['gag', 'c837ab'],
['gla', 'ff7f2a'],
['gle', 'fd6d3c'],
['glg', '00d4aa'],
['hrv', 'abc837'],
['hun', 'ac9d93'],
['hye', '008080'],
['isl', 'f19076'],
['ita', '7bafe0'],
['kat', 'f4e3d7'],
['kaz', 'deaa87'],
['krl', '93ac93'],
['lav', 'de87cd'],
['lit', 'e9afdd'],
['lig', 'f2003c'],
['ltz', '55ddff'],
['mkd', '71c837'],
['mlt', 'a0892c'],
['nap', 'f5003c'],
['nld', 'f4d7d7'],
['nor', 'ff8080'],
['occ', '168d5f'],
['oss', '985fd3'],
['pms', 'f2d53c'],
['pol', '7ecb60'],
['por', '00d4d4'],
['roh', '008079'],
['ron', 'aaccff'],
['rus', '72ff00'],
['sar', 'c0ee3c'],
['sco', '168df0'],
['sic', 'cc003c'],
['slk', '42f460'],
['slv', '81c98d'],
['sme', 'cccccc'],
['spa', 'acd8ed'],
['sqi', 'a0856c'],
['srp', 'abc837'],
['swe', 'ffb380'],
['tat', 'c7a25f'],
['tur', 'cc9e4c'],
['ven', 'f28d3c'],
['xal', 'd34d5f'],
['ukr', 'c1ff00']))

#read the dictionary:
languageDic=[]
wordDic=[]
colorDic=[]
try:
	theDictionary = open(sys.argv[1],"r")
except:
	print 'You need to provide a dictionary.'

for line in theDictionary.readlines():
	languageDic.append( line.split()[0] )
	try:
		wordDic.append( line.split()[1] )
		if wordDic[-1]=='?':
			wordDic[-1]=''
	except:
		wordDic.append( '' )
	try:
		colorDic.append( line.split()[2] )
	except:
		colorDic.append( 'grey' )


#convert the colors in hexadecimal format if the user used english words instead:
## AC: newly defined set of 12 colours from 'grDevices' package in R, terrain.colors() function
for i,col in enumerate(colorDic):
	if col=='g1':
		colorDic[i]='#00A600FF'
	if col=='g2':
		colorDic[i]='#0019FFFF'
	if col=='g3':
		colorDic[i]='#0080FFFF'
	if col=='g4':
		colorDic[i]='#00E5FFFF'
	if col=='g5':
		colorDic[i]='#00FF4DFF'
	if col=='g6':
		colorDic[i]='#1AFF00FF'
	if col=='g7':
		colorDic[i]='#80FF00FF'
	if col=='g8':
		colorDic[i]='#E6FF00FF'
	if col=='g9':
		colorDic[i]='#FFFF00FF'
	if col=='g10':
		colorDic[i]='#FFE53BFF'
	if col=='g11':
		colorDic[i]='#FFDB77FF'
	if col=='g12':
		colorDic[i]='#F2F2F2FF'
## AC: retained from original colour scheme
	if col=='white':
		colorDic[i]='#ffffff'
	if col=='grey':
		colorDic[i]='#999999'



#now we will systematically replace each tag in the .svg ($eng etc)
#with the word given by the user in the dictionary.
#we will also replace the original color with the one requested by the user.
for i,lang in enumerate(languageDic):
	print 'Language:',lang,'- word:',wordDic[i],'- color:',colorDic[i]
	#replace the word:
	theMapSource=theMapSource.replace('$'+lang,wordDic[i])
	#replace the color:
	col=color[ language.index(lang) ]
	theMapSource=theMapSource.replace('#'+col,colorDic[i])



theNewMap = open(outputMap, 'w')
theNewMap.write(theMapSource)
theNewMap.close()
