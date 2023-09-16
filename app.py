from flask import Flask,render_template,jsonify

app = Flask(__name__)


JOBS = [
  {
    'id' : 1,
    'title' : 'Data analyst',
    'location' : 'Delhi',
    'salary' : 'Rs. 100000'
  },
  {
    'id' : 2,
    'title' : 'Data Scientist',
    'location' : 'Bengaluru',
    'salary' : 'Rs. 150000'
  },
  {
    'id' : 3,
    'title' : 'front End develper',
    'location' : 'Delhi',
    'salary' : 'Rs. 120000'
  },
  {
    'id' : 4,
    'title' : 'Back End Engineer',
    'location' : 'Remote',
    'salary' : 'Rs. 125000'
  }
]


@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS,company_name="Chauhan")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)



if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)