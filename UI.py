from flask import Flask,render_template,request, send_file, session
import requests

import os
import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# api-endpoint
METRICS_URL = "http://127.0.0.1:8000/metrics"
TAG_URL = "http://127.0.0.1:8000/tags"
QA_URL = "http://127.0.0.1:8000/questions"
# location given here
#JD = """description scope role piramal pharma solutions pps chief information officer cio role provide vision leadership developing implementing information technology initiatives align vision piramal pharma solutions pps businesses pps cio charter build competitive edge business proactively building world class high quality innovative technology digital analytics solutions global operations job overview strategy innovation strategic business partner create enhanced digital technology vision enterprise identify opportunities differentiated technology capabilities solutions p roactively recommend solutions business functional leadership team considering business vision industry trends bringing outside perspective p ush bar technology innovation imbibing cutting edge technological innovations global benchmarks blue sky thinking create user friendly technologies offering great experience cts champion change agent accelerating organizational changes required create sustain enterprise technology capabilities cts thought leader emerging digital business models technologies articulating digital future enterprise role internally externally enable business growth enable inorganic business growth merger acquisition leading due diligence driving integration post acquisition lead strategic operational planning implementation achieve business goals fostering innovation prioritizing initiatives coordinating evaluation deployment management current future systems across organization coordinate facilitate consultation relevant business stakeholders define business systems requirements new technology implementations planning execution partner various site ho teams manage project portfolio relate selection acquisition development implementation major information systems defines governance mechanism metrics review progress technology projects business case achievement technology budget company provide upfront estimates costs various heads keep track spends ensure best roi company technology investment maintaining balance frugality financial discipline adequately gearing future growth b uild ecosystem group technology teams partners including startups product vendors develop implement technology solutions b uild future read technology team attracting retaining upskilling industry best talent compliance information security collaborate piramal quality e compliance qec team ensure quality compliance per defined sops guidelines accordance 21 cfr part 11 gamp guidelines collaborate information security team ensure adherence information security guidelines processes skills abilities exceptional inter personal skills enabling engagement levels across leadership skills including ability manage large team understanding strategy business technology application levels environment priorities goals quickly change evolve also skills think strategically including developing information security strategies interpreting handling complex information acting political sensitivity driving engaging positively change sound understanding portfolio program project management track record delivering enabling large scale complex change programs qualifications experience delivering strategy delivery essential across multiple organisations desirable experience working pharma business senior position essential experience procuring managing large complex outcome based contracts interdependencies experience working senior management team develop business focussed strategies effectively support business needs experience technologies sap salesforce bi pharma quality applications preferred experience digital technologies ar vr rpa chatbots ai ml etc preferred experience joint procurement market testing outsourcing well negotiating quality cost effective services experience successfully implementing strategy business planning evidence delivering high quality customer focussed services experience contributing development implementation effective management information systems aid decision making process evidence contribution major transformation building teams time change"""

# defining a params dict for the parameters to be sent to the API
#PARAMS = {'data': JD}

# sending get request and saving the response as response object
#r = requests.get(url=URL, params=PARAMS)

# extracting data in json format
#ner = r.json()

path = os.path.join(os.getcwd(), "static/")
for file in os.listdir(path):
    try:
        if file.endswith('.png'):
            os.remove(path+file)
    except:
        pass

def get_metrics():
    s = requests.get(url=METRICS_URL)
    details = s.json()
    df = pd.DataFrame(details)
    sns.set(style='darkgrid')
    f, ax = plt.subplots(figsize=(16, 5))
    splot = sns.barplot(x='Metrics', y="percentage", hue='Models', data=df, ax=ax,
                        palette="gist_earth_r")

    for p in splot.patches:
        splot.annotate("{0:.2f}%".format(p.get_height() * 100), (p.get_x() + p.get_width() / 2., p.get_height()),
                       ha='center', va='center', xytext=(0, 10), textcoords='offset points',
                       fontsize=14)
    # Create plot
    plt.title("Model Performance\n\n", fontsize=20,fontweight='bold')
    plt.xlabel("Metrics", fontsize=14)
    plt.ylabel("Score (%)", fontsize=14)
    plt.tight_layout()
    plt.tick_params(labelsize=14)
    plt.ylim(0.0, 1.1)
    plt.legend(loc="center left",prop={'size': 18},
               framealpha=1, shadow=True, borderpad=1,
               bbox_to_anchor=(1, 0.5))
    image_name = "static/{}_{}.png".format("performance",
                            str(int(random.random()*100)))  # could be a uuid instead of datetime
    plt.savefig(image_name, bbox_inches='tight')
    return image_name

image_url = get_metrics()

app = Flask(__name__,static_folder="static")

#headings =  ("Words","Tags")
#data = ner.get('Entities')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           image_url = image_url)


@app.route('/tags', methods =["GET", "POST"])
def tags():
   if request.method == "POST":
      MDL = request.form.get("drops")
      options = request.form.get("drops")
      #print(options)
      JD = request.form.get("jobdesc")
      PARAMS = { 'model' : MDL,
                 'jobdesc': JD.lower()}
      r = requests.get(url=TAG_URL, params=PARAMS)
      ner = r.json()
      headings = ("Words", "Tags")
      data = ner.get('Entities')
      qadata = []
      try:
         tags = [tag[0] for tag in data]
         PARAMS = {'data': tags}
         r = requests.get(url=QA_URL, params=PARAMS)
         questions = r.json()
         qadata = questions.get('questions')
      except:
         pass
      nques = len(qadata)
      return render_template('index.html',
                             table_headings=headings,
                             table_data=data,
                             JD=JD,
                             questions = qadata,
                             n_quesions = nques,
                             image_url = image_url,
                             options = options)


if __name__ == '__main__':
   app.run(debug=True)