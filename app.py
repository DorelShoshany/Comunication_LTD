import ssl

from application import app



if __name__ == "__main__":

   #from OpenSSL import SSL
   #context = SSL.Context(SSL.PROTOCOL_TLSv1_2)
   #context.use_privatekey_file('server.key')
   #context.use_certificate_file('server.crt')

   app.run(port=80,ssl_context=('cert.pem', 'key.pem'))



