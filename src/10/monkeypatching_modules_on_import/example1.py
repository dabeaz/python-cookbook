from postimport import when_imported

@when_imported('threading')
def warn_threads(mod):
    print('Threads? Are you crazy?')

if __name__ == '__main__':
    import threading
