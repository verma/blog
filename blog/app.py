from flask import Flask, render_template, abort
from model import Session, Picture, setupDB
from sqlalchemy.sql.expression import desc
from ordereddict import OrderedDict

import datetime

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

def getAge(d):
	dob = datetime.datetime(year=2009, month=5, day=6)

	months = (d.year - dob.year) * 12
	if d.month < dob.month:
		months -= dob.month - d.month
	else:
		months += d.month - dob.month

	if months > 24:
		years, months = divmod(months, 12)
		return "%s Years %s Months" % (years, months)
	else:
		return "%s Months" % (months)

@app.route('/suvan')
def suvan():
	s = Session()
	try:
		pictures = s.query(Picture).order_by(desc(Picture.date_uploaded)).all()
		d = OrderedDict()
		for p in pictures:
			dstr = p.date_uploaded.strftime('%B %d, %Y')
			if not d.has_key(dstr):
				d[dstr] = {}
				d[dstr]['date'] = dstr
				d[dstr]['age'] = getAge(p.date_uploaded)
				d[dstr]['pictures'] = []

			d[dstr]['pictures'].append(p)

		return render_template('suvan.html', pictures=d.values())
	finally:
		s.close()

@app.route('/music')
def music():
	return render_template('music.html')

@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == '__main__':
	setupDB('./')
	app.debug = True
	app.run()
