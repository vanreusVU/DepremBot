import snscrape.modules.twitter as sntwitter
import pandas as pd
import locationtagger

# Creating list to append tweet data to
tweets_list2 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('(mahallesi OR mahalle OR mah. OR sokak OR sok.) (min_faves:500) (#deprem)').get_items()):
    if i>1000:
        print("Reached level")
        break
    if tweet == None:
        print("No more data")
        break

    content = tweet.content
    entities = locationtagger.find_locations(text = content)
    tweets_list2.append([tweet.username, tweet.id, content, entities.countries, entities.regions])
    
# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list2, columns=['Username', 'Id', 'Text', 'İl', 'İlçe'])
tweets_df2.to_excel(r'./Tweets.xlsx', sheet_name='Deprem Tweets', index=False)
