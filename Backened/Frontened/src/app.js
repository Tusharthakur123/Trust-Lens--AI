import React, { useState } from "react";
import Upload from "./Upload";
import Report from "./Report";

function App() {
  const [result, setResult] = useState(null);

  return (
    <div>
      <h1>TrustLens AI</h1>
      <Upload setResult={setResult} />
      <Report result={result} />
    </div>
  );
}

export default App;
