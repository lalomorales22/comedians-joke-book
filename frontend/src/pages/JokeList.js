// frontend/src/pages/JokeList.js
import React from 'react';
import JokeCard from '../components/JokeCard';

const JokeList = ({ jokes, onUpdate, onDelete }) => {
  return (
    <div className="joke-list">
      {jokes.length > 0 ? (
        jokes.map((joke) => (
          <JokeCard key={joke.id} joke={joke} onUpdate={onUpdate} onDelete={onDelete} />
        ))
      ) : (
        <p>No jokes found!</p>
      )}
    </div>
  );
};

export default JokeList;
