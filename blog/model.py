from sqlalchemy import Table, Column, Integer, String, \
        Boolean, ForeignKey, MetaData, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relation, backref
from sqlalchemy import create_engine, func

import os
import datetime

Base = declarative_base ()
metadata = Base.metadata
Session = sessionmaker ()

class Picture(Base):
	"""A class representing one available picture."""
	__tablename__ = "pictures"

	id = Column(Integer, primary_key=True)
	file_path = Column(String(255))
	file_thumb_path = Column(String(255))
	date_uploaded = Column(DateTime)

	def __init__(self, file_path, file_thumb_path, date_uploaded = None):
		self.file_path = file_path
		self.file_thumb_path = file_thumb_path
		if date_uploaded is None:
			self.date_uploaded = datetime.datetime.combine(datetime.date.today(),
					datetime.time())
		else:
			self.date_uploaded = date_uploaded

	def __str__(self):
		return '<Picture %s (%s)>' % (self.file_path, self.date_uploaded.strftime('%B %d, %Y'))
		

def setupDB (path):
	dbpath = os.path.join (path, 'db.db')
	engine = create_engine ('sqlite:///' + dbpath, echo=False)

	Session.configure (bind=engine)
	metadata.create_all (engine)

if __name__ == "__main__":
	import os
	setupDB(os.getcwd())
	print 'Database setup complete.'

