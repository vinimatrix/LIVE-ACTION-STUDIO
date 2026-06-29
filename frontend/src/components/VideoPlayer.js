import React from 'react';

const VideoPlayer = ({ url }) => {
  return (
    <div>
      <h2>Result</h2>
      <video width="100%" controls>
        <source src={url} type="video/mp4" />
        Your browser does not support the video tag.
      </video>
    </div>
  );
};

export default VideoPlayer;
