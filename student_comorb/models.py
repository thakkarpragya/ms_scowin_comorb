from django.db import models

# Create your models here.

class Student_reaction(models.Model):
    """
    Student model added here
    """
    id = models.CharField(primary_key=True, max_length=4)
    studentName = models.CharField(max_length=32)    
    existingComorbidites = models.CharField(max_length=300, null=True, blank=True)
    reaction = models.CharField(max_length=300, null=True, blank=True)
    severity = models.CharField(max_length=50, null=True, blank=True)
    remarks = models.CharField(max_length=300, null=True, blank=True)
    
    class Meta:
        """
        To override the database table name, use the db_table parameter in class Meta.
        """

    def __str__(self):
        return "{}".format(self.studentName)
        
