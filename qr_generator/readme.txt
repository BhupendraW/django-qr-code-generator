QR Code Generator Web Application
===================================

Description:
-------------
This is a simple QR Code Generator built using Django, Bootstrap, and Python's QR tools.
It allows users to enter a URL, generate a QR code from that URL, preview the QR code, and download it with a single click.

Features:
---------
- Generates QR code for any URL.
- Preview the generated QR code before downloading.
- One-click download feature for the QR code.

Technologies Used:
------------------
- **Django**: Web framework for backend development.
- **Bootstrap**: Frontend framework for responsive UI.
- **Python**: Programming language for backend logic.
- **qrcode**: Python library to generate QR codes.
- **Pillow**: Python Imaging Library (PIL) to handle image processing (saving the QR code image).
- **HTML/CSS**: Frontend technologies for UI styling.

Required Libraries:
-------------------
Before running the project, you need to install the following Python libraries:

1. **Django**: Web framework to build the application.
2. **qrcode**: Python library to generate QR codes.
3. **Pillow**: Imaging library for handling images.
4. **Bootstrap (via CDN)**: Used for frontend responsive design.

To install these libraries globally (without using a virtual environment), follow these steps:

1. **Install the Required Libraries**:
   Use `pip` to install the necessary dependencies. Run these commands:


Installation Guide:
--------------------
Follow the steps below to install and run the QR Code Generator web app locally.

1. **Clone the Repository**:
First, clone this project to your local machine using the following command:


2. **Navigate to Project Directory**:

3. **Apply Migrations**:
Run the migrations to set up the database:


4. **Run the Development Server**:
Start the development server using the following command:


5. **Access the Application**:
Open your browser and visit `http://127.0.0.1:8000/` to access the QR Code Generator application.

Folder Structure:
-----------------
The project has the following folder structure:


How It Works:
--------------
1. Users visit the main page and enter a URL in the form.
2. When the user clicks "Generate QR Code," the URL is sent to the server.
3. The server uses the Python `qrcode` library to generate a QR code image.
4. The generated QR code is displayed to the user with a download button.

To Add More Features:
----------------------
- You can add user authentication for saving QR codes.
- Implement features like QR code history, or QR codes for more than just URLs (e.g., text, emails).
- Add user-friendly features like QR code styling (colors, logo integration).

Troubleshooting:
-----------------
- If you face any issues with database migrations, try running the following:

License:
--------
This project is open-source and free to use. Feel free to contribute or customize it according to your needs.

Developed by: Bhupendra Singh
