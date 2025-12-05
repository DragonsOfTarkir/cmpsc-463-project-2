import React, { useState } from "react";
import { sendAllocationRequest } from "../api";

export default function InputForm({ setResults }) {
  const [regions, setRegions] = useState("");
  const [supplies, setSupplies] = useState(50);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const regionList = JSON.parse(regions);
    const result = await sendAllocationRequest({
      regions: regionList,
      supplies: Number(supplies)
    });
    setResults(result);
  };

  return (
    <form onSubmit={handleSubmit}>
      <textarea
        rows="6"
        placeholder='[ {"name": "Region A", "need": 20, "urgency": 9} ]'
        value={regions}
        onChange={(e) => setRegions(e.target.value)}
        style={{ width: "400px" }}
      />
      <br />
      <input
        type="number"
        value={supplies}
        onChange={(e) => setSupplies(e.target.value)}
      />
      <button type="submit">Submit</button>
    </form>
  );
}

