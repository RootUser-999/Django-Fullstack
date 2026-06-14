from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save,pre_delete,post_delete,pre_init,post_init
from django.core.signals import request_started,request_finished,got_request_exception
from django.db.models.signals import pre_migrate,post_migrate
from django.db.backends.signals import connection_created

@receiver(user_logged_in,sender=User)
def login_success(sender, request, user, **kwargs):
    print("Login Success")
    print("Sender:", sender)
    print("Request:", request)
    print("User:", user)

# user_logged_in.connect(login_success,sender=User)
@receiver(user_logged_out,sender=User)
def logout_success(sender, request, user, **kwargs):
    print("Logout Success")
    print("Sender:", sender)
    print("Request:", request)
    print("User:", user)

@receiver(user_login_failed)
def login_failed(sender, credentials, request, **kwargs):
    print("Wrong Credentials")
    print("Sender:", sender)
    print("Request:", request)
    print("Credentials:", credentials)

# user_logged_out.connect(logout_success,sender=User)
@receiver(pre_save,sender=User)
def at_pre_save(sender,instance,**kwargs):
        print("Pre Save Signal")
        print("Sender:", sender)
        print("Instance:", instance)

@receiver(post_save,sender=User)
def at_post_save(sender,instance,created,**kwargs):
        if created:
            print("New Record Created")
        else:
            print("Record Updated")
        print("Sender:", sender)
        print("Instance:", instance)

@receiver(pre_delete,sender=User)
def at_pre_delete(sender,instance,**kwargs):
        print("Pre Delete Signal")
        print("Sender:", sender)
        print("Instance:", instance)

@receiver(post_delete,sender=User)
def at_post_delete(sender,instance,**kwargs):
        print("Post Delete Signal")
        print("Sender:", sender)
        print("Instance:", instance) 

@receiver(pre_init,sender=User)
def at_pre_init(sender, *args,**kwargs):
        print("Pre Init Signal")
        print("Sender:", sender)
        print("Args:", args)
        print("Kwargs:", kwargs)

@receiver(post_init,sender=User)
def at_post_init(sender, *args,**kwargs):
        print("Post Init Signal")
        print("Sender:", sender)
        print("Args:", args)
        print("Kwargs:", kwargs)

@receiver(request_started)
def at_request_started(sender,environ, **kwargs):
        print("Request Started Signal")
        print("Sender:", sender)
        print("Environ:", environ)

@receiver(request_finished)
def at_request_finished(sender, **kwargs):
        print("Request Finished Signal")
        print("Sender:", sender)

@receiver(got_request_exception)
def at_got_request_exception(sender, request, **kwargs):
        print("Got Request Exception Signal")
        print("Sender:", sender)
        print("Request:", request)

@receiver(pre_migrate)
def at_pre_migrate(sender,app_config,verbosity,interactive,using,plan,apps, **kwargs):
        print("Pre Migrate Signal")
        print("Sender:", sender)
        print("App Config:", app_config)
        print("Verbosity:", verbosity)
        print("Interactive:", interactive)
        print("Using:", using)
        print("Plan:", plan)
        print("Apps:", apps)
@receiver(post_migrate)
def at_post_migrate(sender,app_config,verbosity,interactive,using,plan,apps, **kwargs):
        print("Post Migrate Signal")
        print("Sender:", sender)
        print("App Config:", app_config)
        print("Verbosity:", verbosity)
        print("Interactive:", interactive)
        print("Using:", using)
        print("Plan:", plan)
        print("Apps:", apps)
        
@receiver(connection_created)
def at_connection_created(sender, connection, **kwargs):
        print("Connection Created Signal")
        print("Sender:", sender)
        print("Connection:", connection)