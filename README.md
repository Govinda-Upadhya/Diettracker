Diet Tracker

Features

1.	User Authentication
   
o	Sign up and sign in features for user accounts.
o	User profile management to personalize diet tracking.

2.	Daily Diet Goal
   
o	Set and monitor daily diet intake goals.

3.	Diet Tracking
   
o	Easily enter and update daily food consumption.
o	View your diet log in both visual and tabular representations.

4.	Visual Representation
   
o	graphs to visualize your daily dietary intake.

5.	Tabular Representation
   
o	Detailed table view for a comprehensive analysis of your daily diet. 

Installation

1.	Clone the Repository
   
git clone https://github.com/Govinda-Upadhya/Diettracker.git

2.	Set Up Virtual Environment (Optional)
   
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3.	Database Setup
   
Configure your database settings in settings.py.

4.	Migrate the Database
   
python manage.py makemigrations
python manage.py migrate

5.	Create a Superuser (Admin) Account
   
python manage.py createsuperuser

6.	Run the Development Server
python manage.py runserver
Diet Tracker web app will now be accessible at http://localhost:8000/.


Screenshots
Signup Page





![Screenshot 2023-11-09 140649](https://github.com/Govinda-Upadhya/Diettracker/assets/143345467/2ca517c4-be91-4edd-961e-5a803fa7acd3)



SignIn Page





![Screenshot 2023-11-09 140658](https://github.com/Govinda-Upadhya/Diettracker/assets/143345467/668a5f9b-2e7a-4be8-a819-48ce6224732d)



Daily Goal Page




![Screenshot 2023-11-09 140717](https://github.com/Govinda-Upadhya/Diettracker/assets/143345467/26fe3355-704f-4c60-bd23-ca54ecf55e0b)




Tracker

![Screenshot 2023-11-09 140808](https://github.com/Govinda-Upadhya/Diettracker/assets/143345467/2cea9dbf-2764-4e33-9ca7-54d195e60080)

