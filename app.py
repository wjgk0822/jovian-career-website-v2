from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
{
  'id':1,
  'title': 'Data Analyst',
  'Location': 'Bengluru, India',
  'salary': 'Rs. 10,00,000'
},
{
  'id':2,
  'title': 'Data Scientist',
  'Location': 'Delhi, India',
  'salary': 'Rs. 15,00,000'
},
{
  'id':3,
  'title': 'Frontend Engineer',
  'Location': 'Remote',
  
},
{
  'id':4,
  'title': 'Backend Engineer',
  'Location': 'San Francisco, USA',
  'salary': '$120,000'
}
]



@app.route("/")
def hello_world():
  return render_template('home.html', 
                         jobs=JOBS,     company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  return jsonfly(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
