import React, { useEffect, useState } from 'react';

const JobStatus = ({ jobId, onComplete }) => {
  const [status, setStatus] = useState('pending');
  const [progress, setProgress] = useState(0);
  const [currentStep, setCurrentStep] = useState('');

  useEffect(() => {
    const interval = setInterval(async () => {
      try {
        if (status !== 'completed') {
          setProgress(prev => Math.min(prev + 10, 100));
          setCurrentStep(`Processing step ${Math.floor(Math.random() * 5) + 1}`);
          if (progress >= 100) {
            setStatus('completed');
            onComplete(jobId);
          }
        }
      } catch (err) {
        setStatus('failed');
      }
    }, 2000);

    return () => clearInterval(interval);
  }, [jobId, status, progress]);

  return (
    <div>
      <h2>Job Status</h2>
      <p>Job ID: {jobId}</p>
      <p>Status: {status}</p>
      <p>Progress: {progress}%</p>
      <p>Current Step: {currentStep}</p>
    </div>
  );
};

export default JobStatus;
