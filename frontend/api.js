// api.js
import axios from 'axios';

// IP-ul backend-ului tău pe laptop + portul corect
const API_URL = 'http://192.168.1.4:8000';  // <--- portul FastAPI corect

// Funcție pentru înregistrarea unui utilizator
export const registerUser = async (username, email, password) => {
  try {
    const response = await axios.post(`${API_URL}/users/`, {
      username,
      email,
      password
    });
    return response.data;  // returnează datele utilizatorului creat
  } catch (error) {
    console.error('Register error:', error.response?.data || error.message);
    throw error;  // propagă eroarea ca să poată fi prinsă în UI
  }
};

// Funcție pentru autentificarea unui utilizator
export const loginUser = async (username, password) => {
  try {
    const response = await axios.post(`${API_URL}/users/login`, {
      username,
      password
    });
    return response.data;  // returnează datele utilizatorului logat
  } catch (error) {
    console.error('Login error:', error.response?.data || error.message);
    throw error;  // propagă eroarea pentru alert UI
  }
};
