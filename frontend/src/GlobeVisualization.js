import React, { useEffect, useRef } from 'react';
import Globe from 'globe.gl';

const GlobeVisualization = ({ onCountrySelect }) => {
  const globeEl = useRef();

  useEffect(() => {
    // Initialize the globe
    const globe = Globe()(globeEl.current)
      .globeImageUrl('//unpkg.com/three-globe/example/img/earth-blue-marble.jpg')
      .backgroundImageUrl('//unpkg.com/three-globe/example/img/night-sky.png')
      .onGlobeClick((latLng) => handleCountryClick(latLng));

    globe.controls().autoRotate = true;
    globe.controls().autoRotateSpeed = 0.7;
  }, []);

  const handleCountryClick = (latLng) => {
    const country = findCountryFromLatLng(latLng);  // Implement this function to map lat/lng to country
    if (country) {
      // Zoom into the selected country
      globeEl.current.pointOfView({ lat: country.lat, lng: country.lng, altitude: 1.5 }, 2000);

      // Fetch metrics for the selected country from the backend
      fetch(`/api/country/${country.name}`)
        .then(res => res.json())
        .then(data => onCountrySelect(country.name, data))  // Pass country and data to App
        .catch(error => console.error('Error fetching data:', error));
    }
  };

  return (
    <div>
      <div ref={globeEl} style={{ height: '600px' }} />
    </div>
  );
};

export default GlobeVisualization;
