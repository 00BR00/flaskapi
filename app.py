from flask import Flask, jsonify, render_template_string, request

app = Flask(__name__)

systems_mapping = {
    "navigation": "NAV-01",
    "communications": "COM-02",
    "life_support": "LIFE-03",
    "engines": "ENG-04",
    "deflector_shield": "SHLD-05"
}

damaged_system = "engines"  

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"damaged_system": damaged_system})

@app.route('/repair-bay', methods=['GET'])
def repair_bay():
    code = systems_mapping.get(damaged_system, "UNKNOWN")
    html_template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Repair</title>
    </head>
    <body>
    <div class="anchor-point">{{ code }}</div>
    </body>
    </html>
    '''
    return render_template_string(html_template, code=code)

@app.route('/teapot', methods=['POST'])
def teapot():
    return "I'm a teapot", 418

if __name__ == '__main__':
   
    app.run(host='0.0.0.0', port=5000, debug=True)
