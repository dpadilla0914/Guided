// # Vite configuration file for a React project. This file sets up the Vite development server and includes the React plugin to enable support for React features such as JSX. The configuration is defined using the `defineConfig` function from Vite, which allows for better type checking and IntelliSense in supported editors.
// import { defineConfig } from "vite";
// import react from "@vitejs/plugin-react";

// export default defineConfig({
//   plugins: [react()],
// });

//# Vite configuration file for a React project. This file sets up the Vite development server and includes the React plugin to enable support for React features such as JSX. The configuration is defined using the `defineConfig` function from Vite, which allows for better type checking and IntelliSense in supported editors. Additionally, the `server` configuration is set to allow all hosts, which can be useful for development in certain environments.
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    allowedHosts: true,
  },
});