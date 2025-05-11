import React, { useState } from "react";

export default function UploadSchema() {
  const [fileName, setFileName] = useState(null);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setFileName(file.name);
      // You can handle uploading logic here
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
      <h1 className="text-2xl font-bold mb-4">Upload Table Schema</h1>
      <label className="cursor-pointer bg-white rounded-xl shadow-md px-6 py-3 hover:shadow-lg transition">
        <input
          type="file"
          className="hidden"
          onChange={handleFileChange}
          accept=".sql,.json,.txt"
        />
        <span>{fileName ? fileName : "Choose a file"}</span>
      </label>
    </div>
  );
}
