from visitor import models
import uuid
def personuser(userdata):
    newuser = models.User()
    newuser.userid = uuid.uuid4()


    pass