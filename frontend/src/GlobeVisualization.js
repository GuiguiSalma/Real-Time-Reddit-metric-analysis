import React, { useEffect, useRef } from 'react';
import Globe from 'globe.gl';
import axios from 'axios';

const GlobeVisualization = () => {
  const globeEl = useRef();

  useEffect(() => {
    const globe = Globe()(globeEl.current)
      .globeImageUrl('//unpkg.com/three-globe/example/img/earth-blue-marble.jpg')
      .backgroundImageUrl('//unpkg.com/three-globe/example/img/night-sky.png');

    fetchSubredditData(globe);

    return () => {
      globe.dispose();
    };
  }, []);

  const fetchSubredditData = async () => {
    const response = await axios.get('/api/globe-subreddit-data');
    globe.pointsData(response.data)
      .pointAltitude('upvotes')
      .pointColor(() => 'orange');
  };

  return <div ref={globeEl} style={{ width: '100%', height: '500px' }} />;
};

export default GlobeVisualization;
