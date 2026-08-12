const blocked=/\b(insert|update|delete|drop|alter|create|truncate|merge|copy|put|remove|grant|revoke|call)\b/i;
const allowed=/^\s*(select|with|show|describe)\b/i;
export function validateSql(sql:string){const normalized=sql.trim().replace(/;+\s*$/g,"");if(!normalized)return {valid:false,error:"SQL is required."};if(sql.includes(";"))return {valid:false,error:"Multiple statements are not allowed."};if(!allowed.test(normalized)||blocked.test(normalized))return {valid:false,error:"Only safe, read-only SELECT, WITH, SHOW, and DESCRIBE statements are allowed."};return {valid:true,sql:normalized}}
