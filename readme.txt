Super user django admin
john
mydjangoapppassword

db details in settings.py

how to add model constraints
class Foo(models.Model):
    #  ... model stuff...
    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError('Start date is after end date')


python virtual environment
bash: source ~/Envs/house_app/bin/activate

open firewall with
sudo ufw allow from 192.168.1.0/24 to any port 8000
