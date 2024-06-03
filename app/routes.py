from flask import Flask, render_template, request
from.forms import SimpleForm
import xml.etree.ElementTree as ET 
import os

app = Flask(__name__)

def parse_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        datos = []
        for child in root:
            datos.append(child.attrib)
        return datos
    except Exception as e:
        print(e)
        return None

@app.context_processor
def inject_form():
    return dict(form=SimpleForm())

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/specially_for_you', methods=['GET', 'POST'])
def specially_for_you():
    form = SimpleForm()
    selected_fruits = None
    selected_alco = None
    selected_nonalco = None
    selected_others = None

    if request.method == 'POST' and form.validate():
        selected_fruits = form.fruits_cb.data
        selected_alco = form.alco_cb.data
        selected_nonalco = form.nonalco_cb.data
        selected_others = form.others_cb.data

    return render_template('specially_for_you.html', form=form,
                           selected_fruits=selected_fruits,
                           selected_alco=selected_alco,
                           selected_nonalco=selected_nonalco,
                           selected_others=selected_others)

@app.route('/cocktails')
def cocktails():
    file_path = os.path.join(os.path.dirname(app.root_path), 'data', 'cocktails.xml')
    datos = parse_xml(file_path)
    return render_template('cocktails.html', datos=datos)

def run_app():
    app.run(debug=True)

if __name__ == '__main__':
    run_app()