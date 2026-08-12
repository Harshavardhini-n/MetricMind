"use client";

import { useEffect, useState } from "react";

type Health = { success: boolean; data?: { snowflakeConfigured: boolean } };

export function ConnectionStatus() {
  const [configured, setConfigured] = useState<boolean | null>(null);
  useEffect(() => {
    fetch("/api/health")
      .then((response) => response.json() as Promise<Health>)
      .then((response) => setConfigured(Boolean(response.data?.snowflakeConfigured)))
      .catch(() => setConfigured(false));
  }, []);

  if (configured === null) return <span className="badge">Checking connection…</span>;
  return configured ? <span className="badge">Snowflake configured</span> : <span className="badge">Demo mode</span>;
}
