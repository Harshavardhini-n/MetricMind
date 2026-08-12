"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { ConnectionStatus } from "@/components/connection-status";
const links=[["Home","/"],["Chat","/chat"],["Dashboards","/dashboards"],["Saved Queries","/history"],["Semantic Models","/semantic-models"],["SQL Explorer","/sql-explorer"],["Warehouse","/warehouse"],["AI Agents","/agents"],["History","/history"],["Settings","/settings"]];
export function AppShell({children}:{children:React.ReactNode}){const path=usePathname();return <div className="shell"><aside className="side"><div className="brand"><i>◈</i> MetricMind</div><nav className="nav">{links.map(([name,href])=><Link className={path===href?"active":""} href={href} key={name}>{name}</Link>)}</nav><div className="side-footer"><b>Subiksha R.</b><br/>Acme Analytics<br/><br/><span className="status"><i className="dot"/> Workspace online</span></div></aside><main className="main"><header className="top"><input className="search" aria-label="Global search" placeholder="Search metrics, dashboards, queries…"/><ConnectionStatus/></header>{children}</main></div>}
