
from ﬂask import Flask, render_template

app = Flask(  name  )

@app.route('/') def index():
def home():
   return render_template('index.html')

if   name	== '_main_':
    app.run(debug=True)
