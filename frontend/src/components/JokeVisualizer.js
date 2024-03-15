// frontend/src/components/JokeVisualizer.js

import React from 'react';
import { TagCloud } from 'react-tagcloud';

const JokeVisualizer = ({ jokes }) => {
  const getTags = () => {
    const tags = {};

    jokes.forEach((joke) => {
      const jokeTags = joke.joke_description.split(' ');

      jokeTags.forEach((tag) => {
        if (tags[tag]) {
          tags[tag].count++;
        } else {
          tags[tag] = { value: tag, count: 1 };
        }
      });
    });

    return Object.values(tags);
  };

  const tags = getTags();

  return (
    <div className="joke-visualizer">
      <h2>Joke Keywords</h2>
      <TagCloud
        minSize={12}
        maxSize={35}
        tags={tags}
        className="tag-cloud"
      />
    </div>
  );
};

export default JokeVisualizer;