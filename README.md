# hazinsesv2
vargi/hazinses updated to work with the new celery.

## hazinSES

![hazinses](http://ucuncuadam.files.wordpress.com/2012/02/sami-hazinses-2.jpg?w=500&h=389 "hazinses")

#####ABOUT

Hazinses is a django app, that helps you to send asynchronous email via celery through Amazon-SES. The biggest problem
is complaint and bounce emails that come as feedback from amazon services. Those emails cause you to be reported as Hard Bounce in case you keep sending emails
and prevent forever you to send email to that user again.


#####INSTRUCTIONS

1) install hazinses app

    pip install hazinsesv2
    
make sure that you installed hazinses requirements
    
    ['boto', 'celery']
    
2) Add hazinses into your INSTALLED_APPS 


    INSTALLED_APPS += ('hazinses')


3) Add hazinses to your urls.py

    url(r'^hazinses/', include('hazinses.urls')),
    
4) Set following settings to your settings.py

    AMAZON_REGION = '<YOUR AMAZON REGION>'
    AWS_ACCESS_KEY_ID = '<AWS_ACCESS_KEY_ID>'
    AWS_SECRET_ACCESS_KEY = '<AWS_SECRET_ACCESS_KEY>'
    BOUNCE_TIMEDELTA = <DAYS FOR NOT SENDING EMAIL AFTER BOUNCE NOTIFICTAION>
    COMPLAINT_TIMEDELTA = <DAYS FOR NOT SENDING EMAIL AFTER COMPLAINT NOTIFICATION>

4) Sync your Database
    
    python manage.py syncdb
    
    
5) RUN CELERY...

    python manage.py celery
    
6) Use default send_mail function of django, after you change the email backend settings from your settings.py like below

    EMAIL_BACKEND = "hazinses.EmailBackend"

                     
                     
###### THANKS

thanks to serdarakarca
thanks to https://github.com/vargi
