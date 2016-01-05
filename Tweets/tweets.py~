##########################################################################################
# Name: Shi Lin (Joanna) Chen    
# This program computes the happiness score of different regions of America. The program 
# intakes a file of tweets and a file of keywords with their respective happiness scores.
# It then computes the total number of tweets in each region and its happiness score.
##########################################################################################

import happy_histogram 

keywordsfile = None
tweetsfile = None

# make sure the files exist
while keywordsfile == None:
	try:
		keywordsfile = open(input('What is the file with the keywords? '), "r")
	except IOError as err:
		print(err)
		
while tweetsfile == None:
	try:
		tweetsfile = open(input('What is the file with the tweets? '), "r")
	except IOError as err:
		print(err)

# {region: [tweets], num of valid tweets, num of keywords, region score, num of tweets}
happiness = {'eastern': [[], 0, 0, 0], 'central': [[], 0, 0, 0], 'mountain': [[], 0, 0, 0], 'pacific': [[], 0, 0, 0]}
regionList = ['eastern', 'central', 'mountain', 'pacific']

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

# extract the words from the tweets file
for line in tweetsfile: 
	lst = line.split()
	lat = lst[0].strip('[')
	lat = float(lat.rstrip(','))
	long = float(lst[1].rstrip(']'))
	
	# ignore the regions that are not in America
	if lat > 49.189787 or lat < 24.660845: 
		continue
	if long > -67.444574 or long < -125.242264:
		continue
	
	# determine what region the tweet is in
	if long <= -115.236428: 
		region = 'pacific'
		happiness['pacific'][3] += 1
	elif long <= -101.998892:
		region = 'mountain'
		happiness['mountain'][3] += 1
	elif long <= -87.518395:
		region = 'central'
		happiness['central'][3] += 1
	elif long <= -67.444574:
		region = 'eastern'
		happiness['eastern'][3] += 1
	
	# remove parts of the line that are not the tweet or unnecessary punctuation
	line = line.replace(', ', '', 4) 
	line = line.replace('.', '', 2)
	line = line.replace('.', ' ')
	line = line.replace(', ', ' ')
	lst = line.split()
	lst = lst[4:]
	
	happiness[region][0].append(lst)
	
# search for the keywords
# score = total of the keywords' happiness value / number of keywords found
# if no keywords, ignored
# happiness of region = total for all tweets / number of tweets 	
def happy_score():
	for region in regionList:
		total = 0
		numTweets = 0
		
		# calculate score
		for i in happiness[region][0]:
			tweetScore = 0
			numKeywords = 0
			for tweetWord in i: 
				# remove all unnecessary symbols
				word = tweetWord.strip('/^"`&@_*\'•“”~[]<>()-+=0123456789»%$:\!.?#,;')
				word = word.lower()
			
				if word in keywords: 
					tweetScore = tweetScore + keywords[word]
					numKeywords += 1
			
			if	numKeywords != 0:
				total += tweetScore	/ numKeywords
				numTweets += 1
			else: 
				total += 0
					
		happiness[region][1] = numTweets
		
		if numTweets != 0:
			happiness[region][2] = total / numTweets
		else:
			happiness[region][2] = 0
	
def main(): 
	keywordsfile.close()
	tweetsfile.close()
	
	happy_score()
	
	for region in regionList:
		print(region + ': \n num of tweets: ' +  str(happiness[region][3]) + ' num of valid tweets: ' + str(happiness[region][1]) + ' happiness score: ' + str(happiness[region][2])) 
		print()
	
	# draw the happy histogram
	happy_histogram.drawSimpleHistogram(happiness['eastern'][2], happiness['central'][2], happiness['mountain'][2], happiness['pacific'][2])
	
main()




