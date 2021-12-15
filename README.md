# InTeleGent
Organized Chat for Doctors and Patients with Facebook Integration

# Setting up Django on your machine
# 1. Make sure you have Python 3 installed and included in PATH
# 2. Clone the repository locally on your machine
# 3. Open powershell (or cmd)
# 4. Install pip (python -m pip install)
# 5. Go to the local qllect repo directory (cd <folder path>)
# 6. Install pipenv (pip install pipenv) and add to PATH
# 7. Start a virtual environment subshell (pipenv shell)
# 8. Install the required libraries and django (pipenv install -r requirements.txt)
# 9. Update the files (python manage.py makemigrations)
# 10. Migrate files (python manage.py migrate)
# 11. Run the server (python manage.py runserver)

# The server should be up and runing. Open a browser and go to http://127.0.0.1:8000/ (or whatever is stated in cmd)
# You should be able to see the homepage

# Every time you want to freshly start the server, repeat steps 3,5,7,9,10,11

# Running your server across your local wifi
# 1. Edit the settings.py file and add your local IPv4 adderss inside the ALLOWED_HOSTS = [] line
#       example ALLOWED_HOSTS = ['192.168.1.3']             
#       ipconfig in your shell to see your IP addresses. 
# 2. When you run the server add your IP:port in the end
#       python manage.py runserver 192.168.1.3:8000
# 3. Open your mobile browser and enter your server IP:port in the address bar. The site should be visible
