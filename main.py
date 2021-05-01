# Import modules
from flask import Flask, render_template, redirect, request, url_for
import dataset
import os
import shutil

# Connect to database
db_init = dataset.connect('sqlite:///db.sqlite3')
db = db_init['patients']

# Create app instance
app = Flask(__name__)

# Index/search route
@app.route('/')
def search():
	patients = list(db.all())
	return render_template('search.html', patients=patients)

# Create route
@app.route('/new')
def new():
	return render_template('new.html')

# Add route
@app.route('/add', methods=['POST'])
def add():
	patient = {
		'first_name': request.form.get('first_name'),
		'last_name': request.form.get('last_name'),
		'phone': request.form.get('phone'),
		'address': request.form.get('address'),
	}
	db.insert(patient)
	return redirect(url_for('search'))

# View patient route
@app.route('/view/<int:pid>')
def view(pid):
	patient = db.find_one(id=pid)
	try:
		uploaded_files = [f for f in os.listdir(f'static/uploads/{pid}') if os.path.isfile(os.path.join(f'static/uploads/{pid}', f))]
	except FileNotFoundError:
		uploaded_files = None
	return render_template('view.html', patient=patient, files=uploaded_files)

# Edit patient's info route
@app.route('/edit/<int:pid>')
def edit(pid):
	patient = db.find_one(id=pid)
	return render_template('edit.html', patient=patient)

# Update patient's info route
@app.route('/update/<int:pid>', methods=['POST'])
def update(pid):
	# get patient's data
	patient = {
		'first_name': request.form.get('first_name'),
		'last_name': request.form.get('last_name'),
		'phone': request.form.get('phone'),
		'address': request.form.get('address'),
		'id': pid
	}
	db.update(patient, ['id'])
	return redirect(url_for('view', pid=pid))

# Delete patient route
@app.route('/delete/<int:pid>', methods=['POST'])
def delete(pid):
	# remove from database
	db.delete(id=pid)
	# delete patient's files if any
	try:
		shutil.rmtree(f'static/uploads/{pid}')
	except:
		pass
	# redirect to homepage
	return redirect(url_for('search'))

# Upload route
@app.route('/upload/<int:pid>', methods=['GET', 'POST'])
def upload(pid):
	if request.method == 'POST':
		files = request.files.getlist("file")
		if files:
			try:
				os.makedirs('static/uploads')
			except:
				pass
			try:
				os.makedirs(f'static/uploads/{pid}')
			except:
				pass
			for file in files:
				file.save(os.path.join(f'static/uploads/{pid}', file.filename))
		return file.filename
	else:
		patient = db.find_one(id=pid)
		return render_template('upload.html', patient=patient)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=7000, debug=True, threaded=True)