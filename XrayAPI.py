import requests
from requests.auth import HTTPBasicAuth
import json


class xray_jfrog_api:

    def __init__(self, baseuri, username, password):
        self.baseuri = baseuri
        self.auth = HTTPBasicAuth(username, password)

    # direction = desc, asc
    # severity = Critical, Major, Minor, Unknown
    def getComponents(self, direction="desc", num_of_rows="20",
                      order_by="last_updated", page_num="1",
                      severity=None, component_type=None):

        myURL = self.baseuri + "/ui/component/paginatedsearch"
        querystring = {}
        querystring.update({"direction": direction})
        querystring.update({"num_of_rows": num_of_rows})
        querystring.update({"order_by": order_by})
        querystring.update({"page_num": page_num})

        payload = {}
        if severity:
            payload.update({"severity": severity})
        if component_type:
            payload.update({"component_type": component_type})

        headers = {
            'content-type': "application/json;charset=UTF-8",
            'accept': "application/json, text/plain, */*",
        }
        response = requests.request("POST", myURL,
                                    data=json.dumps(payload),
                                    auth=self.auth,
                                    headers=headers,
                                    params=querystring)
        return response.json()


if __name__ == "__main__":
    baseuri = "http://example.com:8000"
    username = "username"
    password = "pass"
    d = xray_jfrog_api(baseuri, username, password)
    x = d.getComponents(num_of_rows="1",
                        severity="Critical",
                        component_type="packages")
