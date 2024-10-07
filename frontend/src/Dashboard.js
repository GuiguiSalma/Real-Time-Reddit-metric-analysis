import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Dashboard = () => {
  const [subreddit, setSubreddit] = useState('all');
  const [metrics, setMetrics] = useState({});
  const [topWords, setTopWords] = useState([]);

  useEffect(() => {
    fetchMetrics();
    fetchTopWords();
  }, [subreddit]);

  const fetchMetrics = async () => {
    const response = await axios.get(`/api/metrics/${subreddit}`);
    setMetrics(response.data);
  };

  const fetchTopWords = async () => {
    const response = await axios.get(`/api/top-words/${subreddit}`);
    setTopWords(response.data);
  };

  return (
    <div>
      <h2>Metrics for {subreddit}</h2>
      <input
        type="text"
        value={subreddit}
        onChange={(e) => setSubreddit(e.target.value)}
        placeholder="Enter a subreddit"
      />
      <div>
        <h3>Total Upvotes: {metrics.upvotes || 'N/A'}</h3>
        <h3>Total Comments: {metrics.comments || 'N/A'}</h3>
      </div>
      <div>
        <h3>Top Words</h3>
        <ul>
          {topWords.map((word, index) => <li key={index}>{word}</li>)}
        </ul>
      </div>
    </div>
  );
};

export default Dashboard;
