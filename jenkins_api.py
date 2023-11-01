import csv

def List_job(jenkins_url,jenkins_user,jenkins_pass):
    import jenkins

    jen_server =  jenkins.Jenkins(jenkins_url, username= jenkins_user, password=jenkins_pass)
    user = jen_server.get_whoami()
    jobs = jen_server.get_jobs()

    job_stats=[]
    for i in jobs:
        #print(i['name'])
        #print("*****************")
        job_name =i['name']
        job_url = i['url']
        job_status= i['color']
        job_stats.append([job_name,job_url,job_status])
    return job_stats

#c=List_job('http://45.33.11.12:8080','utrains','devops')

#print(c)

"""with open("example.txt",'a') as f:
    content = "adding data into file\n"
    f.write(content)

with open("example.txt", 'r') as file:
    cont = file.read()
    print(cont)
"""
data=List_job('http://45.33.11.12:8080','utrains','devops')
with open("jenkins_object.csv",'w') as j:
    write_row =csv.writer(j)
    write_row.writerow(['JOB_NAME', 'JOB_URL','JOB_STATUS'])
    for item in data:
     write_row.writerow(item)