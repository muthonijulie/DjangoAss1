Include a README.md file in your project root that explains how to set up and run your project.

Blog Project
This is a Django-based project that allows users to manage blog posts. The application includes functionality for creating, reading, updating, and deleting posts.
To setup the project,clone the repository then cd to the project
git clone https://github.com/muthonijulie/DjangoAss1.git
cd blogpr
Create a Virtual Environment
python3 -m venv venv
source .lily/bin/activate
To set up the database,run the following commands to apply the migrations:
python3 manage.py makemigrations
python3 manage.py migrate
Create a Superuser so that you can access th Django admi site.Run the following commands:
python3 manage.py createsuperuser
Follow the prompts to set up the superuser.
Run the Development Server using the commands below:
python manage.py runserver
The project will be available at http://127.0.0.1:8000/.(localhost:8000)

Provide clear instructions on how to use the admin site to manage posts.

Using the Admin Site to Manage Posts
Navigate to http://127.0.0.1:8000/admin/ in your web browser. Log in using the superuser account created earlier.

Once logged in, you'll see the Django admin dashboard. You can manage posts by clicking on the Posts section.

Click "Add" next to Posts. Fill in the fields (title, content, author) and click "Save".
Click on the title of the post you want to edit, make changes, and click "Save".
In the list of posts, select the post you want to delete by checking the box next to them. Choose "Delete selected posts" from the action dropdown and confirm.
