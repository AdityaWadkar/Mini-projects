import pandas as pd
import datetime
import smtplib

GMAIL_ID = "Your mail id"
GMAIL_PSD = "your password"

def sendmail(to,sub,msg):
    print(F"email to {to} sent with subject {sub} and msg {msg}")
    s=smtplib.SMTP('smtp.gmail.com',587) 
    s.starttls()
    s.login(GMAIL_ID,GMAIL_PSD)
    s.sendmail(GMAIL_ID,to,f"subject: {sub} \n\n {msg}")
    s.quit()
if __name__ == "__main__":

    df=pd.read_excel("birthday.xlsx")
    today=datetime.datetime.now().strftime("%d-%m")
    presentyear=datetime.datetime.now().strftime("%Y")
 
    writeind = []
    for index,item in df.iterrows():
        
        bd=item["Birthday"].strftime("%d-%m")
       
        if (today == bd) and presentyear not in  str(item['Year']):
            sendmail(item["Email"],item["subject"],item["Dialogue"])
            writeind.append(index)
  
    for i in writeind:
        yr = df.loc[i,'Year'] 
        df.loc[i,'Year'] = str(yr) + ", " + str(presentyear)
        
    
    df.to_excel(r'birthday.xlsx',index = False)
