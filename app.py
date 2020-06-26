import ssl
from application import app

if __name__ == "__main__":

   #from OpenSSL import SSL
   #print(type(ssl.PROTOCOL_TLSv1_2))
   #context = SSL.Context(ssl.PROTOCOL_TLSv1_2)
   #context.use_privatekey_file('key.pem')
   #context.use_certificate_file('ert.pem')

   app.run(port=80 ,ssl_context=('cert.pem', 'key.pem'))



