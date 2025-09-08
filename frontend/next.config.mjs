// next.config.mjs (or next.config.js if using ESM by default)
import path from "path";
import { fileURLToPath } from "url";
import dotenv from "dotenv";

// Resolve project root (where .env lives, one dir up from frontend/)
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

dotenv.config({ path: path.resolve(__dirname, "../.env") });

const nextConfig = {
    images: {
        domains: [
            "127.0.0.1",
            "localhost",
            `${process.env.AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com`,
        ],
    },
};

export default nextConfig;
