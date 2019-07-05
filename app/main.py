from flask import Flask
from flask import render_template
from flask import request
import re
from collections import Counter


app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        f = request.files['file'].read()
        txt = str(f.decode('utf-8'))

        pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        ips = re.findall(pattern, txt)

        result = Counter(ips).most_common(10)

        ban = []
        for key, value in result:
            if value > 100:
                ban.append({'ip': key, 'frequency': value})

        return render_template('index.html', ips=ban)
    return render_template('index.html')



# def main():
#     data = open('log').read()
#
#     pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
#     ips = re.findall(pattern, data)
#
#     result = Counter(ips).most_common(10)
#
#     for key, value in result:
#         print(str(key) + ' - ' + str(value))



if __name__ == '__main__':
    app.run(debug=True)
