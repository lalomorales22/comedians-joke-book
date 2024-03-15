// frontend/src/pages/JokeAnalytics.js
import React, { useState, useEffect } from 'react';
import { Bar } from 'react-chartjs-2';

const JokeAnalytics = ({ jokes }) => {
  const [chartData, setChartData] = useState({});

  const prepareChartData = () => {
    // Assuming each joke has a 'created_at' and a 'love_it' score for simplicity
    const jokeLabels = jokes.map(joke => joke.joke_name);
    const loveItScores = jokes.map(joke => joke.love_it);

    setChartData({
      labels: jokeLabels,
      datasets: [
        {
          label: 'Love It Score',
          data: loveItScores,
          backgroundColor: 'rgba(255, 99, 132, 0.2)',
          borderColor: 'rgba(255, 99, 132, 1)',
          borderWidth: 1,
        },
      ],
    });
  };

  useEffect(() => {
    if (jokes.length) {
      prepareChartData();
    }
  }, [jokes]);

  return (
    <div className="joke-analytics">
      <h2>Joke Analytics</h2>
      <Bar data={chartData} options={{ scales: { y: { beginAtZero: true } } }} />
    </div>
  );
};

export default JokeAnalytics;
