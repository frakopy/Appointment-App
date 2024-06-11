# Barber Appointment Scheduling App

This is a Django application that allows users to schedule, cancel, and reschedule appointments with a barbershop using the Google Calendar API.

## Features

- **User Authentication**: Users can sign up and log in to the application.
- **Schedule Appointment**: Users can book an appointment with the barbershop.
- **Cancel Appointment**: Users can cancel their booked appointments.
- **Reschedule Appointment**: Users can change the time or date of their appointments.
- **List Appointments**: Users can view all their scheduled appointments.

## Requirements

- Python 3.x
- Django 3.x or higher
- Google API Client Library for Python
- OAuth2 credentials for Google Calendar API

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/barber-appointment-scheduling.git
    cd barber-appointment-scheduling
    ```

2. **Create a virtual environment and activate it:**
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up your Google Calendar API credentials:**
    - Go to the [Google Cloud Console](https://console.cloud.google.com/).
    - Create a new project or select an existing project.
    - Enable the Google Calendar API for your project.
    - Create OAuth 2.0 credentials and download the `credentials.json` file.
    - Save `credentials.json` in the root directory of the project.

5. **Run the migrations:**
    ```sh
    python manage.py migrate
    ```

6. **Create a superuser:**
    ```sh
    python manage.py createsuperuser
    ```

7. **Start the development server:**
    ```sh
    python manage.py runserver
    ```

8. **Access the application:**
    Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

1. **Sign Up / Log In**: 
    - Create a new account or log in with your existing credentials.

2. **Schedule an Appointment**: 
    - Navigate to the appointment scheduling page.
    - Select a date and time for your appointment and confirm.

3. **Cancel an Appointment**: 
    - Go to your list of scheduled appointments.
    - Select the appointment you wish to cancel and confirm cancellation.

4. **Reschedule an Appointment**: 
    - Go to your list of scheduled appointments.
    - Select the appointment you wish to reschedule.
    - Choose a new date and time and confirm.

5. **View Appointments**: 
    - Navigate to the appointments page to view all your scheduled appointments.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

If you wish to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## Contact

For any inquiries or feedback, please contact to frako789@gmail.com.

