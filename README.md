# **Medicio Template with Django, MySQL, and M-Pesa Integration** 🚀

This project utilizes the **Medicio Bootstrap Template**, **Django** for backend development, a **MySQL database** powered by **XAMPP**, and integration with the **M-Pesa API** for secure payments.

---

## **🌟 Features**
- **Responsive Design**: Powered by the Medicio Bootstrap template for a modern and mobile-friendly UI.
- **Django Backend**: A robust and scalable backend using Python's Django framework.
- **MySQL Database**: Reliable data storage implemented using XAMPP for local hosting.
- **M-Pesa Payments**: Seamlessly integrated with the M-Pesa API.

---

## **🛠️ Technologies Used**

| Technology        | Purpose                                      |
|-------------------|----------------------------------------------|
| **Bootstrap**     | Front-end styling and responsiveness        |
| **Django**        | Backend web framework                       |
| **XAMPP & MySQL** | Database management                         |
| **M-Pesa API**    | Mobile payment integration                  |

---

## **📂 Project Structure**
Main points and files to remember
```
├── static/ # Static assets (CSS, JS, images) 
├── templates/ # HTML templates (Medicio-based) 
├── kotlinFinal/ # Main Django project folder 
│   ├── settings.py # Project configuration 
│   ├── urls.py # URL routing for the apps created in this django project
├── myapp/ # Django created app.
│   ├── credentials.py # M-Pesa API scripts
│   ├── forms.py # to allow forms to gather and fetch data from db
│   ├── models.py # Database models 
│   ├── views.py # View functions handling requests 
│   ├── urls.py # URL routing that allows views and other routing calls to work
└── README.md # Project documentation
```




## **🛑 Prerequisites**
Before you get started, ensure you have the following installed:

- **XAMPP**: To host the MySQL database locally.
- **Python & Virtualenv**: for use with Django backend.
- **Bootstrap**: Integrated via CDN or local assets.
- **M-Pesa API Key**: Obtain credentials from the Safaricom developer portal.



## **🚀 Setup Instructions**
1. Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name 
```
2. Start XAMPP  
   Open XAMPP Control Panel.  
   Start Apache and MySQL services.


3. Configure MySQL Database
   - Open phpMyAdmin from the XAMPP control panel.
   - Import the database schema from the database/ folder.


4. Set Up 💳 M-Pesa Integration
   - The project uses the M-Pesa Daraja API to handle payments.  
   - Ensure you have registered on Safaricom Developer Portal (Daraja) and obtained API keys for the sandbox or live environment.  
   - Update the M-Pesa API credentials in the credentials.py configuration file:
      - MPESA_CONSUMER_KEY = 'your_consumer_key'
      - MPESA_CONSUMER_SECRET = 'your_consumer_secret'

   - Make sure you have configured the callback URLs correctly in the credentials.py file and the functions in view.


5. Run the Application
   ``` bash
   python manage.py runserver
   ```
   - Access the application in your browser at http://127.0.0.1:8000 or any other free port. This is also specified in your settings.py file.


## **📝 License**

This project is licensed under the MIT License. See the LICENSE.txt file for details.



## **🌟 Acknowledgments**

- [XAMPP](https://www.apachefriends.org/download.html)
- [Bootstrap](https://getbootstrap.com)
- [Medicio Template](https://bootstrapmade.com/medicio-free-bootstrap-theme/)
- [Safaricom M-Pesa API](https://developer.safaricom.co.ke)

