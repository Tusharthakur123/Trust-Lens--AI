import axios from "axios";

export const analyzeImage = async (formData) => {
  const response = await axios.post("http://localhost:5000/analyze", formData);
  return response.data;
};
