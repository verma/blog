# FCGI script

from flup.server.fcgi import WSGIServer
from blog import app, setupDB

database_path = '/var/lib/udayv.com'
bind_address = '/var/lib/udayv.com/fcgi.sock'

print 'Using database:', database_path
setupDB(database_path)

print 'Using bind address:', bind_address
WSGIServer(app, bindAddress=bind_address, umask=7).run()
