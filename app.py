
from ﬂask import Flask, render_template

app = Flask(  name  )

@app.route('/') def index():

"""

Renders the main index.html template for the Smart Register application. """

return render_template('index.html')

if   name	== '  main  ':

# Run the Flask application in debug mode for development app.run(debug=True)
