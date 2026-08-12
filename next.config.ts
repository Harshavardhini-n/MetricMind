import type { NextConfig } from "next";
import path from "node:path";
const nextConfig: NextConfig = {
  serverExternalPackages: ["snowflake-sdk"],
  outputFileTracingRoot: path.join(__dirname),
};
export default nextConfig;
