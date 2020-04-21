from application import app

'''
from OpenSSL import SSL
from OpenSSL import SSL
context = SSL.Context(SSL.TLSv1_2_METHOD)
context.use_privatekey_file('server.key')
context.use_certificate_file('server.crt')

   app.run(ssl_context = context)

'''


if __name__ == "__main__":
   app.run()



