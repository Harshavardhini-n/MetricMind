"use client";

import React from "react";

type DashboardTab =
  | "overview"
  | "analyst"
  | "regional"
  | "quarterly"
  | "profit"
  | "sources"
  | "settings";

type SidebarProps = {
  activeTab: DashboardTab;
  onNavigate: (tab: DashboardTab) => void;
};

const navItems: {
  id: DashboardTab;
  label: string;
  icon: string;
}[] = [
  {
    id: "overview",
    label: "Overview",
    icon: "⌂",
  },
  {
    id: "analyst",
    label: "AI Analyst",
    icon: "✦",
  },
  {
    id: "regional",
    label: "Regional",
    icon: "◫",
  },
  {
    id: "quarterly",
    label: "Quarterly",
    icon: "▣",
  },
  {
    id: "profit",
    label: "Profit",
    icon: "◉",
  },
  {
    id: "sources",
    label: "Data Sources",
    icon: "▤",
  },
  {
    id: "settings",
    label: "Settings",
    icon: "⚙",
  },
];

export default function Sidebar({
  activeTab,
  onNavigate,
}: SidebarProps) {
  return (
    <aside className="sidebar">
      {/* BRAND */}

      <div className="sidebar-brand">
        <div className="brand">MetricMind</div>
      </div>

      {/* NAVIGATION */}

      <nav className="nav">
        {navItems.map((item) => {
          const active =
            activeTab === item.id;

          return (
            <button
              key={item.id}
              type="button"
              className={`nav-item ${
                active ? "active" : ""
              }`}
              onClick={() => onNavigate(item.id)}
            >
              <span className="nav-icon">
                {item.icon}
              </span>

              <span>{item.label}</span>
            </button>
          );
        })}
      </nav>

      {/* SYSTEM STATUS */}

      <div className="sidebar-status">
        <div className="sidebar-status-title">
          SYSTEM STATUS
        </div>

        <div className="sidebar-status-row">
          <span className="status-dot" />
          Snowflake Connected
        </div>

        <div className="sidebar-status-row">
          <span className="status-dot" />
          API Connected
        </div>
      </div>

      {/* COLLAPSE BUTTON */}

      <button
        type="button"
        className="sidebar-collapse"
        aria-label="Collapse sidebar"
      >
        ‹
      </button>
    </aside>
  );
}