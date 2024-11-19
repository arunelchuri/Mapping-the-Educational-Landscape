import requests
from bs4 import BeautifulSoup as bs
import csv
#  Collecting the college data from Getmyuni website.
website=requests.get("https://www.getmyuni.com/all-colleges")
soup=bs(website.text,'html.parser')
Data=soup.find_all('div',class_="col-md-6 mobile__white__bg")
join1=[]
join2=[]
join3=[]
try:
    for k in Data:
        clg_det=k.find_all('div',class_='college__detail__row')
        for index,i in enumerate(clg_det):
            slno=index+1
            clg_name= i.find('h2',class_="college__name").text
            location=i.find('span',class_="list__style college__location").text
            PUB_prv=i.find('span',class_="list__style college__affiliation").text
            Rate=i.find('span',class_="list__style college__rating")
            Rating=(Rate.text.strip() if Rate is not None else " ")
            join1.append([slno,clg_name,location,PUB_prv,Rating])
    
    for m in Data:
        cour=m.find_all('div',class_="highlight__cta__row")
        for n in cour:
            Course= n.find('a')
            courses=(Course.text.strip() if Course is not None  else " " )
            Exam_Accept1=n.find('div',class_="highlight__div exam__accepted__div").find('span',class_="highlight__value").find('a')
            Exam2=(Exam_Accept1.text.split()[:] if Exam_Accept1 is not None else "")
            exam=','.join(Exam2)
            fees=n.find_all('div',class_="highlight__div")[2].find('span',class_="highlight__value").text.strip()
            Accreditation=n.find_all('div',class_="highlight__div")[3].find('span',class_="highlight__value")
            Accreditation1= ' '.join(Accreditation.get_text(strip=True).split())
            join2.append([courses,exam,fees,Accreditation1])
    # Here joining the two lists.   
    result=[join3 for a  in zip (join1,join2) for join3 in a ]
    for i in range(0,len(result),2):
        Result1_= result[i]+result[i+1]
        join3.append(Result1_)  
    # saving the college data in a CSV file.
    file_name= "college.csv"
    Col_titles=["Slno","College","Location","Pri/Gov","Rating","Courses","Eligible Exam","Fees","Accreditatio"]
    with open(file_name, mode="w", newline="", encoding="utf-8") as file:
        data = csv.writer(file)
        data.writerow(Col_titles)       
        data.writerows(join3)
        print(" csv file is saved")
        
except Exception as error:
    print(f"{error}")
    
    

