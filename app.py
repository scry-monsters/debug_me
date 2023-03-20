from flask import Flask, render_template
from feature import getFeature
import pickle

file = open('pickle_model.pkl', 'rb')
# Traceback (most recent call last):
#File "/Users/scry/Desktop/coding/web-dev/test_final_phishing/app.py", line 6, in <module>
#gb = pickle.load(file)
#ModuleNotFoundError: No module named 'sklearn'
gb = pickle.load(file)
file.close()

app = Flask(__name__)

@app.route('/')
def index():
    #проверка если этот код вообще работает
    url='https://vk.com/scry_monsters'
    return render_template('index.html', obj=url)

if __name__ == '__main__':
    app.run(debug=True)
