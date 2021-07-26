from django.db import models as md


class Upload(md.Model):

    attachment = md.FileField(upload_to=get_filename)

    def __str__(self):
        return self.attachment.name
