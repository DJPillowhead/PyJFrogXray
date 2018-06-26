import requests
from requests.auth import HTTPBasicAuth
import json
import getpass


class xray_jfrog_api:

    def __init__(self, baseuri, username, password):
        self.baseuri = baseuri
        self.auth = HTTPBasicAuth(username, password)

    # direction = desc, asc
    # severity = Critical, Major, Minor, Unknown
    def getComponents(self, direction="desc", num_of_rows="20",
                      order_by="last_updated", page_num="1",
                      severity=None, component_type=None):

        myURL = self.baseuri + "/api/v1/watches"
        querystring = {}
        # querystring.update({"direction": direction})
        # querystring.update({"num_of_rows": num_of_rows})
        # querystring.update({"order_by": order_by})
        # querystring.update({"page_num": page_num})

        payload = {}
        # if severity:
        #     payload.update({"severity": severity})
        # if component_type:
        #    payload.update({"component_type": component_type})

        headers = {
            'content-type': "application/json;charset=UTF-8",
            'accept': "application/json, text/plain, */*",
        }
        response = requests.request("GET", myURL,
                                    data=json.dumps(payload),
                                    auth=self.auth,
                                    headers=headers,
                                    params=querystring)
        return response.json()


if __name__ == "__main__":
    baseuri = "http://xray.chemaxon.com"
    username = raw_input("Username:")
    password = getpass.getpass("Password for " + username + ":")
    d = xray_jfrog_api(baseuri, username, password)
    x = d.getComponents(num_of_rows="1",
                        severity="Critical",
                        component_type="packages")
    print x
