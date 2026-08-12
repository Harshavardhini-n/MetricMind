"use client";

import React from "react";

const QUERIES: { label: string; query: string }[] = [
  { label: "Revenue Overview", query: "What is the total revenue?" },
  { label: "Regional Revenue", query: "Compare revenue across all regions." },
  { label: "Quarterly Revenue", query: "What is the revenue in East in Q1?" },
  { label: "Highest Revenue", query: "Which region has the highest revenue?" },
  { label: "Lowest Revenue", query: "Which region has the lowest revenue?" },
  { label: "Profit Overview", query: "What is the total profit?" },
];

export default function QuickQueries({ onQuick }: { onQuick: (q: string) => void }) {
  return (
    <div>
      <div style={{ color: "var(--muted)", marginBottom: 8 }}>Quick queries</div>
      <div className="quick-queries">
        {QUERIES.map((q) => (
          <button key={q.label} onClick={() => onQuick(q.query)}>
            {q.label}
          </button>
        ))}
      </div>
    </div>
  );
}
