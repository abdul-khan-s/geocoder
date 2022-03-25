import boto3

AWS_ACCESS_KEY_ID = ''  ## Add access key here
AWS_SECRET_ACCESS_KEY = ''   ## Add the secret key here that you get from JK

addr_list = ['Boston, MA united states', 'Paris, France', 'Milan, Italy', '20 W 34th St, New York']

client = boto3.client('location',
		     AWS_ACCESS_KEY_ID = '' , ## Add access key here
		     AWS_SECRET_ACCESS_KEY = ''   ## Add the secret key here that you get from JK) # Calls AWS Location component
		     )
for i in addr_list:
	Response = client.search_place_index_for_text(
		IndexName = 'geocoding_test4',  # This is the AWS Location service name that was created to use HERE.COM
		Text = i ) 


	Lat_Long = Response['Results'][0]['Place']['Geometry']['Point']  # get lat long
	Country = Response['Results'][0]['Place']['Label'] # get address
	#print (Response)
	print (Lat_Long)  
	print (Country)

	# write the results back.
