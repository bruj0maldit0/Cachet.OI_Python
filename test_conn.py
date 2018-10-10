import requests
import pyodbc

proxies = {
    'http': 'http://diazi:34Bl4ckm3t4l@proxy.standard.corp:8080',
    'https': 'http://diazi:34Bl4ckm3t4l@proxy.standard.corp:8080',
}

server = '10.101.178.29,1433'
# Create the session and set the proxies.
s = requests.Session()
s.proxies = proxies

# Make the HTTP request through the session.
r = s.get('https://www.google.com/', proxies=proxies)

# Check if the proxy was indeed used (the text should contain the proxy IP).
if r.status_code == 200:
    print(r.text)
    r.status_code
    print(r)


try:
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=10.101.178.29,1433;DATABASE=dba_tools;UID=sa;PWD=Faurecia01')
    cursor = cnxn.cursor()

    cursor.execute("SELECT @@VERSION;")
    row = cursor.fetchone()
    ##r = s.put('https://www.google.com/', proxies=proxies)
    print ('SQL Server is up and running ' + server + ' ' + str(row[0]))
except pyodbc.OperationalError:
        print ('SQL Server Service unavailable ' + server)

url = "https://demo.cachethq.io/api/v1/incidents"

payload = "{\"name\":\"SQL Server\",\"message\":\"Service is down\",\"status\":1,\"visible\":1,\"component_id\":4,\"notify\":\"true\",\"component_status\":0,\"created_at\":\"2018-08-29\"}"
response = requests.request("POST", url, data=payload)

print(response.text)
