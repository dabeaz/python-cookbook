# ssl_xmlrpc_client.py
#
# An XML-RPC client that verifies the server certificate

from xmlrpc.client import SafeTransport, ServerProxy
import ssl

class VerifyCertSafeTransport(SafeTransport):
    def __init__(self, cafile, certfile=None, keyfile=None):
        super().__init__()
        self._ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        self._ssl_context.load_verify_locations(cafile)
        if certfile:
            self._ssl_context.load_cert_chain(certfile, keyfile)
        self._ssl_context.verify_mode = ssl.CERT_REQUIRED

    def make_connection(self, host):
        s = super().make_connection((host, {'context': self._ssl_context}))

        return s

# Create the client proxy
s = ServerProxy('https://localhost:15000', 
                transport=VerifyCertSafeTransport('server_cert.pem', 'client_cert.pem', 'client_key.pem'),
#                transport=VerifyCertSafeTransport('server_cert.pem'),
                allow_none=True)

s.set('foo', 'bar')
s.set('spam', [1, 2, 3])
print(s.keys())
print(s.get('foo'))
print(s.get('spam'))
s.delete('spam')
print(s.exists('spam'))

