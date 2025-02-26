from flask import Flask, render_template , request
import requests

app = Flask(__name__)
url_link_api = "http://127.0.0.1:5000"

@app.route("/")
def start(): 
    return render_template('sign_in.html')
    

@app.route("/index", methods=['GET','POST'])
def index():
    login = request.form['login']
    passsword = request.form['password']
    
    donnees = list([login,passsword])
    print(donnees)
    response = requests.post(url_link_api + "/api/recevoir-donnees",json=donnees)
    print(response)
    if response.ok:         #print(response) -> <Response [200]>
        return render_template('start.html')
    else:
        return render_template('start.html')

@app.route("/users")
def users(): 
    return render_template('users.html')

@app.route("/list_serv_web")
def list_serv_web(): 
    return render_template('list_serv_web.html')

@app.route("/detail_conf_serv_web")
def detail_conf_serv_web(): 
    return render_template('detail_conf_serv_web.html')

@app.route("/ajout_serv_web")
def ajout_serv_web(): 
    return render_template('ajout_serv_web.html')
    
@app.route("/suppr_serv_web")
def suppr_serv_web(): 
    return render_template('suppr_serv_web.html')

@app.route("/list_serv_load_balancer")
def list_serv_load_balancer(): 
    return render_template('list_serv_load_balancer.html')

@app.route("/detail_conf_serv_load_balancer")
def detail_conf_serv_load_balancer(): 
    return render_template('detail_conf_serv_load_balancer.html')

@app.route("/ajout_serv_load_balancer")
def ajout_serv_load_balancer(): 
    return render_template('ajout_serv_load_balancer.html')
    
@app.route("/suppr_serv_load_balancer")
def suppr_serv_load_balancer(): 
    return render_template('suppr_serv_load_balancer.html')

@app.route("/list_serv_reverse_proxy")
def list_serv_reverse_proxy(): 
    return render_template('list_serv_reverse_proxy.html')

@app.route("/detail_conf_serv_reverse_proxy")
def detail_conf_serv_reverse_proxy(): 
    return render_template('detail_conf_serv_reverse_proxy.html')

@app.route("/ajout_serv_reverse_proxy")
def ajout_serv_reverse_proxy(): 
    return render_template('ajout_serv_reverse_proxy.html')
    
@app.route("/suppr_serv_reverse_proxy")
def suppr_serv_reverse_proxy(): 
    return render_template('suppr_serv_reverse_proxy.html')

@app.route("/api-test")
def api_test():
    parametre_get = request.args.get('bool')
    print(parametre_get)
    return 'true'

def check_sign_in():
    return True
