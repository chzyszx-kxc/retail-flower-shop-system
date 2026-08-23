import { defineConfig, loadEnv } from "vite";
import uni from "@dcloudio/vite-plugin-uni";

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, ".");

  return {
    plugins: [uni()],

    server: {
      proxy: {
        "/api": {
          target: env.VITE_API_ORIGIN,
          changeOrigin: true,
        }
      }
    }
  };
});