import React from 'react';
import Dashboard from './Dashboard';
import GlobeVisualization from './GlobeVisualization';

function App() {
  return (
    <div className="App">
      <h1>Reddit Sentiment Analysis</h1>
      <Dashboard />
      <GlobeVisualization />
    </div>
  );
}

export default App;
