from configparser import ConfigParser
cfg = ConfigParser()
cfg.read('config.ini')
print('sections:', cfg.sections())
print('installation:library', cfg.get('installation','library'))
print('debug:log_errors', cfg.getboolean('debug','log_errors'))
print('server:port', cfg.getint('server','port'))
print('server:nworkers', cfg.getint('server','nworkers'))
print('server:signature', cfg.get('server','signature'))
