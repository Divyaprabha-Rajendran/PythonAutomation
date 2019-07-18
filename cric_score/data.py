import urllib.request as url
from bs4 import BeautifulSoup

class data:
  score=''
  wicket=''
  overs=''
  batsman1=''
  batsman2=''
  Bowler=''

  prev_score=''
  prev_wicket=''

  def refresh(self):
    global score
    global wicket
    global overs
    global batsman1
    global batsman2
    global Bowler
    global prev_score
    global prev_wicket

    sock = url.urlopen("http://www.espncricinfo.com/series/17891/game/1109602/Sri-Lanka-vs-India-1st-India-tour-of-Sri-Lanka-2017/")
    htmlSource = sock.read()
    soup = BeautifulSoup(htmlSource, 'html.parser')
    #print (soup)

    data = soup.find_all("title")
    print (data)
    print (len(data))
    data1=str(data[0])
    check=data1.strip('<title>')
    check=check.strip(') - Live | Match Summary | ESPNCricinfo</title>')
    print (check)



    split_data=check.split('(')
    print (len(split_data))
    score = split_data[0]
    wicket = score.split('/')[1]
    add_data=split_data[1].split(',')
    print (len(add_data))
    overs=add_data[0]
    batsman1=add_data[1]
    batsman2=add_data[2]
    Bowler=add_data[3]


    print(score)
    print(wicket)
    print(overs)
    print(batsman1)
    print(batsman2)
    print(Bowler)





