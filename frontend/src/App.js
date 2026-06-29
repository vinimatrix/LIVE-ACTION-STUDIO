import React, { useState } from 'react';
import UploadForm from './components/UploadForm';
import JobStatus from './components/JobStatus';
import VideoPlayer from './components/VideoPlayer';

function App() {
  const [jobId, setJobId] = useState(null);
  const [videoUrl, setVideoUrl] = useState(null);

  const handleUpload = async (file) => {
    setJobId(Math.floor(Math.random() * 1000));
  };

  const handleJobComplete = (id) => {
    setJobId(id);
    setVideoUrl(`/api/v1/jobs/result/${id}`);
  };

  return (
    <div className="App">
      <h1>AI Live Action Studio</h1>
      <UploadForm onUpload={handleUpload} />
      {jobId && <JobStatus jobId={jobId} onComplete={handleJobComplete} />}
      {videoUrl && <VideoPlayer url={videoUrl} />}
    </div>
  );
}

export default App;
