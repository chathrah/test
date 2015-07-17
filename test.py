import json

# LOAD and read JSON file
json_file='/Users/ChathraHendahewa/Desktop/test.json'
json_data=open(json_file)
data = json.load(json_data)
json_data.close()

# print json in readable format
print json.dumps(data,indent=1)

# print required fields: Keywords, url, par
print data['_source']['Keywords'] # print keywords
print data['_source']['url'] # url
print data['_source']['par'] # par value
print data['_source']['postDate'][0:10] # extract the post date value only that is applicable for the PAR value



