import React, { useState } from 'react';
import Dashboard from './Dashboard';
import GlobeVisualization from './GlobeVisualization';

function App() {
  const [selectedCountry, setSelectedCountry] = useState(null);
  const [countryData, setCountryData] = useState(null);

  // Handler to update selected country and its metrics
  const handleCountrySelect = (country, data) => {
    setSelectedCountry(country);
    setCountryData(data);
  };

  return (
    <div className="App">
      <h1>Reddit Sentiment Analysis</h1>
      
      <GlobeVisualization onCountrySelect={handleCountrySelect} />

      {selectedCountry && (
        <Dashboard country={selectedCountry} data={countryData} />
      )}
    </div>
  );
}

export default App;
