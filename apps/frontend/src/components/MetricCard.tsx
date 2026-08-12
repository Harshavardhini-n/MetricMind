"use client";

import React from "react";

export default function MetricCard({ title, subtitle }: { title: string; subtitle?: string }) {
  return (
    <div className="card">
      <h4>{title}</h4>
      <div className="value">{subtitle ?? "Ask MetricMind"}</div>
    </div>
  );
}
