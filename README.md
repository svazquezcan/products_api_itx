# Description
_This project is an API service that fetches product information and similar products using an external service, 
with caching mechanisms to improve performance and reduce redundant calls._

# Requirements
Python (version = 3.11)

# Clone the repository and navigate into it
git clone <repository-url>
cd <repository-folder>

# Create and activate the virtual environment
python -m venv venv

# Activate virtual environment (Linux/macOS)
source venv/bin/activate || venv\Scripts\activate

# Install required dependencies
pip install -r requirements.txt

# Run the server on port 5000
daphne -b 0.0.0.0 -p 5000 core.asgi:application

    
