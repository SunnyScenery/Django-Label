## Quick Start

```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser # Create a superuser
python3 manage.py runserver
```

### Test Demo
first create a user by the admin, then use this user as the customer to test all functions.

For example, a customer named `testuser`.

the main page will show all the labels that this customer has.

click `add` button to add a new label.

click an existing label to `delete` or `update`.