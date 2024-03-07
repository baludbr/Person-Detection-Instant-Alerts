# Person Detection & Instant Alerts

## Introduction
This project encompasses a system designed to detect individuals from camera feeds and promptly send their pictures to a designated Telegram chat. Additionally, it involves the development of a responsive web application where users can manage their registered devices with proper authentication. The project prioritizes security by encrypting and storing user data in a MongoDB database.

## Features
- **Person Detection**: Utilizes OpenCV for real-time person detection from camera feeds.
- **Instant Alerts**: Sends detected person's images instantly to a designated Telegram chat.
- **Responsive Web Interface**: Provides a user-friendly interface allowing users to register and remove devices securely.
- **Authentication**: Implements authentication mechanisms to ensure secure access to the web interface.
- **Secure Data Storage**: Utilizes MongoDB for storing and maintaining user data securely with encryption to maintain confidentiality.
- **Authorized Development**: Authorized and supported by Kognitiv Club.

## Tech Stack
- **OpenCV**: Utilized for person detection from camera feeds.
- **Telegram APIs**: Used for sending instant alerts to designated chat.
- **Django**: Framework employed for developing the responsive web interface.
- **MongoDB**: Chosen for storing and maintaining user data securely with encryption.

## Installation
1. Clone the repository:
    ```
    git clone https://github.com/Person-Detection-Instant-Alerts.git
    ```
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Set up MongoDB database and configure database settings.
4. Configure Telegram API credentials.
5. Run the Django server:
    ```
    python manage.py runserver
    ```

## Usage
1. Access the web interface through the provided URL.
2. Register your devices and set up authentication credentials.
3. Ensure cameras are properly set up for person detection.
4. Receive instant alerts on the designated Telegram chat upon person detection.

## Contributors
- [Balaji Reddy Dwarampudi](https://github.com/baludbr) - BackEnd Developer & Lead
- [Pavan Mandavilli](https://github.com/Pavanmandavilli) - CV Developer
- [Durga JayaSai Pillagolla](https://github.com/Durgajayasai1) - Database Administrator

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgements
Special thanks to Kognitiv Club for their authorization and support throughout the development process.
