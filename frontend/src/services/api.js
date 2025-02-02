//Here are the contents for the file: /frontend/frontend/src/services/api.js

import axios from 'axios';

const API_URL = 'http://localhost:8000/api/faqs/';

export const fetchFAQs = async () => {
    try {
        const response = await axios.get(API_URL);
        return response.data;
    } catch (error) {
        console.error('Error fetching FAQs:', error);
        throw error;
    }
};