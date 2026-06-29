import React, { useState } from 'react';

const UploadForm = ({ onUpload }) => {
  const [file, setFile] = useState(null);
  const [uploading, setUploading] = useState(false);

  const handleChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;

    setUploading(true);
    try {
      await new Promise(resolve => setTimeout(resolve, 2000));
      onUpload(file);
    } finally {
      setUploading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="manga-upload">Upload Manga Page:</label>
        <input
          type="file"
          id="manga-upload"
          accept="image/*"
          onChange={handleChange}
          disabled={uploading}
        />
      </div>
      <button type="submit" disabled={uploading || !file}>
        {uploading ? "Processing..." : "Process Manga"}
      </button>
    </form>
  );
};

export default UploadForm;
