// frontend/src/services/api.js

import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
});

export const createJoke = async (audioFile) => {
  const formData = new FormData();
  formData.append('audio', audioFile);

  try {
    const response = await api.post('/jokes', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    });
    return response.data;
  } catch (error) {
    console.error('Error creating joke:', error);
    throw error;
  }
};

export const getJokes = async () => {
  try {
    const response = await api.get('/jokes');
    return response.data; // Assuming this returns an array of jokes
  } catch (error) {
    console.error('Error retrieving jokes:', error);
    throw error;
  }
};

export const getJoke = async (jokeId) => {
  try {
    const response = await api.get(`/jokes/${jokeId}`);
    return response.data;
  } catch (error) {
    console.error('Error retrieving joke:', error);
    throw error;
  }
};

export const updateJoke = async (jokeId, updateData) => {
  try {
    const response = await api.put(`/jokes/${jokeId}`, updateData);
    return response.data;
  } catch (error) {
    console.error('Error updating joke:', error);
    throw error;
  }
};

export const deleteJoke = async (jokeId) => {
  try {
    const response = await api.delete(`/jokes/${jokeId}`);
    return response.status === 204; // true if successfully deleted
  } catch (error) {
    console.error('Error deleting joke:', error);
    throw error;
  }
};
