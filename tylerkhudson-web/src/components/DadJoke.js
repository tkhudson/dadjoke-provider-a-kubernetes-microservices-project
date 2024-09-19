import React, { useState, useEffect } from 'react';
import '../styles/DadJoke.css';

function DadJokeProvider() {
  const [joke, setJoke] = useState('');
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchJoke = async () => {
    setIsLoading(true);
    try {
      const response = await fetch('http://localhost:5002/joke');
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      setJoke(data.joke);
    } catch (e) {
      setError('Failed to fetch joke. Is the backend running?');
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchJoke();
  }, []);

  if (error) return <div>Error: {error}</div>;
  if (isLoading) return <div>Loading...</div>;

  return (
    <div className="dad-joke-container">
      <h2>Dad Joke of the Day:</h2>
      <p>{joke}</p>
      <button onClick={fetchJoke}>Get Another Joke</button>
    </div>
  );
}

export default DadJokeProvider;
