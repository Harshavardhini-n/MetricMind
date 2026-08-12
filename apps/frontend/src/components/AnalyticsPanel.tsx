"use client";

import React from "react";

export default function AnalyticsPanel() {
  return (
    <section className="card" style={{ padding: 18 }}>
      <h3 style={{ marginBottom: 8 }}>Example Analytics</h3>
      <p style={{ color: "var(--muted)", marginBottom: 12 }}>Live analytics are generated from Snowflake through MetricMind.</p>

      <div className="analytics">
        <div className="cap-card">
          <strong>Revenue</strong>
          <div style={{ color: "var(--muted)", marginTop: 8 }}>Ask MetricMind for revenue totals and trends.</div>
        </div>
        <div className="cap-card">
          <strong>Profit</strong>
          <div style={{ color: "var(--muted)", marginTop: 8 }}>Analyze profit and margins across dimensions.</div>
        </div>
        <div className="cap-card">
          <strong>Regional Analysis</strong>
          <div style={{ color: "var(--muted)", marginTop: 8 }}>Compare performance across regions.</div>
        </div>
        <div className="cap-card">
          <strong>Quarterly Analysis</strong>
          <div style={{ color: "var(--muted)", marginTop: 8 }}>Drill into quarterly performance by region.</div>
        </div>
      </div>
    </section>
  );
}
