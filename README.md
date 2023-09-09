# Detection of Phished URL using Machine Learning

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

This project focuses on detecting phished URLs using machine learning techniques. It utilizes Django and Django REST Framework to create an API for URL classification. The project includes feature extraction, model training, and deployment for real-time URL classification.

## Features

- Phished URL detection using machine learning algorithms
- Feature extraction based on various URL attributes
- Django framework for API development
- Bootstrap and jQuery for frontend development

## Getting Started

To get started with this project, follow these steps:

### Prerequisites

- Python 3.x
- Django
- Django REST Framework
- Other required dependencies (specified in `requirements.txt`)

### Installation

- Sequentially execute this code  

   ```bash
  1. git clone https://github.com/your-username/phished-url-detection.git
  2. pip install -r requirements.txt
  3. python manage.py migrate
  4. python manage.py runserver
  ```
## Usage
- Visit the homepage to access the URL classification interface.
- Enter a URL in the provided input field.
- Click the "Classify" button to initiate the classification process.
- The system will analyze the URL using the pre-trained Gradient Boosting model.
- The classification result (phished or not phished) will be displayed on the page.

## Acknowledgments
Special thanks to the contributors and open-source projects that provided inspiration, guidance, and tools for this project.
