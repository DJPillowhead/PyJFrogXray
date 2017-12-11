# PyJFrogXray
JFrog Xray Rest API Python

#Usage
baseuri = "http://example.com:8000"
username = "username"
password = "pass"
myXray = xray_jfrog_api(baseuri,username,password)

#Get all the Xray Components
myComponents = myXray.getComponents(num_of_rows="1",
                    severity="Critical",
                    component_type="packages")
print myComponents