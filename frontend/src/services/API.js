const BASE_URL = "http://localhost:8000";

export async function postCheckIn(colegioId) {
  const response = await fetch(`${BASE_URL}/checkin`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ colegio_id: colegioId }),
  });

  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.detail); // fastAPI puts error messages in "detail"
  }

  return response.json();
}

export async function getRecords(start, end) {
  const response = await fetch(`${BASE_URL}/records?start=${start}&end=${end}`);

  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.detail);
  }

  return response.json();
}
