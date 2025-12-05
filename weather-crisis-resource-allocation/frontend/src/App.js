import React, { useState } from "react";
import InputForm from "./components/InputForm";
import AllocationResults from "./components/AllocationResults";

function App() {
  const [results, setResults] = useState(null);

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Weather Crisis Resource Allocation System</h1>
      <InputForm setResults={setResults} />
      {results && <AllocationResults results={results} />}
    </div>
  );
}

export default App;

