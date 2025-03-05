README.md:  
    ├── Description
    │   _This project is an API service that fetches product information 
    │   and similar products using an external service, 
    │   with caching mechanisms to improve performance and reduce redundant calls._
    │
    ├── Requirements
    │   # Python (version = 3.11)
    │
    ├── Setup Project
    │   # Steps for setup project for the first time.
    │
    ├── Setting up the project
    │   # Clone the repository
    │   # Create virtual environment: python -m venv venv
    │   # Activate virtual environment: source venv/bin/activate (linux, macOS) or venv\Scripts\activate (win)
    │   # Installed required dependencies: pip install -r requirements.txt
    │
    └── Run server in port 5000:
        # Command: daphne -b 0.0.0.0 -p 5000 core.asgi:application
    