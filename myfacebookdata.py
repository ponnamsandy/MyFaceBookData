# MyFaceBookDataimport json
import requests
token="EAACEdEose0cBANN9xPE9oggndS8CRZCzJekdRW7MtZBC3jqCOC6qtsqVZA9oBuedVK0U4U48yxQZC6h71inp7bRsOnaFBzhex68QmlTEpBxTeN8tMyOQzqY4fSl9s1gxhe5s7mYG9IMZBJxdHzCQhsnWMML8zntnc9N33IrW1ma6KI0ROZBrKViMvMMclhwHMZD"


print("My Facebook profile details : ")
me="https://graph.facebook.com/v2.12/me?access_token="+token
request=requests.get(me)
name_json=request.json()
converted_name_json=json.dumps(name_json)
print(converted_name_json)



print("---------------------------------------------------------------")
print("My Facebook friends list : ")
friends="https://graph.facebook.com/v2.12/me/friends?access_token="+token
request1=requests.get(friends)
k=request1.json()
converted=json.dumps(k)
friends_list=converted[315:719]
print("\n".join(friends_list.split(",")))
print("Total friends: "+converted[748:751])

print("---------------------------------------------------------------")
print("Likes list in my facebook database : ")
Likes="https://graph.facebook.com/v2.12/me/likes?access_token="+token
request2=requests.get(Likes)
k1=request2.json()
converted1=json.dumps(k1)
Like_list=converted1[816:3025]
print("\n".join(Like_list.split(",")))


print("---------------------------------------------------------------")
print("print my data of birth : ")
Dob="https:/graph.facebook.com/v2.12/me/birthday?access_token="+token
request3=requests.get(Dob)
k2=request3.json()
print(k2)


