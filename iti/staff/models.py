from django.db import models


# Create your models here.

# you will use this file to deal with the staff table in datbase

# staff --> name, image

# ORM ---> Class ,
class Departments(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return str(self.name)

class Staff(models.Model):
    name = models.CharField(max_length=100, db_column="fullname")  # string
    image = models.CharField(max_length=100)
    # Alter table staff add column  gender enum ('','')
    masters = models.BooleanField(null=True)   #### Not null
    gender = models.CharField(
        max_length=2,
        choices=[
            ("m", "male"),
            ("f", "female")
        ]
    )

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(null=True)  ## create field with type email
    # birthdate = models.DateField()

    ## define relation between department and staff member,
    # check the pk of departments
    # Alter table staffs add column dept int
    # Alter table staffs add constraint dept_fk foriegn key references department(id)
    # on update cascade, on delete cascade
    dept =models.ForeignKey(Departments, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)



