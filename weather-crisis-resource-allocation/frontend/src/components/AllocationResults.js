export default function AllocationResults({ results }) {
  return (
    <div style={{ marginTop: "2rem" }}>
      <h2>Results</h2>
      <pre>{JSON.stringify(results, null, 2)}</pre>
    </div>
  );
}

