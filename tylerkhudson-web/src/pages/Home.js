import React from 'react';
import '../styles/Home.css';
import DadJokeProvider from '../components/DadJoke';

function Home() {
  return (
    <div className="home-container">
      <h1>Welcome to the mind of Tyler!</h1>
      <h2>DevSecOps | Game Dev | FullStack</h2>
      <p>Hello World!</p>
      <DadJokeProvider />
    </div>
  );
}

export default Home;
