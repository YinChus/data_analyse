
#we are sending emails through Django
# this is the example.... create a local_settings.py file and copy this

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 465
EMAIL_HOST_USER = '1871645411@qq.com'
EMAIL_HOST_PASSWORD = 'ufepwtcsrqfgcaac'