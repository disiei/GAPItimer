import requests
import datetime

f = open("access.txt", "a")


t_ini = datetime.datetime.now()
HTTPreq = requests.get('https://content-sheets.googleapis.com/$discovery/rest?version=v4&pp=0&fields=fields%5B%22kind%22%5D%2Cfields%5B%22name%22%5D%2Cfields%5B%22version%22%5D%2Cfields%5B%22rootUrl%22%5D%2Cfields%5B%22servicePath%22%5D%2Cfields%5B%22resources%22%5D%2Cfields%5B%22parameters%22%5D%2Cfields%5B%22methods%22%5D%2Cfields%5B%22batchPath%22%5D%2Cfields%5B%22id%22%5D&key=AIzaSyBP_kVQrTe2vm3JoicescF5DAb1mrn_wxM')
t_fi = datetime.datetime.now()

f.write(str(t_ini) + " - "+ str(t_fi) + "\n")

f.write("Status: " + str(HTTPreq.status_code) + "\n")
f.write("Elapsed: " + str(HTTPreq.elapsed) + "\n")

f.write("\n")
f.close()

f = open("access.txt", "r")
print(f.read())
