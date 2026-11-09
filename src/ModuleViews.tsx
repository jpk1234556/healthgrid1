import { useEffect, useState } from "react";
import { api } from "./api";
import type { Patient, Referral } from "./api";

type ModuleName = "patients" | "referrals" | "emergency" | "records" | "reports";
type ModuleViewsProps = { module: ModuleName };

function ModuleHeader({ eyebrow, title, description, action }: { eyebrow: string; title: string; description: string; action: string }) {
  return <section className="module-heading"><div><p className="eyebrow">{eyebrow}</p><h1>{title}</h1><p className="subtitle">{description}</p></div><button className="primary-button">+ {action}</button></section>;
}

function DataState({ message }: { message: string }) {
  return <div className="data-state"><b>{message}</b><span>Data will appear here after the backend is connected and records are available.</span></div>;
}

function PatientsView() {
  const [patients, setPatients] = useState<Patient[]>([]);
  const [search, setSearch] = useState("");
  const [state, setState] = useState<"loading" | "ready" | "error">("loading");
  useEffect(() => { setState("loading"); api.getPatients(search).then((data) => { setPatients(data.results); setState("ready"); }).catch(() => setState("error")); }, [search]);
  return <><ModuleHeader eyebrow="PATIENT REGISTRY" title="Patients" description="Search patients registered in the connected care network." action="Register patient" /><section className="panel module-panel"><div className="module-toolbar"><label className="search-box"><span>⌕</span><input value={search} onChange={(event) => setSearch(event.target.value)} placeholder="Search by name or HealthGrid ID" /></label></div>{state === "loading" && <DataState message="Loading patients..." />}{state === "error" && <DataState message="Patient data could not be loaded." />}{state === "ready" && patients.length === 0 && <DataState message="No patients found." />}{state === "ready" && patients.length > 0 && <div className="data-table"><div className="table-row table-head"><span>HealthGrid ID</span><span>Patient</span><span>Facility</span><span>Status</span><span /></div>{patients.map((patient) => <div className="table-row" key={patient.id}><span className="mono">{patient.healthgrid_id}</span><b>{patient.full_name}</b><span>{patient.registered_facility_name}</span><span className={`tag ${patient.status}`}>{patient.status}</span><button className="row-action" aria-label={`Open ${patient.full_name}`}>→</button></div>)}</div>}</section></>;
}

function ReferralsView() {
  const [referrals, setReferrals] = useState<Referral[]>([]);
  const [state, setState] = useState<"loading" | "ready" | "error">("loading");
  useEffect(() => { api.getReferrals().then((data) => { setReferrals(data.results); setState("ready"); }).catch(() => setState("error")); }, []);
  const pending = referrals.filter((referral) => referral.status === "pending");
  const inProgress = referrals.filter((referral) => referral.status === "in_progress");
  const completed = referrals.filter((referral) => referral.status === "completed");
  return <><ModuleHeader eyebrow="COORDINATION DESK" title="Referrals" description="Track handoffs between connected facilities." action="Create referral" />{state === "loading" && <section className="panel module-panel"><DataState message="Loading referrals..." /></section>}{state === "error" && <section className="panel module-panel"><DataState message="Referral data could not be loaded." /></section>}{state === "ready" && referrals.length === 0 && <section className="panel module-panel"><DataState message="No referrals found." /></section>}{state === "ready" && referrals.length > 0 && <section className="panel module-panel"><div className="panel-heading"><div><p className="eyebrow">DATABASE RECORDS</p><h2>Referral board</h2></div></div><div className="referral-board"><ReferralColumn title="Pending acceptance" referrals={pending} /><ReferralColumn title="In progress" referrals={inProgress} /><ReferralColumn title="Completed" referrals={completed} /></div></section>}</>;
}

function ReferralColumn({ title, referrals }: { title: string; referrals: Referral[] }) {
  return <div><h3>{title} <span>{referrals.length}</span></h3>{referrals.map((referral) => <div className="referral-card" key={referral.id}><b>{referral.patient_name}</b><small>{referral.specialty} · {referral.origin_name} → {referral.destination_name}</small><em>{referral.priority} · {new Date(referral.created_at).toLocaleString()}</em></div>)}</div>;
}

function NotConfiguredView({ title, description }: { title: string; description: string }) {
  return <><ModuleHeader eyebrow="NOT CONFIGURED" title={title} description={description} action="Unavailable" /><section className="panel module-panel"><DataState message="This module has no database model yet." /></section></>;
}

export function ModuleView({ module }: ModuleViewsProps) {
  if (module === "patients") return <PatientsView />;
  if (module === "referrals") return <ReferralsView />;
  if (module === "emergency") return <NotConfiguredView title="Emergency coordination" description="Emergency incidents and receiving capacity will appear after their database models are implemented." />;
  if (module === "records") return <NotConfiguredView title="Records access" description="Consent, access requests, and audit events will appear after the governance models are implemented." />;
  return <NotConfiguredView title="Reports" description="Reports will appear after reporting data models and approved aggregation rules are implemented." />;
}
