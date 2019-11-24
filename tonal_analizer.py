def tonal_analize(string):
	from dostoevsky.tokenization import RegexTokenizer
	from dostoevsky.models import FastTextSocialNetworkModel

	tokenizer = RegexTokenizer()
	model = FastTextSocialNetworkModel(tokenizer=tokenizer)
	messages = [string]
	results = model.predict(messages, k=2)

	for message, sentiment in zip(messages, results):
	    negative = 0
	    positive = 0
	    
	    if 'positive' in sentiment:
	    	positive += sentiment['positive']
	    if 'negative' in sentiment:
	    	negative += sentiment['negative']
	    
	    delta = positive - negative
	    
	return delta