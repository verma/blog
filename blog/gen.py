from model import *
import os
import shutil


image_url = '/static/pictures/'
image_path = 'static/pictures/'
image = '/tmp/img.jpg'
image_thumb = '/tmp/img_thumb.jpg'

def add_image(path, path_thumb, fordate):
	s = Session()
	try:
		p = Picture(path, path_thumb, fordate)
		s.add(p)
		s.commit()
	except Exception, e:
		s.rollback()
		print 'Failed to add image:', e
		sys.exit(1)
	finally:
		s.close()

def gen_images(for_date, count):
	print 'Adding %s images for date %s' % (count, for_date.strftime('%Y%m%d'))
	for i in range(count):
		d = '%s_%s.jpg' % (for_date.strftime('%Y%m%d'), i)
		dt = '%s_%s_thumb.jpg' % (for_date.strftime('%Y%m%d'), i)

		pi = os.path.join(image_path, d)
		pit = os.path.join(image_path, dt)

		shutil.copyfile(image, os.path.join(image_path, d))
		shutil.copyfile(image_thumb, os.path.join(image_path, dt))

		li = os.path.join(image_url, d)
		lit = os.path.join(image_url, dt)

		add_image(li, lit, for_date)

if __name__ == "__main__":
	import datetime

	setupDB('./')

	d = datetime.datetime.now()
	gen_images(d, 10)
	gen_images(d + datetime.timedelta(days=1), 10)
	gen_images(d + datetime.timedelta(days=2), 10)
	gen_images(d + datetime.timedelta(days=20), 10)




