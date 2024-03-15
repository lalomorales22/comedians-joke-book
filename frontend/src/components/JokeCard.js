// frontend/src/components/JokeCard.js

import React from 'react';

const JokeCard = ({ joke, onUpdate, onDelete }) => {
  const handleUpdate = () => {
    // Handle update logic
    onUpdate(joke.id);
  };

  const handleDelete = () => {
    // Handle delete logic
    onDelete(joke.id);
  };

  return (
    <div className="joke-card">
      <h3>{joke.joke_name}</h3>
      <p>{joke.joke_description}</p>
      <p>Created At: {new Date(joke.created_at).toLocaleString()}</p>
      <p>Percentage: {joke.percentage}%</p>
      <p>Love It: {joke.love_it}%</p>
      <button onClick={handleUpdate}>Update</button>
      <button onClick={handleDelete}>Delete</button>
    </div>
  );
};

export default JokeCard;