# Frontend FAQ Application

This project is a frontend application built with React that integrates with a Django backend FAQ application. It fetches and displays frequently asked questions (FAQs) from the backend and provides a user-friendly interface for users to view the questions and answers.

## Project Structure

```
frontend
├── public
│   ├── index.html         # Main HTML file for the application
│   └── favicon.ico        # Favicon for the application
├── src
│   ├── components
│   │   ├── FaqList.js     # Component to display a list of FAQs
│   │   └── FaqItem.js     # Component to display a single FAQ
│   ├── services
│   │   └── api.js         # API service for making requests to the backend
│   ├── App.js             # Main application component
│   ├── index.js           # Entry point of the React application
│   └── styles
│       └── App.css        # CSS styles for the application
├── package.json           # npm configuration file
├── .gitignore             # Files and directories to ignore by Git
└── README.md              # Documentation for the project
```

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd frontend
   ```

2. **Install Dependencies**
   Make sure you have Node.js installed. Then run:
   ```bash
   npm install
   ```

3. **Run the Application**
   Start the development server:
   ```bash
   npm start
   ```

4. **Access the Application**
   Open your browser and go to `http://localhost:3000` to view the application.

## Usage

- The application will fetch FAQs from the Django backend at the `/api/faqs/` endpoint.
- Users can view the list of FAQs, and clicking on an FAQ will display its details.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.