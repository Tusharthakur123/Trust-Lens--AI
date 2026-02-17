import React, { useState } from "react";
import { analyzeImage } from "./api";

function Upload({ setResult }) {
  const [image, setImage] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("image", image);
    formData.append("seller_rating", 4.7);
    formData.append("base_price", 15000);

    const result = await analyzeImage(formData);
    setResult(result);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="file" onChange={(e) => setImage(e.target.files[0])} />
      <button type="submit">Analyze Product</button>
    </form>
  );
}

export default Upload;
