export async function sendAllocationRequest(input) {
  const response = await fetch("http://127.0.0.1:5000/allocate", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(input),
  });
  return await response.json();
}

