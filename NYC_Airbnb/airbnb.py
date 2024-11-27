import pandas as pd

last_review = pd.read_csv("NYC_Airbnb/airbnb_last_review.csv")
price = pd.read_csv("NYC_Airbnb/airbnb_price.csv")
roomtype = pd.read_excel('NYC_Airbnb/airbnb_room_type.xlsx')

last_review_df = pd.DataFrame(last_review)
price_df = pd.DataFrame(price)
roomtype_df =pd.DataFrame(roomtype)

# roomtype_df.set_index('listing_id').join(price_df.set_index('listing_id')).head(5)
#roomtype_df.join(price_df.set_index('listing_id'), on='listing_id').head(5)

#commented code below makes the last two columns NaN
#roomtype_df.join(price_df.set_index('listing_id'), on='listing_id').join(last_review_df.set_index(' listing_id')).head(5)
rp = roomtype_df.set_index('listing_id').join(price_df.set_index('listing_id')).join(last_review_df.set_index(' listing_id')).head(5)

#identify NAN
rp.isna().sum()
rp[rp.isna().any(axis=1)]

#Drop null values
rp.dropna(inplace= True)
rp.count()

#Duplicates
rp[rp.duplicated()]
rp.drop_duplicates(inplace=True)

# Last review to date time
rp["last_review"] = pd.to_datetime(rp["last_review"])

# changing currency type and format
rp['price'] = [i.strip("dollars") for i in rp['price']]
rp['price'] = [int(i) for i in rp['price']]
rp['price'] = rp['price'].map("${:,.0f}".format)

#checking values again for null values
rp.isnull().sum()

#convert dataframe to csv file
rp.to_csv("converted_airbnb_file.csv")
