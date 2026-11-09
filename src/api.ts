const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000/api";

export type Patient = {
  id: number;
  healthgrid_id: string;
  full_name: string;
  given_name: string;
  family_name: string;
  date_of_birth: string | null;
  registered_facility_name: string;
  status: string;
};

export type Referral = {
  id: number;
  patient_name: string;
  patient: number;
  specialty: string;
  priority: string;
  status: string;
  origin_name: string;
  destination_name: string;
  created_at: string;
};

export type Overview = {
  patients_total: number;
  referrals_active: number;
  referrals_pending: number;
  referrals_in_progress: number;
  referrals_completed_today: number;
};

async function get<T>(path: string): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    credentials: "include",
    headers: { Accept: "application/json" },
  });
  if (!response.ok) {
    throw new Error(response.status === 401 || response.status === 403 ? "Authentication required" : `Request failed (${response.status})`);
  }
  return response.json() as Promise<T>;
}

  async function getList<T>(path: string): Promise<{ results: T[] }> {
    const data = await get<T[] | { results: T[] }>(path);
    return Array.isArray(data) ? { results: data } : data;
  }

export const api = {
  getOverview: () => get<Overview>("/overview/"),
    getPatients: (search = "") => getList<Patient>(`/patients/${search ? `?search=${encodeURIComponent(search)}` : ""}`),
    getReferrals: () => getList<Referral>("/referrals/"),
};
