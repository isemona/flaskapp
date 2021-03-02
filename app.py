from flask import Flask 
  
app = Flask(__name__) 
  
@app.route('/', methods=['GET']) 
def hello(): 
    html_content = '''<h1>Hello, World!</h1>'''
    return html_content
  
if __name__ == "__main__": 
  app.run(debug=True, port=8000)