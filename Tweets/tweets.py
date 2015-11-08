keywordsfile = open(input('What is the file with the keywords? '), "r")
tweetsfile = open(input('What is the file with the tweets? '), "r")
# make sure the files exist

# {region: [tweets], total tweet scores, num of keywords, region score, num of tweets}
happiness = {'eastern': [[], 0, 0, 0], 'central': [[], 0, 0, 0], 'mountain': [[], 0, 0, 0], 'pacific': [[], 0, 0, 0]}

keywords = {}

# extract the keywords and values from the keywords file
for line in keywordsfile:
	i = 0
	word = ''
	while line[i] != ",":
		word = word + line[i]
		i += 1
	if line[i+2] == "\n":
		number = int(line[i+1])
	else: 
		number = 10
	keywords[word] = number 
# print(keywords)

for line in tweetsfile: 
	lst = line.split(' ', 6)
	lat = lst[0].lstrip('[')
	lat = lst[0].rstrip(',') 
	long = lst[1].rstrip(']')
	
	# ignore the regions that are not in America
	if lat > 49.189787 or lat < 24.660845: 
		continue
	if long > -67.444574 or long < -125.242264:
		continue
		
	# determine what region the tweet is in
	if long < -115.236428: 
		region = 'pacific'
		happiness['pacific'][3] += 1
	elif long < -101.998892:
		region = 'mountain'
		happiness['mountain'][3] += 1
	elif long < -87.518395:
		region = 'central'
		happiness['central'][3] += 1
	else:
		region = 'eastern'
		happiness['eastern'][3] += 1
		
	tweet = lst[5].replace(' ', ', ')
	
	# add tweet in the correct region
	happiness[region][0].append(tweet)
	
	''' 
	possibly unnecessary 
	n = 1
	while line[n] != ',':
		lat = lat + lat[n]
		n += 1
	n += 2
	while line[n] != ']':
		long = long + long[n]
		n += 1
	'''	

# constants 

def timezone(lat, long): 
	# determine timezone
	pass
	
def happy_score():
	numKeywords = 0
	# eastern score
	for i in happiness['eastern'][0]:
		if i in keywords: 
			total = total + keywords[i]
			numKeywords += 1
	happiness['eastern'][1] = total
	happiness['eastern'][2] = total / numKeywords
	
	numKeywords = 0
	# central score
	for i in happiness['central'][0]:
		if i in keywords: 
			total = total + keywords[i]
			numKeywords += 1
	happiness['central'][1] = total
	happiness['central'][2] = total / numKeywords
	
	numKeywords = 0
	# mountain score		
	for i in happiness['mountain'][0]:
		if i in keywords: 
			total = total + keywords[i]
			numKeywords += 1
	happiness['mountain'][1] = total
	happiness['mountain'][2] = total / numKeywords
	
	numKeywords = 0
	# pacific score	
	for i in happiness['pacific'][0]:
		if i in keywords: 
			total = total + keywords[i]
			numKeywords += 1
	happiness['pacific'][1] = total
	happiness['pacific'][2] = total / numKeywords
		
	# search for the keywords
	# score = total of the keywords' happiness value / number of keywords found
	# if no keywords, ignored
	# happiness of region = total for all tweets / number of tweets 

def main(): 
	happy_score()
	print('Eastern: \n num of tweets: ' +  happiness['eastern'][3] + 'happiness score: ' + happiness['eastern'][2]) 
	print('Central: \n num of tweets: ' +  happiness['central'][3] + 'happiness score: ' + happiness['central'][2]) 
	print('Mountain: \n num of tweets: ' +  happiness['mountain'][3] + 'happiness score: ' + happiness['mountain'][2]) 
	print('Pacific: \n num of tweets: ' +  happiness['pacific'][3] + 'happiness score: ' + happiness['pacific'][2]) 



