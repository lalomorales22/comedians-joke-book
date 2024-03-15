// frontend/src/pages/Home.js
import React, { useState, useEffect } from 'react';
import JokeList from './JokeList';
import JokeVisualizer from '../components/JokeVisualizer';
import { getJokes } from '../services/api';

const Home = () => {
  const [jokes, setJokes] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    const fetchJokes = async () => {
      const fetchedJokes = await getJokes();
      setJokes(fetchedJokes);
    };

    fetchJokes();
  }, []);

  const handleSearch = (event) => {
    setSearchTerm(event.target.value);
  };

  const filteredJokes = jokes.filter(joke =>
    joke.joke_name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    joke.joke_description.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div>
      <input
        type="text"
        placeholder="Search jokes..."
        value={searchTerm}
        onChange={handleSearch}
      />
      <JokeList jokes={filteredJokes} />
      <JokeVisualizer jokes={filteredJokes} />
    </div>
  );
};

export default Home;
